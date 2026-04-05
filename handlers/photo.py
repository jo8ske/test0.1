from aiogram import Dispatcher, types
from services.ocr import extract_text
from services.youtube import search_youtube
from services.downloader import download_audio

def register(dp: Dispatcher):
    dp.register_message_handler(handle_photo, content_types=["photo"])

async def handle_photo(message: types.Message):
    await message.answer("📷 Читаю картинку...")

    photo = message.photo[-1]
    file = await message.bot.get_file(photo.file_id)

    path = f"temp_{photo.file_id}.jpg"
    await message.bot.download_file(file.file_path, path)

    text = extract_text(path)

    await message.answer(f"🔍 Найдено:\n{text}")

    url = search_youtube(text)
    file_path = download_audio(url)

    await message.answer_audio(open(file_path, "rb"))
