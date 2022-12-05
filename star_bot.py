#!/usr/bin/env python3

import telebot
from telebot import types
import sqlite3

sqll = [0]

bot = telebot.TeleBot("1774678528:AAGJO1yuK9SyDxDfJSbujLcnTxmGhXaGyyI", parse_mode=None)

conn = sqlite3.connect('SQLdb.db', check_same_thread=False)
cursor = conn.cursor()

def updateUserBalance (id: int, balans: int):
    cursor.execute('UPDATE users SET balans=? WHERE id=?', (balans, id))
    conn.commit()

def createUser (id: int, user_name: str, user_login: str, balans: int):
    cursor.execute('INSERT INTO users (id, user_name, user_login, balans) VALUES (?, ?, ?, ?)', (id, user_name, user_login, balans))
    conn.commit()

def getUserBalans (id: int):
    balans = cursor.execute('SELECT balans FROM users WHERE id = ?', (id,))
    conn.commit()
    return balans.fetchone()[0]

def getUserName (id: int):
    userData = cursor.execute('SELECT user_name FROM users WHERE id = ?', (id,))
    conn.commit()
    return userData.fetchone()[0]

def selectAll_id ():
    all_id = cursor.execute('SELECT id FROM users')
    conn.commit()
    return all_id.fetchall()

def idINFOMRER (ID):        # вытаскиваем список ID-шников из картежа sqlite
    allin = selectAll_id()
    print(allin)
    num = 0   
    # usId = call.from_user.id
    print(ID, '- user')
    new_base = []
    for el in allin:
        print(num)
        print(ID, allin[num][0])
        new_base.insert(num, allin[num][0])
        num = num+1
        print(new_base)
        print('==========================================')
    return new_base

def select_all_base ():
    all_base = cursor.execute('SELECT * FROM users')
    conn.commit()
    return all_base.fetchall()

    

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Этот бот призван читать круче Кендрика Ламара.")
    stick = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)
    markup = types.ReplyKeyboardRemove(selective=False)
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtm1 = types.InlineKeyboardButton('Правила', callback_data='inc_1')
    itembtm2 = types.InlineKeyboardButton('Пользовательское соглашение', callback_data='inc_2')
    itembtm3 = types.InlineKeyboardButton('Пополнение баланса', callback_data='inc_3')
    itembtm4 = types.InlineKeyboardButton('Личный кабинет', callback_data='inc_4')
    markup.add(itembtm1, itembtm2, itembtm3, itembtm4)
    bot.send_message(message.chat.id, "Меню:", reply_markup=markup)

