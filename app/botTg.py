from app import config
import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from app.sqlighter import SQLighter


# инициализируем бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# инициализируем соединение с БД
db = SQLighter('../db.db')


# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем
        db.add_subscriber(message.from_user.id)
    else:
        # если он уже есть, обновляем статус подписки
        db.update_subscription(message.from_user.id, True)

    await message.answer(
        "Вы успешно подписались на рассылку!")


# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы и так не подписаны.")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки.")


# запускаем лонг поллинг
if __name__ == '__main__':
   # dp.loop.create_task(scheduled(10))  пока что оставим 10 секунд (в качестве теста)
    executor.start_polling(dp, skip_updates=True)
