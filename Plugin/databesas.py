from datetime import datetime 
import json 
import os

class databesas:

    def __init__(self):
        self.PAT = './databesas/databesas.json'
        self.PAT_BOT = './databesas/bot.json'


    def GET_DATA(self, ):
        with open(self.PAT, 'r') as JSFile:
            obj = json.load(JSFile)
        return obj
    
    def UPDATE_DATA(self, NEW_DATA):
        with open(self.PAT, 'w') as JSObj:
            json.dump(NEW_DATA, JSObj, indent=3)

    def NEW_USER_DATA(self, user_id: int):
        obj = self.GET_DATA()
        obj.update({user_id:{
            'datetime':str(datetime.now()),
            'emil':None,
            'emil_data':{}
        }})
        self.UPDATE_DATA(obj)
        return obj 
    
    def GET_USER_DATA(self, user_id: int):
        datas = self.GET_DATA()
        return datas[str(user_id)]
    
    def ADD_EMIL(self, user_id: int, emil: str):
        datas = self.GET_DATA()
        datas[str(user_id)]['emil'] = emil
        datas[str(user_id)]['emil_data'] = {
            'datetime':str(datetime.now())
        }
        self.UPDATE_DATA(datas)

    def DELETE_EMIL(self, user_id: int):
        datas = self.GET_DATA()
        datas[str(user_id)]['emil'] = None
        datas[str(user_id)]['emil_data'] = {}
        self.UPDATE_DATA(datas)

    def user_exists(self, user_id: int):
        datas = self.GET_DATA()
        return str(user_id) in datas
    

    def GET_BOT_DATA(self, ):
        with open(self.PAT_BOT, 'r') as JSFile:
            obj = json.load(JSFile)
        return obj
    
    def UPDATE_BOT_DATA(self, NEW_DATA):
        with open(self.PAT_BOT, 'w') as JSObj:
            json.dump(NEW_DATA, JSObj, indent=3)
    





        
