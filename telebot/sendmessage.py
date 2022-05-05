from lib2to3.pgen2 import token
from urllib import request
import requests
from .models import telesettings 




def sendTelegram(tg_name, tg_phone):
    if telesettings.objects.get(pk=1):
        settings = telesettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_messgae)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'    

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            a = text.find('{')
            b = text.find('}')
            c = text.rfind('{')
            d = text.rfind('}')

            part1 = text[0:a]
            part2 = text[b+1:c]
            part3 = text[d:-1]

            text_slise = part1 + tg_name + part2 + tg_phone + part3
        else:
            text_slise = text

            try:
                req = requests.post(method, data={'chat_id':chat_id , 'text':text_slise})
            except:
                pass
            finally:
                if req.status_code != 200:
                    print ("Send Error")
                elif req.status_code == 500:
                    print ("Error 500")
                else:
                    print ("All is OK")




