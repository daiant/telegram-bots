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

def echo(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
	text_to_caps = ' '.join(args).upper()
	if len(text_to_caps) == 0:
		bot.send_message(chat_id=update.message.chat_id, text="Que no has escrito nada, tú.")
		return
	bot.send_message(chat_id=update.message.chat_id, text=text_to_caps)

def inline_caps(bot, update):
	query = update.inline_query.query
	if not query:
		return
	results = list()
	results.append(
		InlineQueryResultArticle(
			id = query.upper(),
			title = 'Caps',
			input_message_content = InputTextMessageContent(query.upper())
		)
	)
	bot.answer_inline_query(update.inline_query.id, results)

def unsplash(bot, update, args):
	query = ' '.join(args)
	if(len(query)) == 0:
		return
	res = search_photos(query)
	if res == "EMPTY":
		text = "Esto no va!!"
		return	
	bot.send_message(chat_id=update.message.chat_id, text = "https://unsplash.com/photos/"+res)

def unknown(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Yo aún no sé hacer esas cosas.")

### HANDLERS ###

# Gestión del comando /start.
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

# Gestion del echo
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

# Gestión de caps
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

# Gestión de inline_caps
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# Gestión de comando /unsplash
unsplash_handler = CommandHandler('unsplash', unsplash, pass_args=True)
dispatcher.add_handler(unsplash_handler)

# Gestión de comandos desconocidos.
### Siempre último ###
unknown_handler=MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


### Let's make a (bot) baby!
updater.start_polling()