from aiogram import Dispatcher, types

def register(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])

async def start(message: types.Message):
    await message.answer(
        "🎵 Отправь:\n"
        "- название трека\n"
        "- ссылку YouTube / Spotify\n"
        "- фото (скрин песни)\n"
        "- или строчку из песни"
    )
