import logging

from aiogram.filters import Text
from aiogram.types import Message, FSInputFile
from aiogram import Router

from config_data.config import load_config, Config
from lexicon.lexicon_ru import LEXICON_RU
from services import weather
from services.answer_to_admin import answer_to_admin
from services.weather import city_weather

router: Router = Router()
config: Config = load_config()


# Этот хэндлер срабатывает на текст weather
@router.message(Text(text=[LEXICON_RU['weather'], '/weather', 'weather']))
async def process_weather_text(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text='Введите сначала слово город затем название города например "город Москва"')

# Этот хэндлер срабатывает на ввод города для получения погоды
@router.message(Text(startswith='город', ignore_case=True))
async def process_weather_city(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=city_weather(' '.join(message.text.split()[1:]), config.tg_bot.weather_api))
    try:
        temp = weather.data['main']['temp']
        logging.info(f'температура в городе {" ".join(message.text.split()[1:]).title()}: {temp}')
        if temp < -10:
            image = r'media/frozen.jpg'
        elif -10 <= temp <= 20:
            image = r'media/prohladno.jpg'
        else:
            image = r'media/well_weather.jpg'
        photo = FSInputFile(image)
        await message.answer_photo(photo)
    except Exception:
        await message.answer(text='Для следующего выбора города отправьте сообщение с названием города')
