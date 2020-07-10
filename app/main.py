# from flask import Flask
# from flask import request
# from flask import jsonify
# import requests
# import json
#
# app = Flask(__name__)
#
# URL = 'https://api.telegram.org/bot1191345010:AAGQ1vSTvKqDj0I_LnVjNGFTou8dU454YQE/'
#
# # @app.route('/')
# # def index():
# #     return '<h1>Flask app</h1>'
#
#
# def write_json(data, filename='answer.json'):
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)
#
#
# def get_updates():
#     url = URL + 'getUpdates'
#     r = requests.get(url)
#     # write_json(r.json())
#     return r.json()
#
#
# def send_message(chat_id, text='bla-bla'):
#     url = URL + 'sendMessage'
#     answer = {'chat_id': chat_id, 'text': text}
#     r = requests.post(url, json=answer)
#     return r.json()
#
#
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         r = request.get_json()
#         chat_id = r['message']['chat']['id']
#         message = r['message']['text']
#         write_json(r)
#         return jsonify(r)
#     return '<h1>Bot welcomes you</h1>'
#
#
# def main():
#     r = get_updates()
#     chat_id = r['result'][-1]['message']['chat']['id']
#     print(chat_id)
#     send_message(chat_id)
#
#
# if __name__ == '__main__':
#     app.run()
