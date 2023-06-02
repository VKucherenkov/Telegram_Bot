from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import Router

from keyboards.keyboards import create_phraz_keyboard, start_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.praz import phraz


router: Router = Router()

# Этот хэндлер срабатывает на текст phraz
@router.message(Text(text=[LEXICON_RU['phraz'], '/phraz', 'phraz']))
async def process_phraz_text(message: Message):
    image = r'media/photo_eji_lec.jpg'
    photo = FSInputFile(image)
    await message.answer_photo(photo)
    await message.answer(text=phraz(), reply_markup=create_phraz_keyboard(
                LEXICON_RU['yes_phraz'], LEXICON_RU['no_phraz']))

# Этот хэндлер срабатывает на нажатие инлайн кнопки yes_phraz
@router.callback_query(Text(text=[LEXICON_RU['yes_phraz']]))
async def process_phraz_text(callback: CallbackQuery):
    await callback.message.edit_text(text=phraz(), reply_markup=callback.message.reply_markup)
    # await callback.answer()


# Этот хэндлер срабатывает на нажатие инлайн кнопки no_phraz
@router.callback_query(Text(text=[LEXICON_RU['no_phraz']]))
async def process_phraz_no_text(callback: CallbackQuery):
    await callback.message.answer(text='Печалька, тогда давай займемся чем-то другим\n\n'
                                        'Выбирай!', reply_markup=start_kb)
    await callback.answer()