from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

updater = Updater(token='1295611507:AAHLGyAKby-ilZijQhsEelNYhsT9ELYaZbg')

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola soy el bot de Oscar R y estoy en prueba")