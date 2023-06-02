LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nмы можем почитать книгу "/book";\n\nсыграть в игру "/game";\n\n'
              'узнать погоду в твоём любимом (или не очень) городе "/weather";\n\n'
              'почитать анекдоты "/joke";\n\nпрочитать крылатые фразы великого Ёжи Леца "/phraz";\n\n'
              'узнать что есть на Youtube нового по запросу "/search_youtube";\n\n ну и '
              'насколько ты богат в разных валютах "/converter".\n\n'
              'Выбирай!',
    'game': 'Игра "Камень 🗿, ножницы ✂, бумага 📜"',
    'book': 'Читать книгу 📖',
    '/game': 'Давай с тобой сыграем в игру '
              '"Камень, ножницы, бумага"?\n\nЕсли ты, вдруг, '
              'забыл правила, команда /game_help тебе поможет!\n\n<b>Играем?</b>',
    '/game_help': 'Это очень простая игра. Мы одновременно должны '
             'сделать выбор одного из трех предметов. Камень, '
             'ножницы или бумага.\n\nЕсли наш выбор '
             'совпадает - ничья, а в остальных случаях камень '
             'побеждает ножницы, ножницы побеждают бумагу, '
             'а бумага побеждает камень.\n\n<b>Играем?</b>',
    'rock': 'Камень 🗿',
    'paper': 'Бумага 📜',
    'scissors': 'Ножницы ✂',
    'yes_button': 'Давай!',
    'no_button': 'Не хочу!',
    'other_answer': 'Извини, увы, это сообщение мне непонятно...\n\n'
                    'Если совсем запутался всегда можно начать сначала щелкнув по\n\n<b>/start</b>',
    'yes': 'Отлично! Делай свой выбор!',
    'no': 'Жаль...\nЕсли захочешь сыграть, просто разверни '
          'клавиатуру и нажми кнопку "Камень 🗿, ножницы ✂, бумага 📜"',
    'bot_won': 'Я победил!\n\nСыграем еще?',
    'user_won': 'Ты победил! Поздравляю!\n\nДавай сыграем еще?',
    'nobody_won': 'Ничья!\n\nПродолжим?',
    'bot_choice': 'Мой выбор',
    'forward': '>>',
    'backward': '<<',
    '/book': '<b>Привет, читатель!</b>\n\nЭто бот, в котором '
              'ты можешь прочитать книгу Рэя Брэдбери "Марсианские '
              'хроники"\n\nЧтобы посмотреть список доступных '
              'команд - набери /book_help',
    '/book_help': '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'перейти в начало книги\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    '/bookmarks': '<b>Это список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактировать закладки</b>',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение',
    '/help': '- Вы можете сыграть в игру "Камень, ножницы, бумага" наберите "/game";\n\n'
             '- почитать книгу Рэя Брэдбери "Марсианские хроники" наберите "/book";\n\n-узнать '
             'погоду в любом городе "/weather";\n\n'
              '- почитать анекдоты "/joke";\n\n- прочитать крылатые фразы великого Ёжи Леца "/phraz";\n\n'
              '- узнать что есть на Youtube нового по запросу "/search_youtube";\n\n- ну и '
              'насколько ты богат в разных валютах "/converter".\n\n'
              'Выбирай!',
    'weather': 'Узнать погоду ⛅',
    'joke': 'Прочитать анекдот 😜',
    'yes_joke': 'Еще анекдотик',
    'no_joke': 'Пока хватит',
    'phraz': 'Крылатые фразы Ёжи Леца',
    'yes_phraz': 'Еще фраза?',
    'no_phraz': 'Пока хватит фраз'
            }


LEXICON_COMMANDS_RU: dict[str, str] = {
    '/start': 'Начать общение',
    '/book': 'Почитать книгу',
    '/game': 'Играть в игру камень-ножницы-бумага',
    '/help': 'Справка по работе бота',
    '/beginning': 'В начало книги',
    '/continue': 'Продолжить чтение',
    '/bookmarks': 'Мои закладки',
    '/url': 'Перейти на внешние ресурсы '}
