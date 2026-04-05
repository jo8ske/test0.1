from aiogram import Dispatcher, types
from services.youtube import search_youtube
from services.downloader import download_audio
from services.spotify import get_track_name
from utils.cache import get_cached, save_cache

def register(dp: Dispatcher):
    dp.register_message_handler(handle_music, content_types=["text"])

async def handle_music(message: types.Message):
    query = message.text

    await message.answer("🔍 Ищу...")

    # 🎧 Spotify → преобразуем в текст
    if "spotify.com" in query:
        query = get_track_name(query)

    # ⚡ кэш
    cached = get_cached(query)
    if cached:
        await message.answer_audio(open(cached, "rb"))
        return

    url = search_youtube(query)
    file_path = download_audio(url)

    save_cache(query, file_path)

    await message.answer_audio(open(file_path, "rb"))
