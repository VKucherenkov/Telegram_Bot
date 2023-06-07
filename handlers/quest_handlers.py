from pprint import pprint

from aiogram import Router
from aiogram.filters import Command, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.types import Message
from aiogram import F

from keyboards.keyboards import get_kb_cancel, get_kb_gender, get_kb_education, get_kb_create, start_kb
from services.sqlite import edit_profile

router: Router = Router()

# Создаем "базу данных" пользователей
user_dict: dict[int, dict[str, str | int | bool]] = {}



class ClientStatesGroup(StatesGroup):
    user_name = State()
    user_email = State()
    user_photo = State()
    user_desc = State()
    user_gender = State()
    user_age = State()
    user_education = State()



@router.message(Command(commands=['create']))
async def cmd_create(message: Message) -> None:
    pprint(message)
    await message.answer('Давай заполним анкетку', reply_markup=get_kb_create())


@router.message(Text(text='Передумал заполнять'))
async def process_cancel_create(message: Message, state: FSMContext):
    await message.answer(text='Жаль! Может в другой раз заполним.', reply_markup=get_kb_create())
    await state.clear()


@router.message(Text(text='Начать заполнение анкеты'), StateFilter(default_state))
async def process_start_create(message: Message, state: FSMContext):
    await message.answer(text='Напиши свое имя', reply_markup=get_kb_cancel())
    await state.set_state(ClientStatesGroup.user_name)


@router.message(StateFilter(ClientStatesGroup.user_name), F.text.isalpha())
async def process_name_create(message: Message, state: FSMContext):
    await message.answer(text=f'Ваше имя {message.text} сохранено.\n\n Теперь напиши свой email:', reply_markup=get_kb_cancel())
    await state.update_data(name=message.text)
    await state.set_state(ClientStatesGroup.user_email)



@router.message(StateFilter(ClientStatesGroup.user_name))
async def check_name(message):
    await message.answer(text='Это не имя. Напиши пожалуйста свое имя.')


@router.message(StateFilter(ClientStatesGroup.user_email), lambda x: x.text if "@" in x.text else False)
async def process_email_create(message: Message, state: FSMContext):
    await message.answer(text=f'Ваш email {message.text} сохранен.\n\n Теперь отправь пожалуйста фотографию:', reply_markup=get_kb_cancel())
    await state.update_data(user_email=message.text)
    await state.set_state(ClientStatesGroup.user_photo)

@router.message(StateFilter(ClientStatesGroup.user_email))
async def check_email(message):
    await message.answer(text='Это не email. Напиши пожалуйста свой email:')


@router.message(lambda x: x.photo, StateFilter(ClientStatesGroup.user_photo), F.photo[-1].as_('largest_photo'))
async def load_photo(message, state: FSMContext, largest_photo):
    await message.answer(text='Отлично а теперь добавь описание фотографии.')
    await state.update_data(photo=largest_photo.file_id, photo_unique_id=largest_photo.file_unique_id)
    await state.set_state(ClientStatesGroup.user_desc)

@router.message(StateFilter(ClientStatesGroup.user_photo))
async def check_photo(message):
    await message.answer(text='Это не фотография. Отправь пожалуйста фотографию:')


@router.message(lambda message: message.text, StateFilter(ClientStatesGroup.user_desc))
async def load_desc(message, state: FSMContext):
    await message.answer(text='Отлично описание сохранено.\n\n Теперь укажи пожалуйста свой пол:', reply_markup=get_kb_gender())
    await state.update_data(desc=message.text)
    await state.set_state(ClientStatesGroup.user_gender)

@router.message(lambda x: not x.text, StateFilter(ClientStatesGroup.user_desc))
async def check_desc(message):
    await message.answer(text='Это не описание фотографии.')


@router.callback_query(Text(text=['Мужской', 'Женский', 'Пока не ясно']), StateFilter(ClientStatesGroup.user_gender))
async def load_gender(callback, state: FSMContext):
    await state.update_data(gender=callback.data)
    await state.set_state(ClientStatesGroup.user_age)
    await callback.message.delete()
    await callback.message.answer(text='Спасибо! А теперь укажи свой возраст '
                                       'в полных годах:')

@router.message(StateFilter(ClientStatesGroup.user_gender))
async def check_gender(message):
    await message.answer(text='Это не похоже на пол. Выбери пожалуйста свой пол:', reply_markup=get_kb_gender())

@router.message(lambda x: x.text.isdigit() and 14 <= int(x.text) <= 150, StateFilter(ClientStatesGroup.user_age))
async def load_age(message, state: FSMContext):
    await message.answer(text='Отлично возраст сохранен.\n\n Теперь укажи пожалуйста своё образование:',
                         reply_markup=get_kb_education())
    await state.update_data(age=message.text)
    await state.set_state(ClientStatesGroup.user_education)

@router.message(StateFilter(ClientStatesGroup.user_age))
async def check_age(message):
    await message.answer(text='Это не похоже на возраст, введите пожалуйста Ваш возраст в полных годах.')


@router.callback_query(Text(text=['Среднее', 'Высшее', 'Нету']),
                       StateFilter(ClientStatesGroup.user_education))
async def load_education(callback, state: FSMContext):
    await state.update_data(education=callback.data)
    await callback.message.delete()
    await callback.message.answer(text='Спасибо! Заполнение анкеты завершено!'
                                       'Вот данные Вашей анкеты:')
    # Завершаем машину состояний
    user_dict[callback.message.chat.id] = await state.get_data()
    pprint(user_dict)
    print(user_dict.keys())
    pprint(callback.message)
    await edit_profile(user_dict, user_id=callback.message.chat.id)

    await state.clear()
    await callback.message.answer(text='Вот данные твоей анкеты:', reply_markup=start_kb)
    await callback.message.answer_photo(
        photo=user_dict[callback.message.chat.id]['photo'],
        caption=f'Имя: {user_dict[callback.message.chat.id]["name"]}\n'
                f'Email: {user_dict[callback.message.chat.id]["user_email"]}\n'
                f'Описание: {user_dict[callback.message.chat.id]["desc"]}\n'
                f'Пол: {user_dict[callback.message.chat.id]["gender"]}\n'
                f'Возраст: {user_dict[callback.message.chat.id]["age"]}\n'
                f'Образование: {user_dict[callback.message.chat.id]["education"]}\n')


@router.message(StateFilter(ClientStatesGroup.user_education))
async def check_education(message):
    await message.answer(text='Это не похоже на образование. Выбери пожалуйста своё образование:', reply_markup=get_kb_education())







