from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Start command function (async required)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi, I’m alive!")

# Create the bot app
app = Application.builder().token("8004438645:AAHpRbSxrEk6Qf0MazH5EJn63EgJcEsoWjY").build()

# Register the /start command
app.add_handler(CommandHandler("start", start))

# Start the bot
app.run_polling()
