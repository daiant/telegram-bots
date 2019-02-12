import telegram
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from doggos import search_photos
import logging

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


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Soy penelio y estoy ready para ti.")

def unsplash(bot, update, args):
	query = ' '.join(args)
	if(len(query)) == 0:
		return
	res = search_photos(query)
	if res == "EMPTY":
		text = "Esto no va!!"
		return	
	bot.send_message(chat_id=update.message.chat_id, text = "https://unsplash.com/photos/"+res)

def inline_unsplash(bot, update):
	query = update.inline_query.query
	if not query:
		return
	results = list()
	results.append(
		InlineQueryResultArticle(
			id = title,
			query = 'Unsplash Photos',
			input_message_content = InputTextMessageContent("https://unsplash.com/photos/"+search_photos(query))
		)
	)
	bot.answer_inline_query(update.inline_query.id, results)

def unknown(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Yo aún no sé hacer esas cosas.")


### HANDLERS ###

# Gestión del comando /start.
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

# Gestión de comando /unsplash
unsplash_handler = CommandHandler('unsplash', unsplash, pass_args=True)
dispatcher.add_handler(unsplash_handler)

# Gestión de inline_unsplash
inline_unsplash_handler = InlineQueryHandler(inline_unsplash)
dispatcher.add_handler(inline_unsplash_handler)

# Gestión de comandos desconocidos.
### Siempre último ###
unknown_handler=MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


### Let's make a (bot) baby!
updater.start_polling()