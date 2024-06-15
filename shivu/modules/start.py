import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        ***Heyyyy...***
 ***🌸𝙄 𝙖𝙢 𝘼𝙣 𝘽𝙤𝙩 𝙒𝙝𝙤 𝘾𝙧𝙚𝙖𝙩 𝙃𝙖𝙧𝙚𝙢𝙨 𝙊𝙛 𝙔𝙤𝙪𝙧𝙨 𝘼𝙣𝙞𝙢𝙚 𝘾𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨 𝘾𝙤𝙡𝙡𝙚𝙘𝙩𝙞𝙣𝙜 𝘽𝙤𝙩..​𝘼𝙙𝙙 𝙈𝙚 𝙞𝙣 𝙔𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥.. 𝘼𝙣𝙙 𝙄 𝙬𝙞𝙡𝙡 𝙨𝙚𝙣𝙙 𝙍𝙖𝙣𝙙𝙤𝙢 𝘾𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨 𝘼𝙛𝙩𝙚𝙧.. 𝙚𝙫𝙚𝙧𝙮 100 𝙢𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥... 𝙐𝙨𝙚 /𝙘𝙤𝙡𝙡𝙚𝙘𝙩 𝙩𝙤.. 𝘾𝙤𝙡𝙡𝙚𝙘𝙩 𝙩𝙝𝙖𝙩 𝘾𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨 𝙞𝙣 𝙔𝙤𝙪𝙧 𝘾𝙤𝙡𝙡𝙚𝙘𝙩𝙞𝙤𝙣.. 𝙖𝙣𝙙 𝙨𝙚𝙚 𝘾𝙤𝙡𝙡𝙚𝙘𝙩𝙞𝙤𝙣 𝙗𝙮 𝙪𝙨𝙞𝙣𝙜 /𝙃𝙖𝙧𝙚𝙢... 𝙎𝙤 𝙖𝙙𝙙 𝙞𝙣 𝙔𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥𝙨 𝙖𝙣𝙙 𝘾𝙤𝙡𝙡𝙚𝙘𝙩 𝙔𝙤𝙪𝙧 𝙃𝙖𝙧𝙚𝙢🌸***
        """
        
        keyboard = [
            [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("SUPPORT", url=f'https://t.me/namoHaremChat{SUPPORT_CHAT}'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/namopdates{UPDATE_CHAT}')],
            [InlineKeyboardButton("HELP", callback_data='help')],
         
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice("photo url", url=f'https://graph.org/file/877aecc1642bbb4804e3e.jpg')

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice ("photo url", url=f'https://graph.org/file/877aecc1642bbb4804e3e.jpg')]
        keyboard = [
            [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("HELP", callback_data='help')],
            
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="🎴Alive!?... \n connect to me in PM For more information ",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***Help Section:***
    
***/collect: To Guess character (only works in group)***
***/fav: Add Your fav***
***/trade : To trade Characters***
***/gift: Give any Character from Your Collection to another user.. (only works in groups)***
***/collection: To see Your Collection***
***/topgroups : See Top Groups.. Ppl Guesses Most in that Groups***
***/top: Too See Top Users***
***/htop : Your HaremTop***
***/settime: Change Character appear time (only works in Groups)***
   """
        help_keyboard = [[InlineKeyboardButton("⤾ Bᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        ***Hoyyyy...*** ✨
    
    ***🌸𝙄 𝙖𝙢 𝘼𝙣 𝘽𝙤𝙩 𝙒𝙝𝙤 𝘾𝙧𝙚𝙖𝙩 𝙃𝙖𝙧𝙚𝙢𝙨 𝙊𝙛 𝙔𝙤𝙪𝙧𝙨 𝘼𝙣𝙞𝙢𝙚 𝘾𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨 𝘾𝙤𝙡𝙡𝙚𝙘𝙩𝙞𝙣𝙜 𝘽𝙤𝙩..​𝘼𝙙𝙙 𝙈𝙚 𝙞𝙣 𝙔𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥.. 𝘼𝙣𝙙 𝙄 𝙬𝙞𝙡𝙡 𝙨𝙚𝙣𝙙 𝙍𝙖𝙣𝙙𝙤𝙢 𝘾𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨 𝘼𝙛𝙩𝙚𝙧.. 𝙚𝙫𝙚𝙧𝙮 100 𝙢𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥... 𝙐𝙨𝙚 /𝙘𝙤𝙡𝙡𝙚𝙘𝙩 𝙩𝙤.. 𝘾𝙤𝙡𝙡𝙚𝙘𝙩 𝙩𝙝𝙖𝙩 𝘾𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨 𝙞𝙣 𝙔𝙤𝙪𝙧 𝘾𝙤𝙡𝙡𝙚𝙘𝙩𝙞𝙤𝙣.. 𝙖𝙣𝙙 𝙨𝙚𝙚 𝘾𝙤𝙡𝙡𝙚𝙘𝙩𝙞𝙤𝙣 𝙗𝙮 𝙪𝙨𝙞𝙣𝙜 /𝙃𝙖𝙧𝙚𝙢... 𝙎𝙤 𝙖𝙙𝙙 𝙞𝙣 𝙔𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥𝙨 𝙖𝙣𝙙 𝘾𝙤𝙡𝙡𝙚𝙘𝙩 𝙔𝙤𝙪𝙧 𝙃𝙖𝙧𝙚𝙢🌸***

        
        keyboard = [
            [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("HELP", callback_data='help')],
            
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
