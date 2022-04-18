from lib2to3.pgen2 import token
from urllib import request
import requests

token1 = '5340193945:AAH3sCzG-ylrRXsBZj7nhHqNX-Paa486I4k'
chat_id = '-543296554'
text = 'тест_2'

def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token1 + '/sendMessage'    

    req = requests.post(method, data={'chat_id':chat_id , 'text':text})

sendTelegram()
