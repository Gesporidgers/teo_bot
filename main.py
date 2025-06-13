import telebot
from telebot import types
from telebot import formatting
from FUN import *

bot = telebot.TeleBot('7678445926:AAFJHrBTmUvYh9RxCXjSIEmN4ODSqIb_muQ')
markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Рассчитать Slope')
btn2 = types.KeyboardButton('Ссылка на simbrief')
btn3 = types.KeyboardButton('Сделать пароль')
btn4 = types.KeyboardButton('Расшифровать символику Кендалла')
markup_main.add(btn1,btn2,btn3,btn4)
current_mode = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,'Привет',reply_markup=markup_main)
    global current_mode
    current_mode = 0

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global current_mode
    markup_sub = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    markup_sub.add(back)
    if current_mode == 0:
        if message.text == 'Рассчитать Slope':
            current_mode = 1
            bot.send_message(message.from_user.id,'Отправьте в формате: превышение_у_торца превышение_на_противоположном торце длина_впп',reply_markup=markup_sub)
        elif message.text == 'Ссылка на simbrief':
            current_mode = 2
            bot.send_message(message.from_user.id,'Отправьте в формате: аэропорт_отправления аэропорт_назначения',reply_markup=markup_sub)
        elif message.text == 'Сделать пароль':
            bot.send_message(message.from_user.id,'Отправьте что нужно зашифровать',reply_markup=markup_sub)
            current_mode = 3
        elif message.text == 'Расшифровать символику Кендалла':
            bot.send_message(message.from_user.id, 'Отправьте характеристики СМО', reply_markup=markup_sub)
            current_mode = 4
        elif message.text == 'Назад':
            current_mode = 0
            bot.send_message(message.from_user.id,'Привет',reply_markup=markup_main)
    elif current_mode == 1:
        args = message.text.split()
        bot.send_message(message.from_user.id,RwySlope(int(args[0]), int(args[1]),int(args[2])),reply_markup=markup_main)
        current_mode = 0
    elif current_mode == 2:
        args = message.text.split()
        bot.send_message(message.from_user.id,FlightLink(args[0],args[1]),reply_markup=markup_main)
        current_mode = 0
    elif current_mode == 3:
        bot.send_message(message.from_user.id,'`'+Encryption(message.text)+'`',reply_markup=markup_main,parse_mode='MARKDOWN')
        current_mode = 0
    elif current_mode == 4:
        bot.send_message(message.from_user.id, Kendall(str(message.text)), reply_markup=markup_main,parse_mode='MARKDOWN')
        current_mode = 0

bot.polling(non_stop=True,interval=0)