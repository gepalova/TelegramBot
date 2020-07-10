# import requests
# import json
#
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# from app import config
# from app.config import TOKEN
# from app.sqlighter import SQLighter
#
# token = config.TOKEN
# URL = 'https://api.telegram.org/bot' + token + '/'
#
#
# def get_updates():
#     url = URL + 'getUpdates'
#     r = requests.get(url)
#     return r.json()
#
#
# def get_message():
#     data = get_updates()
#     chat_id = data['result'][-1]['message']['chat']['id']
#     message_text = data['result'][-1]['message']['text']
#     message = {'chat_id': chat_id,
#                'text': message_text}
#     return message
#
#
# def send_message(chat_id, text="Wait a sec..."):
#     url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
#     requests.get(url)
#
#
# # инициализация бота
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# # инициализируем соединение с БД
# db = SQLighter('../db.db')
#
#
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Напиши что-нибудь!")
#
#
# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши что-нибудь, и я отпрпавлю этот текст в ответ!")
#
#
# # @dp.message_handler()
# # async def echo_message(msg: types.Message):
# #    await bot.send_message(msg.from_user.id, msg.text)
#
#
# # Команда активации подписки
# @dp.message_handler(commands=['subscribe'])
# async def subscribe(message: types.Message):
#     if (not db.subscriber_exists(message.from_user.id)):
#         # если юзера нет в базе, добавляем его
#         db.add_subscriber(message.from_user.id)
#     else:
#         # если он уже есть, то просто обновляем ему статус подписки
#         db.update_subscription(message.from_user.id, True)
#
#     await message.answer(
#         "Вы успешно подписались на рассылку!")
#
#
# # Команда отписки
# @dp.message_handler(commands=['unsubscribe'])
# async def unsubscribe(message: types.Message):
#     if (not db.subscriber_exists(message.from_user.id)):
#         # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
#         db.add_subscriber(message.from_user.id, False)
#         await message.answer("Вы и так не подписаны.")
#     else:
#         # если он уже есть, то просто обновляем ему статус подписки
#         db.update_subscription(message.from_user.id, False)
#         await message.answer("Вы успешно отписаны от рассылки.")
#
#
# def main():
#     # d = get_updates()
#     # with open('updates.json', 'w') as file:
#     #     json.dump(d, file, indent=2, ensure_ascii=False)
#     answer = get_message()
#     chat_id = answer['chat_id']
#     text = answer['text']
#
#     send_message(chat_id, 'Hihihello')
#
#
# if __name__ == '__main__':
#     main()
#     executor.start_polling(dp)
