import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text, start, page_size):
    for i in range(start + page_size - 1, start - 1, -1):
        if len(text) - (start + page_size) <= 0:
            return [text[start: i + 1], len(text[start: i + 1])]
        elif text[i] not in ',.!:;?':
            continue
        elif text[i] in ',.!:;?' and text[i + 1] not in ',.!:;?':
            return [text[start: i + 1], len(text[start: i + 1])]


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    file = open(path, 'r', encoding='utf-8')
    book_txt = file.read()
    start = 0
    count = 1
    txt = len(book_txt)
    while txt > 0:
        get_part_text = _get_part_text(book_txt, start, PAGE_SIZE)
        book[count] = get_part_text[0].lstrip()
        start += get_part_text[1]
        txt -= get_part_text[1]
        count += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))

