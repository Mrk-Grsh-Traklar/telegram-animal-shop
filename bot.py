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
    support = types.KeyboardButton('support')
    buy = types.KeyboardButton('buy')
    markup.add(profile, support, buy )
    bot.send_message(message.chat.id, f"Hello! {message.from_user.first_name}", reply_markup=markup)

# тех.поддержка
@bot.message_handler(regexp='support')
def support(message):
    bot.send_message(message.chat.id, f"Hello! if you encounter difficulties contact technical support \n @assmaser")

# открытие листа покупок 
# 1) выбор животного
# 2) выбор категории товара
# 3) выбор товара
@bot.message_handler(regexp='buy')
def animal(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    cat = types.KeyboardButton('cat')
    dog = types.KeyboardButton('dog')
    chinchilla = types.KeyboardButton('chinchilla')
    parrot = types.KeyboardButton('parrot')
    snake = types.KeyboardButton('snake')
    lizard =  types.KeyboardButton('lizard')
    main = types.KeyboardButton('main')
    markup.add(cat,dog,chinchilla,parrot,snake,lizard,main)
    bot.send_message(message.chat.id, f'select animal category:', reply_markup=markup)

# катигории товара
@bot.message_handler(regexp='product_category')
def product_category(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add()    





bot.infinity_polling()