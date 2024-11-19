from telebot import TeleBot
from telebot.types import Message

bot = TeleBot(token='6454617316:AAHfZvI7FCOLV8V4wQ9EqBLmlzn_6DXXWhM', parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Привет, как у тебя дела?')


if __name__ == '__main__':
    bot.polling(none_stop=True)
