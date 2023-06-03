from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder на команду /start -------

# Создаем кнопки с ответами game, book, weather, joke
button_game: KeyboardButton = KeyboardButton(text=LEXICON_RU['game'])
button_book: KeyboardButton = KeyboardButton(text=LEXICON_RU['book'])
button_weather: KeyboardButton = KeyboardButton(text=LEXICON_RU['weather'])
button_joke: KeyboardButton = KeyboardButton(text=LEXICON_RU['joke'])
button_phraz: KeyboardButton = KeyboardButton(text=LEXICON_RU['phraz'])


# Инициализируем билдер для клавиатуры с кнопками game и book
start_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
start_kb_builder.row(button_game, button_book, button_weather, button_joke, button_phraz, width=2)

# Создаем клавиатуру с кнопками game и book
start_kb = start_kb_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb = yes_no_kb_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)


# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1],
                                              [button_2],
                                              [button_3]],
                                    resize_keyboard=True)

# Создаем объекты инлайн-кнопок
url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api')
group_name = 'aiogram_stepik_course'
url_button_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Группа "Телеграм-боты на AIOgram"',
    url=f'tg://resolve?domain={group_name}')
channel_name = 'toBeAnMLspecialist'
url_button_4: InlineKeyboardButton = InlineKeyboardButton(
    text='Канал "Стать специалистом по машинному обучению"',
    url=f'https://t.me/{channel_name}')

# Создаем объект инлайн-клавиатуры
# keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
#     inline_keyboard=[[url_button_1],
#                      [url_button_2],
#                      [url_button_3],
#                      [url_button_4],
#                      [url_button_5]])
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2],
                     [url_button_3],
                     [url_button_4]])


# Функция, генерирующая клавиатуру для модуля Анекдоты
def create_joke_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_RU[button] if button in LEXICON_RU else button,
        callback_data=button) for button in buttons])
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Функция, генерирующая клавиатуру для модуля Крылатые фразы
def create_phraz_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_RU[button] if button in LEXICON_RU else button,
        callback_data=button) for button in buttons])
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def get_kb_create() -> ReplyKeyboardMarkup:
    button1 = KeyboardButton(text='Начать заполнение анкеты')
    button2 = KeyboardButton(text='Не буду заполнять')

    kb_create = ReplyKeyboardMarkup(keyboard=[[button1, button2]],
                                    resize_keyboard=True)
    return kb_create

def get_kb_cancel() -> ReplyKeyboardMarkup:
    button1 = KeyboardButton(text='Передумал заполнять')
    kb_cancel = ReplyKeyboardMarkup(keyboard=[[button1]],
                                    resize_keyboard=True)
    return kb_cancel

def get_kb_gender():
    # Создаем объекты инлайн-кнопок
    male_button = InlineKeyboardButton(text='Мужской ♂',
                                       callback_data='Мужской')
    female_button = InlineKeyboardButton(text='Женский ♀',
                                         callback_data='Женский')
    undefined_button = InlineKeyboardButton(text='🤷 Пока не ясно',
                                            callback_data='Пока не ясно')
    # Добавляем кнопки в клавиатуру (две в одном ряду и одну в другом)
    keyboard: list[list[InlineKeyboardButton]] = [[male_button, female_button],
                                                  [undefined_button]]
    # Создаем объект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup

def get_kb_education():
    # Создаем объекты инлайн-кнопок
    secondary_button = InlineKeyboardButton(text='Среднее',
                                            callback_data='Среднее')
    higher_button = InlineKeyboardButton(text='Высшее',
                                         callback_data='Высшее')
    no_edu_button = InlineKeyboardButton(text='🤷 Нету',
                                         callback_data='Нету')
    # Добавляем кнопки в клавиатуру (две в одном ряду и одну в другом)
    keyboard: list[list[InlineKeyboardButton]] = [
        [secondary_button, higher_button],
        [no_edu_button]]
    # Создаем объект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup