import telebot

bot = telebot.TeleBot('6343220717:AAFwAAD-s2nmRnrVFPUiwRK40RdvW2Lbt1g')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)