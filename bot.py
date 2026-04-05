from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from config import BOT_TOKEN
from handlers import start, music, photo

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register(dp)
music.register(dp)
photo.register(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
  
