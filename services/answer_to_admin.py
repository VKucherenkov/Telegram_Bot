from aiogram import Bot

from config_data.config import Config, load_config

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')

async def answer_to_admin(message):
    await bot.send_message(config.tg_bot.admin_ids[0],
                           text=f'Пользователь {message.from_user.full_name} с id: '
                                f'{message.from_user.id} отправил текст {message.text}')