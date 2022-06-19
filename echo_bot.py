#!/usr/bin/env python3

import telebot
from telebot import types

bot = telebot.TeleBot("5102469357:AAHmLJWIIvpQDVmG5PIbJb94k13Om9owOpg", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Этот бот призван читать круче Кендрика Ламара.")
    stick = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)

@bot.message_handler(content_types=['text'])
def text_up(message):
    if message.text == "Z":
        bot.reply_to(message, "Хуя ты")
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('Правила')
        itembtn2 = types.KeyboardButton('Пользовательское соглашение')
        itembtn3 = types.KeyboardButton('Пополнение баланса')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    elif message.text == "Правила":
        bot.send_message(message.chat.id, "Мы тут не в игры играем, никаких правил")
    elif message.text == "Пользовательское соглашение":
        bot.send_message(message.chat.id, "Можем просто заблокировать, если ты нам не понравишься")
    elif message.text == "Пополнение баланса":
        bot.send_message(message.chat.id, "$9000000000000")
    else:
        bot.reply_to(message, message.text)
        bot.send_message(message.chat.id, "You lose")
    
@bot.message_handler(content_types=['sticker'])
def text_down(message):
    bot.send_message(message.chat.id, "You win")

bot.infinity_polling()


'''
@bot.message_handler(func=lambda m: True)
def answer(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, "You lose")      
'''