"""--------------------------- Обработчик кнопок -----------------------------------------------------------"""
@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.message:
        if call.data == "inc_0":
            markup = types.InlineKeyboardMarkup(row_width=1)
            itembtm1 = types.InlineKeyboardButton('Правила', callback_data='inc_1')
            itembtm2 = types.InlineKeyboardButton('Пользовательское соглашение', callback_data='inc_2')
            itembtm3 = types.InlineKeyboardButton('Пополнение баланса', callback_data='inc_3')
            itembtm4 = types.InlineKeyboardButton('Личный кабинет', callback_data='inc_4')
            markup.add(itembtm1, itembtm2, itembtm3, itembtm4)
            bot.edit_message_text("Меню:", call.message.chat.id, call.message.message_id, reply_markup=markup)


        elif call.data == "inc_1":
            user_ID = call.from_user.id
            if user_ID in idINFOMRER(user_ID):
                print('Hello, friend')
            else:
                us_id = call.from_user.id
                us_name = call.from_user.first_name
                us_sname = call.from_user.username
                createUser(id=us_id, user_name=us_name, user_login=us_sname, balans=0)
                print('new user') 
                # bot.send_message(call.from_user.id, 'Привет! Ваше имя добавленно в базу данных!')            

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Отправить отзыв', callback_data='la_2')
            item2 = types.InlineKeyboardButton('Назад', callback_data='inc_0')
            markup.add(item1, item2)
            bot.edit_message_text("Мы тут не в игры играем, никаких правил", call.message.chat.id, call.message.message_id, reply_markup=markup)

        elif call.data == "inc_2":
            user_ID = call.from_user.id
            if user_ID in idINFOMRER(user_ID):
                print('Hello, friend')
            else:
                us_id = call.from_user.id
                us_name = call.from_user.first_name
                us_sname = call.from_user.username
                createUser(id=us_id, user_name=us_name, user_login=us_sname, balans=0)
                print('new user')
                # bot.send_message(call.from_user.id, 'Привет! Ваше имя добавленно в базу данных!') 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_for_block_1 = types.InlineKeyboardButton('Инверсировать игру', callback_data='item_block_2')
            item_for_block_2 = types.InlineKeyboardButton('Назад', callback_data='inc_0')
            markup.add(item_for_block_1, item_for_block_2)
            bot.edit_message_text("Можем просто заблокировать, если ты нам не понравишься", call.message.chat.id, call.message.message_id, reply_markup=markup)

        elif call.data == "inc_3":
            user_ID = call.from_user.id
            if user_ID in idINFOMRER(user_ID):

                print('Hello, friend')
            else:
                us_id = call.from_user.id
                us_name = call.from_user.first_name
                us_sname = call.from_user.username
                createUser(id=us_id, user_name=us_name, user_login=us_sname, balans=0)
                # bot.send_message(call.from_user.id, 'Привет! Ваше имя добавленно в базу данных!')
                print('new user')

            us_id = call.from_user.id
            us_name = call.from_user.first_name
            us_sname = call.from_user.username
            currentUserBalance = getUserBalans(us_id)
            # print(currentUserBalance.fetchone()[0])
            currentUserBalance = currentUserBalance+100
            updateUserBalance(id=us_id, balans=currentUserBalance)
            markup = types.InlineKeyboardMarkup(row_width=1)
            balansbtn = types.InlineKeyboardButton('Назад', callback_data='inc_0')
            markup.add(balansbtn)
            bot.edit_message_text("Баланс пополнен!", call.message.chat.id, call.message.message_id, reply_markup=markup)

        elif call.data == "inc_4":
            user_ID = call.from_user.id
            if user_ID in idINFOMRER(user_ID):
                print('Hello, friend')
            else:
                us_id = call.from_user.id
                us_name = call.from_user.first_name
                us_sname = call.from_user.username
                createUser(id=us_id, user_name=us_name, user_login=us_sname, balans=0)
                print('new user')
                # bot.send_message(call.from_user.id, 'Привет! Ваше имя добавленно в базу данных!')
            if user_ID == 795675764 or user_ID == 5510951877:
                markup = types.InlineKeyboardMarkup(row_width=1)
                lkbtn1 = types.InlineKeyboardButton('Назад', callback_data='inc_0')
                lkbtn2 = types.InlineKeyboardButton('База данных', callback_data='admin_base')
                markup.add(lkbtn1, lkbtn2)
                us_id = call.from_user.id
                bot.edit_message_text('Привет, создатель!\n'+'Игрок: '+str(getUserName(us_id))+'\nБаланс: '+str(getUserBalans(us_id)), 
                    call.message.chat.id, call.message.message_id, reply_markup=markup)
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                lkbtn1 = types.InlineKeyboardButton('Назад', callback_data='inc_0')
                markup.add(lkbtn1)
                us_id = call.from_user.id
                bot.edit_message_text('Игрок: '+str(getUserName(us_id))+'\nБаланс: '+str(getUserBalans(us_id)), 
                    call.message.chat.id, call.message.message_id, reply_markup=markup)

        elif call.data == "la_2":
            markup = types.InlineKeyboardMarkup(row_width=1)
            otzyv = types.InlineKeyboardButton('Назад', callback_data='inc_0')
            markup.add(otzyv)
            bot.edit_message_text("info@xcloudclub.com", call.message.chat.id, call.message.message_id, reply_markup=markup)

        elif call.data == 'item_block_2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            inv_1 = types.InlineKeyboardButton('Назад', callback_data='inc_0')
            markup.add(inv_1)
            bot.edit_message_text("Инверсированно", call.message.chat.id, call.message.message_id, reply_markup=markup)

        elif call.data == 'admin_base':
            my_list = []
            for x in select_all_base():
                my_list.append(''.join(str(x)))    #https://ru.stackoverflow.com/questions/1178388
            my_str = '\n'.join(my_list)
            # print(select_all_base())
            # for item in select_all_base():
            #     print(item)
            markup = types.InlineKeyboardMarkup(row_width=1)
            button_back = types.InlineKeyboardButton('Назад', callback_data='inc_0')
            markup.add(button_back)
            bot.edit_message_text('База данных\n'+my_str, call.message.chat.id, call.message.message_id, reply_markup=markup)


"""------------------------- Обработчики текста и стикеров --------------------------------------------------"""
@bot.message_handler(content_types=['text'])
def text_up(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, "Давай без самодеятельности. Мы для кого кнопки сделали?")

@bot.message_handler(content_types=['sticker'])
def text_down(message):
    bot.send_message(message.chat.id, "Козырный стикер!")

"""--------------------------------- Start ------------------------------------------------------------------"""
bot.infinity_polling()
