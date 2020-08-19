import json
import requests
import os
from sys import argv

#====================================
#set variables
#====================================

with open('env.sh') as file:
    url = str(file.readline())
    token = str(file.readline())
    chat_id=str(file.readline())
    command_api=str(file.readline())

#url=str(os.environ[telegram_url])
#token=str(os.environ[telegram_token])
#chat_id=str(os.environ[telegram_chatid])
#command_api=str(os.environ[telegram_command])

#====================================
#set messages
#====================================

text=str(argv[1])

#====================================
#send url split
#====================================

url=url+token+command_api
url=url.replace("\n","")
#====================================
#send messages
#====================================
def message_telegram(chat_id, text):
    json={"chat_id": chat_id, "text": text}
    r=requests.post(url,json=json)

message_telegram(chat_id, text)

