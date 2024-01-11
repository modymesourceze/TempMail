from requests import get
import json 



class TempMailApi:

    def __init__(self, ):
        pass

    def Rand_Mail(self, count : int =1):
        api = f'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={count}'
        Mail = json.loads(get(api).text)
        return Mail

    def get_domen_list(self,):
        api = 'https://www.1secmail.com/api/v1/?action=getDomainList'
        Mail = json.loads(get(api).text)
        return Mail

    def Get_All_Message(self, emil: str):
        api = 'https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain={}'
        Emil_split = emil.split("@")
        Obj = json.loads(get(api.format(Emil_split[0],Emil_split[1])).text)
        return Obj
    
    def get_single_message(self, emil: str, id: int):
        api = 'https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain={}&id={}'
        Emil_split = emil.split("@")
        Obj = json.loads(get(api.format(Emil_split[0],Emil_split[1], id)).text)
        return Obj


async def CHECK_USER_JOIN(api_key, channls_join: list, user_id : int):
    c ,r = None ,False
    statues = ['administrator','creator','member','restricted']
    for channl in channls_join:
        url =f"https://api.telegram.org/bot{api_key}/getChatMember?chat_id=@{channl}&user_id={str(user_id)}"
        respons = get(url)
        JSObj = json.loads(respons.text) 
        user_state = JSObj['result']['status']
        if user_state in statues:
            r = True 
        else : 
            r = False
            c = channl
            return r,c
    return r,c