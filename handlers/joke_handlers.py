import logging

from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram import Router

from keyboards.keyboards import create_joke_keyboard, start_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.answer_to_admin import answer_to_admin
from services.parser_joke import joke


router: Router = Router()

# Этот хэндлер срабатывает на текст joke
@router.message(Text(text=[LEXICON_RU['joke'], '/joke', 'joke', LEXICON_RU['yes_joke']]))
async def process_joke_yes_text(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=joke(), reply_markup=create_joke_keyboard(
                LEXICON_RU['yes_joke'], LEXICON_RU['no_joke']))

# Этот хэндлер срабатывает на нажатие инлайн кнопки yes_joke
@router.callback_query(Text(text=[LEXICON_RU['yes_joke']]))
async def process_joke_yes_text(callback: CallbackQuery):
    logging.info(f'сообщение: "yes_joke", user id: {callback.message.chat.id}, '
                 f'fullname: {callback.message.chat.full_name}')
    await callback.message.answer(text=joke(), reply_markup=callback.message.reply_markup)
    await callback.answer()

# Этот хэндлер срабатывает на нажатие инлайн кнопки no_joke
@router.callback_query(Text(text=[LEXICON_RU['no_joke']]))
async def process_joke_no_text(callback: CallbackQuery):
    logging.info(f'сообщение: "no_joke", user id: {callback.message.chat.id}, '
                 f'fullname: {callback.message.chat.full_name}')
    await callback.message.answer(text='Печалька , тогда давай займемся чем-то другим\n\n'
                                        'Выбирай!', reply_markup=start_kb)
    await callback.answer()