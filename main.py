from pyrogram import Client
from pyrogram import filters, types, enums
import asyncio 
from config import *
from Plugin.helpers import *




def is_regex(data):
    async def func(flt, __, query: types.CallbackQuery):
        return query.data.split('|')[0] == flt.data
    return filters.create(func=func, data=data)

def is_sudo(data):
    async def func(flt, __, message):
        return message.from_user.id == flt.data
    return filters.create(func=func, data=data)

@app.on_message(filters.command('start'))
async def START_BOT(_, message: types.Message):
    join_, channl = await CHECK_USER_JOIN(API_KEY, CHANNLS_BOT, message.from_user.id)
    if not join_:
        await app.send_message(text=ADMIN_MESSAGE['JOIN_CHANLL'].format(channl), reply_markup=KeyboardMarkup.JOIN_CHANLL(channl),chat_id=message.chat.id)
        return 
    if not datas.user_exists(message.from_user.id):
        datas.NEW_USER_DATA(message.from_user.id)
        bot_data = datas.GET_BOT_DATA()
        if bot_data['admin_setting']['new_user']:
            await app.send_message(text=ADMIN_MESSAGE['NEW_USER'].format(
                message.from_user.id, 
                message.from_user.first_name, 
                message.from_user.username, 
                str(datetime.now())
            ), chat_id=SUDO)
        bot_data['users']+=1
        datas.UPDATE_BOT_DATA(bot_data)
        
    user_data = datas.GET_USER_DATA(message.from_user.id)
    await app.send_message(text=HOME_MESSAGE['HOME_MESSAGE'].format(user_data['emil']), chat_id= message.chat.id,reply_markup=KeyboardMarkup.HOME(user_data['emil']))



