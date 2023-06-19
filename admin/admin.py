from aiogram import Router
from aiogram.filters import Text
from services.admin_anketa import get_ankets

router: Router = Router()


@router.callback_query(Text(text=['Показать пользователей']))
async def get_anket(callback):
    await callback.message.delete()
    for user in get_ankets():
        await callback.message.answer_photo(
            photo=user[1],
            caption=f'Имя: {user[2]}\n'
                    f'Email: {user[3]}\n'
                    f'Описание: {user[4]}\n'
                    f'Пол: {user[5]}\n'
                    f'Возраст: {user[6]}\n'
                    f'Образование: {user[7]}\n'
                    f'Время размещения: {user[8]}\n')

@router.message(Text(text=['Показать пользователей']))
async def get_anket(message):
    for user in get_ankets():
        if user[1]:
            await message.answer_photo(
                photo=user[1],
                caption=f'User_id: {user[0]}\n'
                        f'Имя: {user[2]}\n'
                        f'Email: {user[3]}\n'
                        f'Описание: {user[4]}\n'
                        f'Пол: {user[5]}\n'
                        f'Возраст: {user[6]}\n'
                        f'Образование: {user[7]}\n'
                        f'Время размещения: {user[8]}\n')
        else:
            await message.answer(
                text=f'User_id: {user[0]}\n'
                     f'Имя: {user[2]}\n'
                     f'Email: {user[3]}\n'
                     f'Описание: {user[4]}\n'
                     f'Пол: {user[5]}\n'
                     f'Возраст: {user[6]}\n'
                     f'Образование: {user[7]}\n'
                     f'Время размещения: {user[8]}\n')
