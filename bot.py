from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import logging
from telegram.ext import CommandHandler

updater = Updater(token='1295611507:AAHLGyAKby-ilZijQhsEelNYhsT9ELYaZbg', use_context=True)

dispatcher = updater.dispatcher

# Habilitar registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola soy el bot de Oscar R y estoy en prueba")

# Activamos CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)