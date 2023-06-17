import logging
from copy import deepcopy

from aiogram import Router, Bot

from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery, FSInputFile


from database.database import users_db, user_dict_template
from filters.filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from keyboards.bookmarks_kb import (create_bookmarks_keyboard, create_edit_keyboard)
from keyboards.pagination_kb import create_pagination_keyboard
from keyboards.keyboards import game_kb, yes_no_kb, keyboard, start_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.answer_to_admin import answer_to_admin
from services.services import get_bot_choice, get_winner
from services.file_handling import book
from pprint import pprint

from config_data.config import Config, load_config
from services.sqlite import create_profile

router: Router = Router()
config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    print(message.from_user.first_name, message.from_user.id)
    pprint(message)
    await create_profile(user_id=message.from_user.id)
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU['/help'])


# Этот хэндлер срабатывает на команду /game и текст - Игра "Камень, ножницы, бумага"
@router.message(Command(commands=['game']))
async def process_start_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU['/game'], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON_RU['game']))
async def process_start_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU['/game'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на команду /game-help
@router.message(Command(commands=['game_help']))
async def process_help_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU['/game_help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_yes_answer(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(Text(text=LEXICON_RU['no_button']))
async def process_no_answer(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU['no'], reply_markup=start_kb)


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(Text(text=[LEXICON_RU['rock'],
                           LEXICON_RU['paper'],
                           LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await answer_to_admin(message)
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await answer_to_admin(message)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


# Этот хэндлер будет срабатывать на команду "/delmenu"
# и удалять кнопку Menu c командами
@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await bot.delete_my_commands()
    await answer_to_admin(message)
    await message.answer(text='Кнопка "Menu" удалена')


# Этот хэндлер будет срабатывать на команду "/url"
# и отправлять в чат клавиатуру c url-кнопками
@router.message(Command(commands='url'))
async def process_start_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(text='Это инлайн-кнопки с параметром "url"',
                         reply_markup=keyboard)


# Этот хэндлер будет срабатывать на команду "/book" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(Command(commands='book'))
async def process_start_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(LEXICON_RU['/book'])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


@router.message(Text(text=LEXICON_RU['book']))
async def process_start_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(LEXICON_RU['/book'])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


# Этот хэндлер будет срабатывать на команду "/help_book"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='book_help'))
async def process_help_command(message: Message):
    logging.info(f'сообщение: "{message.text}", user id: {message.from_user.id}, '
                 f'fullname: {message.from_user.full_name}')
    await answer_to_admin(message)
    await message.answer(LEXICON_RU['/book_help'])


# Этот хэндлер будет срабатывать на команду "/beginning"
# и отправлять пользователю первую страницу книги с кнопками пагинации
@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    users_db[message.from_user.id]['page'] = 1
    text = book[users_db[message.from_user.id]['page']]
    await answer_to_admin(message)
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[message.from_user.id]["page"]}/{len(book)}',
            'forward'))


# Этот хэндлер будет срабатывать на команду "/continue"
# и отправлять пользователю страницу книги, на которой пользователь
# остановился в процессе взаимодействия с ботом
@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    text = book[users_db[message.from_user.id]['page']]
    await answer_to_admin(message)
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[message.from_user.id]["page"]}/{len(book)}',
            'forward'))


# Этот хэндлер будет срабатывать на команду "/bookmarks"
# и отправлять пользователю список сохраненных закладок,
# если они есть или сообщение о том, что закладок нет
@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    await answer_to_admin(message)
    if users_db[message.from_user.id]["bookmarks"]:
        await message.answer(
            text=LEXICON_RU[message.text],
            reply_markup=create_bookmarks_keyboard(
                *users_db[message.from_user.id]["bookmarks"]))
    else:
        await message.answer(text=LEXICON_RU['no_bookmarks'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя с сообщением-книгой
@router.callback_query(Text(text='forward'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < len(book):
        users_db[callback.from_user.id]['page'] += 1
        text = book[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя с сообщением-книгой
@router.callback_query(Text(text='backward'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        text = book[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с номером текущей страницы и добавлять текущую страницу в закладки
@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
async def process_page_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].add(
        users_db[callback.from_user.id]['page'])
    await callback.answer('Страница добавлена в закладки!')


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок
@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery):
    text = book[int(callback.data)]
    users_db[callback.from_user.id]['page'] = int(callback.data)
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
            'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "редактировать" под списком закладок
@router.callback_query(Text(text='edit_bookmarks'))
async def process_edit_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU[callback.data],
        reply_markup=create_edit_keyboard(
            *users_db[callback.from_user.id]["bookmarks"]))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "отменить" во время работы со списком закладок (просмотр и редактирование)
@router.callback_query(Text(text='cancel'))
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['cancel_text'])
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок к удалению
@router.callback_query(IsDelBookmarkCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].remove(
        int(callback.data[:-3]))
    if users_db[callback.from_user.id]['bookmarks']:
        await callback.message.edit_text(
            text=LEXICON_RU['/bookmarks'],
            reply_markup=create_edit_keyboard(
                *users_db[callback.from_user.id]["bookmarks"]))
    else:
        await callback.message.edit_text(text=LEXICON_RU['no_bookmarks'])
    await callback.answer()


