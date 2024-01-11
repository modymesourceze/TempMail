from mody import Mody
from pyrogram import Client
from Plugin.databesas import *
from Plugin.api import *
import os 

SUDO = 6581896306 # admin or sudo id
CHANNLS_BOT = ['Source_Ze'] # bot channls 


if not os.path.exists('./.session'):
    os.mkdir('./.session')

if not os.path.exists('./.databesas'):
    os.mkdir('./.databesas')

app = Client(
    '.session/rad',
    bot_token=Mody.TG_BOT_TOKEN, # API_KEY 
    api_hash=Mody.API_HASH, # UserBot api_hahs
    api_id=Mody.APP_ID # UserBot api_id 
)

datas, apiV = databesas(), TempMailApi()


