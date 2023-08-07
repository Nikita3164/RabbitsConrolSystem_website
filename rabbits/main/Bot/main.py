import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("""Здравствуйте!

Вы запустили бота для мониторинга кроликов.
Пока он только присылает сообщения о состоянии кроликов, но в дальнейшем он будет дорабатываться.                
    """)
    await sending('d', 'd', 'd')


async def sending(name, id, problem):
    await types.Message.answer(f"У кролика {name} {problem}, его ID - {id}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())