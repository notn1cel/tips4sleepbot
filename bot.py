import telebot
from config import token

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Пришло время рассказать тебе секрет 🤫 Если ты выспался, то у тебя будет много сил в течение дня: тебе легко быть продуктивным в течение всего дня, лёгко учиться, ты спокоен в любой ситуации. А вот если не выспался... Пиши пропало: всё идёт из рук вон плохо, ничего не понимаешь, злишься из-за любого пустяка 🤬")
  bot.send_message(message.chat.id,"Я помогу тебе как можно чаще высыпаться, чтобы улучшить качество твоей жизни 😇")

@bot.message_handler(commands=['help'])
  bot.send_message(message.chat.id,"")

@bot.message_handler(content_types = ["text"] )
def howareu_message(message):
	if message.text == 'Как дела?':
		bot.send_message(message.chat.id,"Средненько, а у тебя")
	elif message.text == 'Как жизнь?':
		bot.send_message(message.chat.id,"Отлично оу воу воу")

bot.infinity_polling() # Запуск бота
