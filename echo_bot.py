#!/usr/bin/env python3

import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN", parse_mode=None)

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
        bot.send_message(message.chat.id, "Menu:", reply_markup=markup)
    elif message.text == "Y":
        markup = types.ReplyKeyboardRemove(selective=False)
        markup = types.InlineKeyboardMarkup(row_width=1)
        itembtm1 = types.InlineKeyboardButton('Правила', callback_data='inc_1')
        itembtm2 = types.InlineKeyboardButton('Пользовательское соглашение', callback_data='inc_2')
        itembtm3 = types.InlineKeyboardButton('Пополнение баланса', callback_data='inc_3')
        markup.add(itembtm1, itembtm2, itembtm3)
        bot.send_message(message.chat.id, "Меню:", reply_markup=markup)
    elif message.text == "Правила":
        bot.send_message(message.chat.id, "Мы тут не в игры играем, никаких правил")
    elif message.text == "Пользовательское соглашение":
        bot.send_message(message.chat.id, "Можем просто заблокировать, если ты нам не понравишься")
    elif message.text == "Пополнение баланса":
        bot.send_message(message.chat.id, "$9000000000000")
    else:
        bot.reply_to(message, message.text)
        bot.send_message(message.chat.id, "You lose")

@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.message:
        if call.data == "inc_1":
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Ага', callback_data='inc_0')
            item2 = types.InlineKeyboardButton('Отправить отзыв', callback_data='la_2')
            markup.add(item1, item2)
            bot.edit_message_text("Мы тут не в игры играем, никаких правил", call.message.chat.id, call.message.message_id, reply_markup=markup)
        elif call.data == "inc_2":
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_for_block_1 = types.InlineKeyboardButton('Ага', callback_data='inc_0')
            item_for_block_2 = types.InlineKeyboardButton('Угу', callback_data='item_block_2')
            markup.add(item_for_block_1, item_for_block_2)
            bot.edit_message_text("Можем просто заблокировать, если ты нам не понравишься", call.message.chat.id, call.message.message_id, reply_markup=markup)
        elif call.data == "inc_3":
            bot.send_message(call.message.chat.id, "$9000000000000")
        elif call.data == "inc_0":
            markup = types.InlineKeyboardMarkup(row_width=1)
            itembtm1 = types.InlineKeyboardButton('Правила', callback_data='inc_1')
            itembtm2 = types.InlineKeyboardButton('Пользовательское соглашение', callback_data='inc_2')
            itembtm3 = types.InlineKeyboardButton('Пополнение баланса', callback_data='inc_3')
            markup.add(itembtm1, itembtm2, itembtm3)
            bot.edit_message_text("Меню:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    
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
