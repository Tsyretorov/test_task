import logging
import datetime

from telegram.ext import ApplicationBuilder, Updater, CallbackQueryHandler, MessageHandler, CommandHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update, WebAppInfo


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update, context):

    inline_main = InlineKeyboardMarkup([
        [InlineKeyboardButton("тык", web_app=WebAppInfo("https://tsyretorov.github.io/"))],])

    await context.bot.send_message(update.message.chat.id, "test", reply_markup=inline_main)
def main():
    app = ApplicationBuilder().token("ТОКЕН").build()

    app.add_handler(CommandHandler('start', start))

    app.run_polling()
    app.idle()

if __name__ == "__main__":
    main ()
