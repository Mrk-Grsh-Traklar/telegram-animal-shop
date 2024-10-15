import telebot as tb
from telebot import types

Token = '7175732877:AAGKjHDw4DeTu5cfFeZIHCCRug2wxVAqcHM'
bot = tb.TeleBot(Token)

print('started')
# главное меню
@bot.message_handler(commands=['main, start'])
@bot.message_handler(regexp='start')
@bot.message_handler(regexp='main')
def mein_menu(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    profile = types.KeyboardButton('profile')
    help = types.KeyboardButton('help')
    support = types.KeyboardButton('support')
    donate = types.KeyboardButton('donate')
    markup.add(profile, help, support,donate)
    bot.send_message(message.chat.id, f"Hello! {message.from_user.first_name}", reply_markup=markup)

# тех.поддержка
@bot.message_handler(regexp='support')
def support(message):
    bot.send_message(message.chat.id, f"Hello! if you encounter difficulties contact technical support \n @assmaser")







bot.infinity_polling()