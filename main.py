from telebot import TeleBot
from telebot.types import Message

bot = TeleBot(token='UR_TOKEN', parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Привет, как у тебя дела?')


if __name__ == '__main__':
    bot.polling(none_stop=True)
