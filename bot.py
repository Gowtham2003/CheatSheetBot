from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
import telegram
import os
from cheatsheet import querySh
from carbon import carbonize



def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def start(update,context):
    name = "Hello! " + update.message.from_user["first_name"]
    context.bot.send_message(chat_id=update.effective_chat.id,text=name)

    welcome = """
Hi I'm Your Portable Cheat Sheet

Send /help for Help 

Made With ❤️ In India By @Gowtham_2003

Join @AlphaProjects for More Projects and Updates
"""
    context.bot.send_message(chat_id=update.effective_chat.id,text=
welcome)


def help(update,context):
    helpmessage = '''
Send Me Any Language and Query to Me

I'll Send You Code Snippet based On Your Query

For Example : /query java append list

Type

/help to Get this Message 

/donate To Donate Me (Still Not Added)

/query [LANG] [QUERY]

/carbon To Create a Carbon of the code

if Any Issues Contact : @Gowtham_2003

A Part of @AlphaProjects 

'''
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpmessage)

def donate(update,context):
    donate = '''
Donate Feature Haven't Added Yet 

If You Want to Donate My Works 
Contact Me :
    Telegram : @Gowtham_2003 or @Gowtham2003
'''
    context.bot.send_message(chat_id=update.effective_chat.id,text=donate )

def carbon(update,context):
    chat_id = update.effective_chat.id
    try:
        text = update.message.reply_to_message.text
    except AttributeError:
        text = None
    if text:
        context.bot.send_chat_action(chat_id,"upload_photo")
        code_snap = carbonize(text,chat_id)
        if code_snap:
            context.bot.send_photo(chat_id = chat_id,photo=open(code_snap, 'rb'), caption="Carbonized ⚡️\n\nPowered by [Carbon API](https://github.com/cyberboysumanjay/carbon-api)",parse_mode=telegram.ParseMode.MARKDOWN_V2)
            try:
                os.remove(code_snap)
            except FileNotFoundError:
                pass
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,text="Unable to Carbonize the code.\nPlease try again later.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Reply with /carbon on the text you want to Carbonize ⚡️" )

def queryHandler(query):
    commandList = query.replace("/","").split(" ")

    try:
        lang = commandList[1]
        commandList.pop(0)
        commandList.pop(0)
        query = "+".join(commandList)
        return querySh(lang,query)
    except:
        return "__error__"

def query(update,context):
    text = queryHandler(update.message.text) 
    if text=="__error__":
        text = "Cannot Find Any Results : / , \n Check Your Query "
    if len(text) <= 5:
        text = "Cannot Find Any Results : /"

    context.bot.send_message(chat_id=update.effective_chat.id,text=str(text))

# def learnHandler(query):
    # commandList = query.replace("/","").split(" ")
    # lang = commandList[1]
    # return learn(lang)

# def learnCmd(update,context):
    # text = learnHandler(update.message.text) 
    # if len(text) <= 5:
        # text = "Cannot Find Any Results : /"

    # context.bot.send_message(chat_id=update.effective_chat.id,text=str(text))


def main():
    updater = Updater(os.environ.get("BOT_TOKEN", ""), use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler("start",start)
    dp.add_handler(start_handler)

    help_handler = CommandHandler("help",help)
    dp.add_handler(help_handler)

    donate_handler = CommandHandler("donate",donate)
    dp.add_handler(donate_handler)

    donate_handler = CommandHandler("carbon",carbon)
    dp.add_handler(donate_handler)

    donate_handler = CommandHandler("query",query)
    dp.add_handler(donate_handler)

    # donate_handler = CommandHandler("learn",learnCmd)
    # dp.add_handler(donate_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
main()
