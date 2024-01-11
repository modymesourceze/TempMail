from pyrogram import types



# All Bot Message .
HOME_MESSAGE = {
    'HOME_MESSAGE':
                u'اهلان بك في بوت خدمة البريد الموقأت ♻️.'
                u'\n\n . ماذا يقدم البوت ? .🔰'
                u'\n - يمكنك من خلال البوت انشاء بريد موأقت او مهمل لي التسجيل في الموقع و الطبيقات ☑️⚜️.'
                u'\n\nEmil: {}'
                u'\n\n• 𝗗𝗘𝗩 - @ELHYBA - @Source_Ze 👨‍💻.',
    'SELECT_MAIL':
                u'قم بي اختيار البريد 🔱💭.'
                u'\n Emil : {}'
                u'\n\n لي اختيار البريد 🔗 Select ولي اضهار بريد جديد ♻️ Refresh .\n',

    'READ_MESSAGE':
                    u'قم بي اختيار الرسالة لي الدخول اليها 💭🔰.'
                    u'\n\n Emil : {}  💬.'
}

ADMIN_MESSAGE = {
    'NEW_USER':
                u'نم دخول عضو جديد الى البوت .'
                u'\n == === == == === === === === === == ==='
                u'\n id : {}'
                u'\n Name   : {}'
                u'\n username : {}'
                u'\n date :{}\n',

    'NEW_EMIL':
               u'تم تفعيل بريد جديد .'
               u'\n Emil  : {}'
               u'\n user_id : {}'
               u'\n user_name : {}'
               u'\n user_username : {}'
               u'\n date  : {}',
    'JOIN_CHANLL':
                u'عذرن عزيزي عليك الاشترك بي قناة البوت اولان لي استخدام البوت 🧩💬.'
                u'\n\n Channl : @{} 💭🔰.'
                u'\n\n  👇 قم بي الاشترك من ثم اضغط علا زر تحقق 🔱🔗 .'
                u'',

    'DONE_JOIN_CHANNL':
                        u'شكرأ لك على الاشتراك في قنات البوت 〽️🧩.'
                        u'\n\n الان فم بي ارسال ( /start ) لي تشغيل البوت ♻️🔱.'
                        u'\n\n اتمنة لك تجربا ممتعة ✅🤍'
                        u'\n معا تحيات ⧛ 𓆩 𝑴𝒐𝒅𝒚 ➫ ⁽𝑆₎𝑻𝒆𝒂𝒎 ࿐ 𝑫 𝒆 𝒗 𝒊 𝒍 𓆪 ⧚  - @ELHYBA 💬👨‍💻'
                        u''
                
                
}

# bot inlinekyebaord Markup

class KeyboardMarkup:

    def HOME(emil: str):
        
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text=f'{emil}', callback_data='not')
            ],[
                types.InlineKeyboardButton('RandMail 〽️💭.' if emil == None else 'Refresh ♻️💭.', callback_data='randmail'),
            ],
            [
                types.InlineKeyboardButton('Delete 🗑.', callback_data='deletemail'),
                types.InlineKeyboardButton('ReadMessage 💬.', callback_data='readmessage')
            ],
            
        ])

    def SELECT_MAIL(Emil: str):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text=Emil, callback_data='NOT')
            ],
            [
                types.InlineKeyboardButton(text='Refresh ♻️.', callback_data='refrshmail'), 
                types.InlineKeyboardButton(text='Select 🔗💭.', callback_data=f'selectmail|{Emil}')
            ]
        ])
    def REDRESH_LANSHER(text: str):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text=text, callback_data='NOT')
            ]
        ])
    
    def BACK_BUTTON(call: str):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(f'Back 🔙.', callback_data=call)
                
            ]
        ])
    
    def SHOW_MESSAGE(Messages: list, emil: str):
        ALL_MESSAGE = [
            [
                types.InlineKeyboardButton('Mail Message  💬.', callback_data='not'),
                types.InlineKeyboardButton(f'Refresh ♻️.', callback_data='refreshmessag'),
                types.InlineKeyboardButton(f'Back 🔙.', callback_data='backhome')
            ]]
        if not Messages:
            ALL_MESSAGE.append([
                types.InlineKeyboardButton('NO MESSAGE', callback_data='not'),
            ]) 
            
        for message_id in range(len(Messages)):
            ALL_MESSAGE.append([
                types.InlineKeyboardButton(Messages[message_id]['subject'], callback_data=f'showmessage|{Messages[message_id]["id"]}'),
                types.InlineKeyboardButton(Messages[message_id]['date'], callback_data='not')
            ])

        return types.InlineKeyboardMarkup(ALL_MESSAGE)
    

    def ADMIN_PANL(bot_data):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='الاحصأيات', callback_data='not')
            ],
            [
                types.InlineKeyboardButton(text=str(bot_data['users']), callback_data='not2'),
                types.InlineKeyboardButton(text='عدد الاعضاء', callback_data='not1')

            ],
            [
                types.InlineKeyboardButton(text=str(bot_data['emils']), callback_data='not4'),
                types.InlineKeyboardButton(text='عدد الايميلات', callback_data='not3')
            ],
            [
                types.InlineKeyboardButton(text='الاشعارات', callback_data='not5')
            ],
            [
                types.InlineKeyboardButton(text=bot_data['admin_setting']['new_user'], callback_data='not3'),
                types.InlineKeyboardButton(text='دخول عضو ', callback_data='noticon_user')
            ],
            [
                types.InlineKeyboardButton(text=bot_data['admin_setting']['new_emil'], callback_data='not3'),
                types.InlineKeyboardButton(text='بريد جديد', callback_data='noticon_emil')
            ],
        ])
    
    def JOIN_CHANLL(Channl: str):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='قناة البوت 〽️💭.', url=f't.me/{Channl}'),
                types.InlineKeyboardButton(text='تحقق ♻️.', callback_data='checkjoin')
            ]
        ])
    