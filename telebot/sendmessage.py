from lib2to3.pgen2 import token
from urllib import request
import requests
from .models import telesettings 




def sendTelegram(tg_name, tg_phone):
    settings = telesettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_messgae)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'    

    a = text.find('{')
    b = text.find('}')
    c = text.rfind('{')
    d = text.rfind('}')

    part1 = text[0:a]
    part2 = text[b+1:c]
    part3 = text[d:-1]

    text_slise = part1 + tg_name + part2 + tg_phone + part3

    req = requests.post(method, data={'chat_id':chat_id , 'text':text_slise})


