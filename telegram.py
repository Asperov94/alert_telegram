import json
import requests
import os
from sys import argv

#====================================
#set variables
#====================================

url=str(os.environ[telegram_url])
token=str(os.environ[telegram_token])
chat_id=str(os.environ[telegram_chatid])
#====================================
#set messages
#====================================
text=str(argv[1])



#====================================
#send messages
#====================================
json={"chat_id": chat_id, "text": text}
r=requests.post(url,json=json)

