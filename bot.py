import asyncio
import logging

from aiogram import Bot, Dispatcher

from admin import admin
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers, weather_handlers, joke_handlers, phraz_handlers, quest_handlers
from keyboards.main_menu import set_main_menu
from services.psql import db_start

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Инициализируем базу данных
    await db_start()

    # Настраиваем кнопку Menu
    await set_main_menu(bot)


    # Регистриуем роутеры в диспетчере
    dp.include_router(admin.router)
    dp.include_router(quest_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(weather_handlers.router)
    dp.include_router(joke_handlers.router)
    dp.include_router(phraz_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    for adm in config.tg_bot.admin_ids:
        await bot.send_message(adm, 'Бот запущен')
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
