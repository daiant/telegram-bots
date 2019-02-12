# Imports de telegram #
import telegram
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging

from google_download import download
#### INFO TELEGRAM ####
# Do not share
token = '760276058:AAEnrGP9u0ZJsabq2WeK6sBtinMAq4Fev1M'
# El bot guapo
bot = telegram.Bot(token)
# Herramienta que te da la info del chat.
updater = Updater(token)
# Lo que gestiona la ejecucion de comandos y tal cual.
dispatcher = updater.dispatcher
# Just in case things get wrong.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#################################################


def images(bot,update, args):
	query = ' '.join(args)
	if len(query) == 0:
		return

	bot.send_message(chat_id=update.message.chat_id, text="En ello estoy!!")
	download(query)

def inline_images(bot, update):
	query = update.inline_query.query
	if not query:
		return
	results = list()
	results.append(InlineQueryResultArticle(
		id=query,
		title='Images',
		input_message_content = InputTextMessageContent("En ello estoy!!")))
	bot.answer_inline_query(update.inline_query.id, results)


### HANDLERS ###

# IMAGES #
images_handler = CommandHandler('images', images, pass_args=True)
dispatcher.add_handler(images_handler)

# INLINE_IMAGES #
inline_images_handler = InlineQueryHandler(inline_images)
dispatcher.add_handler(inline_images_handler)


### Let's make a (bot) baby!
updater.start_polling()