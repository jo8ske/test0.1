from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.youtube import search_youtube
from services.downloader import download_audio
from services.spotify import get_track_name

# временное хранилище (можно потом заменить на БД)
user_queries = {}


def register(dp: Dispatcher):
    dp.register_message_handler(handle_music, content_types=["text"])
    dp.register_callback_query_handler(download_callback, lambda c: c.data.startswith("download"))


# 🎵 Когда пользователь пишет текст
async def handle_music(message: types.Message):
    query = message.text

    await message.answer("🔍 Ищу трек...")

    # Spotify → текст
    if "spotify.com" in query:
        query = get_track_name(query)

    url = search_youtube(query)

    # сохраняем для кнопки
    user_queries[message.from_user.id] = url

    # кнопка
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("⬇️ Скачать", callback_data="download")
    )

    await message.answer(
        f"🎵 Найдено!\n\n{query}",
        reply_markup=keyboard
    )


# ⬇️ Когда нажали кнопку
async def download_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    await callback.answer("⏳ Скачиваю...")

    url = user_queries.get(user_id)

    if not url:
        await callback.message.answer("❌ Ошибка, попробуй снова")
        return

    file_path = download_audio(url)

    await callback.message.answer_audio(open(file_path, "rb"))
