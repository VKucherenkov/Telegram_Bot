import random
from datetime import datetime


phraz_res = []


def phraz_days():
    with open(r'database/phraz_result.txt', 'r',
              encoding='utf-8') as file:
        phraz_day = [i.strip() for i in file.readlines()]
    some_data = datetime(2023, 6, 2)
    now_data = datetime.now()
    return phraz_day[(now_data - some_data).days % len(phraz_day)]


def phraz():
    global phraz_res
    if not len(phraz_res):
        with open(r'database/phraz_result.txt', 'r',
                  encoding='utf-8') as file:
            phraz_res = [i.strip() for i in file.readlines()]

    random.shuffle(phraz_res)
    phraz = phraz_res.pop(0)
    return phraz


if __name__ == '__main__':
    print(phraz_days())
