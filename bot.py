import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers import start, game_selection, service_selection, order_input

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем роутеры хендлеров
    dp.include_router(start.router)
    dp.include_router(game_selection.router)
    dp.include_router(service_selection.router)
    dp.include_router(order_input.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    print("Бот успешно запущен и начинает polling...")

if __name__ == "__main__":
    asyncio.run(main())