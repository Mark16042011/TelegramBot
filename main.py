from telebot import TeleBot
from telebot.apihelper import send_message
from telebot.types import Message

bot = TeleBot(token='7625687779:AAHdzebhwJR6x9eT5bohG8MPuLgEyXTtQhE')

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Приветь)😜😙😙 Как тебя зовут?)🤔🥺🥺")
    bot.register_next_step_handler(message, what_is_ur_surname)

def what_is_ur_surname(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Ой какое имя красивое))😍😇 А фамилия какая у тебя?🥺")
    bot.register_next_step_handler(message, ur_adress)

def ur_adress(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Ясненько🥰)) А где ты живешь?🧐")
    bot.register_next_step_handler(message, ur_age)

def ur_age(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Ого!🤩 А сколько тебе лет..?")
    bot.register_next_step_handler(message, povestka)

def povestka(message: Message):
    if message.text >=f"{18}":
        bot.send_message(chat_id=message.chat.id, text="Оооооо братик ну ты попал~ Лови повестку!")
        bot.send_photo(chat_id=message.chat.id,photo="https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Favatars.dzeninfra.ru%2Fget-zen_doc%2F271828%2Fpub_65618a0988410d6f4aa2873e_65618b73654b6f493a9b1b92%2Fscale_1200&lr=2&pos=2&rpt=simage&text=%D0%BF%D0%BE%D0%B2%D0%B5%D1%81%D1%82%D0%BA%D0%B0")
    else:
        bot.send_message(chat_id=message.chat.id, text="База, разходимся, он не совершеннолетний...")

if __name__ == '__main__':
    bot.polling(none_stop=True)