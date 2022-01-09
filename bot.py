import telebot
from config import token
from AdvicesArray import Advices
import sqlite3
import schedule
import time
import threading

table = sqlite3.connect("users.db") #Connecting table
cursor = table.cursor()

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Пришло время рассказать тебе секрет 🤫 Если ты выспался, то у тебя будет много сил в течение дня: тебе легко быть продуктивным в течение всего дня, лёгко учиться, ты спокоен в любой ситуации. А вот если не выспался... Пиши пропало: всё идёт из рук вон плохо, ничего не понимаешь, злишься из-за любого пустяка 🤬")
  bot.send_message(message.chat.id,"Я помогу тебе как можно чаще высыпаться, чтобы улучшить качество твоей жизни 😇")
  table1 = sqlite3.connect("users.db")
  cursor1 = table1.cursor()
  cursor1.execute(f"insert into users values({message.chat.id},0)")
  table1.commit()

def advice():
    table2 = sqlite3.connect("users.db")
    cursor2 = table2.cursor()
    cursor2.execute("select * from users")
    users = cursor2.fetchall()
    for i in users:
        id = i[0]
        day = i[1]
        bot.send_message(id, f"*Совет №{day}*\n\n{Advices[day]}", parse_mode="MARKDOWN")
        cursor2.execute("update users set day = day + 1")
        table2.commit()

schedule.every(2).seconds.do(advice)

def threadFunction():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=threadFunction).start()

bot.infinity_polling() # Запуск бота
