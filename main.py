from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ['BOT_TOKEN']

def start(update, context):
    update.message.reply_text('Hello! Welcome to Hi5 Premium Tips.')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
