import telebot

bot = telebot.TeleBot('6343220717:AAFwAAD-s2nmRnrVFPUiwRK40RdvW2Lbt1g')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID:{message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('mona.jpeg','rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop=True)


# 18:00