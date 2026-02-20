import telebot
from tgToken import tgToken

bot = telebot.TeleBot(tgToken)

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id,"hello")

bot.polling(non_stop=True)