@app.on_callback_query(filters.regex('^checkjoin$'))
async def CHAECK_JOIN(_, query: types.CallbackQuery):
    await app.edit_message_text(text='انتضر جاري التحقق من الاشتراك ⚙️.', reply_markup=KeyboardMarkup.REDRESH_LANSHER('تحقق من الاشتراك♻️⚙️.'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.3)
    join_, channl = await CHECK_USER_JOIN(API_KEY, CHANNLS_BOT, query.from_user.id)
    if not join_:
        await app.edit_message_text(text=ADMIN_MESSAGE['JOIN_CHANLL'].format(channl), reply_markup=KeyboardMarkup.JOIN_CHANLL(channl) ,chat_id= query.message.chat.id, message_id=query.message.id)    
        await app.answer_callback_query(query.id, 'تأكد من اشتراك في القناة و اعد المحاولا ✅〽️.', show_alert=True)  
        return
    await app.edit_message_text(text=ADMIN_MESSAGE['DONE_JOIN_CHANNL'], chat_id= query.message.chat.id, message_id=query.message.id)






# Callback Query data.
@app.on_callback_query(filters.regex('^randmail$'))
async def RAND_MAIL(_, query: types.CallbackQuery):
    await app.edit_message_text(text='انتضر جاري توليد بريد  ⚙️.', reply_markup=KeyboardMarkup.REDRESH_LANSHER('توليد بريد عشوائي ♻️⚙️.'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.2)
    mail = apiV.Rand_Mail()[0]
    user_data = datas.GET_USER_DATA(query.from_user.id)
    await app.edit_message_text(text=HOME_MESSAGE['SELECT_MAIL'].format(mail), chat_id= query.message.chat.id, message_id=query.message.id, reply_markup=KeyboardMarkup.SELECT_MAIL(mail))

@app.on_callback_query(filters.regex('^refrshmail$'))
async def REFRESH_MAIL(_, query: types.CallbackQuery):
    await app.edit_message_text(text=HOME_MESSAGE['SELECT_MAIL'].format('NONE'), reply_markup=KeyboardMarkup.REDRESH_LANSHER('توليد بريد جديد ♻️⚙️.'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.3)
    mail = apiV.Rand_Mail()[0]
    user_data = datas.GET_USER_DATA(query.from_user.id)
    await app.edit_message_text(text=HOME_MESSAGE['SELECT_MAIL'].format(mail), chat_id= query.message.chat.id, message_id=query.message.id, reply_markup=KeyboardMarkup.SELECT_MAIL(mail))


@app.on_callback_query(filters.regex('^deletemail$'))
async def DELETE_MAIL(_, query: types.CallbackQuery):
    await app.edit_message_text(text='انتضر جاري حذف البريد 🗑⚙️..', reply_markup=KeyboardMarkup.REDRESH_LANSHER('حذف البريد ♻️⚙️.'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.6)
    user_data = datas.GET_USER_DATA(query.from_user.id)
    if user_data['emil'] == None:
        await app.edit_message_text(text='عذرن لا يوجد بريد لي يتم حذفه 🗑⚙️..', reply_markup=KeyboardMarkup.REDRESH_LANSHER('لا يوجد بريد ♻️⚙️.'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.2)
    datas.DELETE_EMIL(query.from_user.id) 
    user_data = datas.GET_USER_DATA(query.from_user.id)
    await app.edit_message_text(text=HOME_MESSAGE['HOME_MESSAGE'].format(user_data['emil']), chat_id= query.message.chat.id, message_id=query.message.id,reply_markup=KeyboardMarkup.HOME(user_data['emil']))
    
@app.on_callback_query(is_regex('selectmail'))
async def SELECT_MAIL_QUERY(_, query: types.CallbackQuery):
    await app.edit_message_text(text='انتضر جاري اختيار البريد ⚙️..', reply_markup=KeyboardMarkup.REDRESH_LANSHER('اختيار البريد ♻️⚙️.'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.2)
    emil_select = query.data.split('|')[1]
    datas.ADD_EMIL(query.from_user.id, emil_select)
    user_data = datas.GET_USER_DATA(query.from_user.id)
    bot_data = datas.GET_BOT_DATA()
    bot_data['emils']+=1
    datas.UPDATE_BOT_DATA(bot_data)
    if bot_data['admin_setting']['new_emil']:
        await app.send_message(chat_id=SUDO, text=ADMIN_MESSAGE['NEW_EMIL'].format(
            emil_select,
            query.from_user.id, 
            query.from_user.first_name,
            query.from_user.username,
            str(datetime.now())
        ))
    await app.edit_message_text(text=HOME_MESSAGE['HOME_MESSAGE'].format(user_data['emil']), chat_id= query.message.chat.id, message_id=query.message.id,reply_markup=KeyboardMarkup.HOME(user_data['emil']))
    

@app.on_callback_query(filters.regex('^readmessage$'))
async def READ_MESSAGE(_, query: types.CallbackQuery):
    user_data = datas.GET_USER_DATA(query.from_user.id)
    if user_data['emil'] == None:
        await app.answer_callback_query(query.id, 'عذرن لا يوجد لديك بريد قم بي اختيار بريد اولان 🧩💬.', show_alert=True)
        return 
    MailMessage = apiV.Get_All_Message(user_data['emil'])
    await app.edit_message_text(text=HOME_MESSAGE['READ_MESSAGE'].format(user_data['emil']), reply_markup=KeyboardMarkup.SHOW_MESSAGE(MailMessage,user_data['emil']),chat_id=query.message.chat.id, message_id=query.message.id)


@app.on_callback_query(is_regex('showmessage'))
async def SELECT_MAIL_QUERY(_, query: types.CallbackQuery):
    user_data = datas.GET_USER_DATA(query.from_user.id)
    message_id = query.data.split('|')[1]
    Message_obj = apiV.get_single_message(user_data['emil'], message_id)
    await app.edit_message_text(text=Message_obj['body'], reply_markup=KeyboardMarkup.BACK_BUTTON('readmessage'),chat_id=query.message.chat.id, message_id=query.message.id, disable_web_page_preview=True)

@app.on_callback_query(filters.regex('^backhome$'))
async def BACK_HOME(_, query: types.CallbackQuery):
    user_data = datas.GET_USER_DATA(query.from_user.id)
    await app.edit_message_text(text=HOME_MESSAGE['HOME_MESSAGE'].format(user_data['emil']), chat_id= query.message.chat.id, message_id=query.message.id,reply_markup=KeyboardMarkup.HOME(user_data['emil']))

@app.on_callback_query(filters.regex('^refreshmessag$'))
async def REFRESH_MESSAGE(_, query: types.CallbackQuery):
    user_data = datas.GET_USER_DATA(query.from_user.id)
    await app.edit_message_text(text='انتضر جاري تحديث الرسائل ⚙️..', reply_markup=KeyboardMarkup.REDRESH_LANSHER('تحديث الرسائل ♻️⚙️.'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.4)
    MailMessage = apiV.Get_All_Message(user_data['emil'])
    await app.edit_message_text(text=HOME_MESSAGE['READ_MESSAGE'].format(user_data['emil']), reply_markup=KeyboardMarkup.SHOW_MESSAGE(MailMessage,user_data['emil']),chat_id=query.message.chat.id, message_id=query.message.id)

# Admin or Sudo command
@app.on_message(filters.regex('^/admin$') & is_sudo(SUDO))
async def ADMIN_PANL(_, message: types.Message):
    bot_data = datas.GET_BOT_DATA()
    await app.send_message(text='لوحة المطور ', reply_markup=KeyboardMarkup.ADMIN_PANL(bot_data),chat_id=message.chat.id)



# on noticon 
@app.on_callback_query(filters.regex('^noticon_user$'))
async def NOTICONE_NEW_USER(_, query: types.CallbackQuery):
    bot_data = datas.GET_BOT_DATA()
    bot_data['admin_setting']['new_user'] = True if bot_data['admin_setting']['new_user'] == False else False 
    datas.UPDATE_BOT_DATA(bot_data)
    await app.edit_message_text(text='لوحة المطور ', reply_markup=KeyboardMarkup.ADMIN_PANL(bot_data), chat_id=query.message.chat.id, message_id=query.message.id)


@app.on_callback_query(filters.regex('^noticon_emil$'))
async def NOTICONE_NEW_USER(_, query: types.CallbackQuery):
    bot_data = datas.GET_BOT_DATA()
    bot_data['admin_setting']['new_emil'] = True if bot_data['admin_setting']['new_emil'] == False else False 
    datas.UPDATE_BOT_DATA(bot_data)
    await app.edit_message_text(text='لوحة المطور ', reply_markup=KeyboardMarkup.ADMIN_PANL(bot_data), chat_id=query.message.chat.id, message_id=query.message.id)

asyncio.run(app.run())