from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8004438645:AAHpRbSxrEk6Qf0MazH5EJn63EgJcEsoWjY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Welcome to Hi5 Premium Tips!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
