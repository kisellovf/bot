import telebot
import random 
from glob import glob
from random import choice
from telebot import types
bot = telebot.TeleBot('1242295502:AAF90d8D30052YUXySiHYkFRtOmSnD7qP5c')
@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    

    sti = open('content/5.png', 'rb')
    bot.send_sticker(message.chat.id, sti)
    
    keyborad = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mem = types.KeyboardButton('Пришли мем')
    num = types.KeyboardButton('Рандомное число')
    music = types.KeyboardButton('Музыка')


    keyborad.add(mem, num, music, )
    bot.send_message(message.chat.id, 'Привет {0.first_name}!\nЯ бот {1.first_name}, созданый для того чтобы тебе не было скучно!'.format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=keyborad)

@bot.message_handler(regexp='Как дела')
def frendly(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Нормально', callback_data=  'good')
    button2 = types.InlineKeyboardButton(text='Не очень', callback_data = 'bad')
    markup.add(button1, button2)

    bot.send_message(message.chat.id,'Нормально\n.А у тебя как?',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def reaction_on_quests(call):
    try:
        if call.message:
            if call.data == 'bad':
                sti = open('content/sticker.webp', 'rb')
                bot.send_sticker(call.message.chat.id,sti )
                bot.send_message(call.message.chat.id, 'Печально, я сочуствую 😢')
            elif call.data == 'good':
                sti = open('content/AnimatedSticker.tgs', 'rb')
                bot.send_sticker(call.message.chat.id,sti )
                bot.send_message(call.message.chat.id, 'Вот и хорошо😄😄😄')

    except Exception as e:
        print(repr(e))
@bot.message_handler(content_types=['text'])
def send_meme(message):
    if message.chat.type == "private":
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))

        elif message.text == 'Пришли мем':
            list = glob('meme/*')
            meme = choice(list)
            bot.send_photo(message.chat.id, photo = open(meme, 'rb'))

        elif message.text == 'Музыка':
            list = glob('music/*')
            music = choice(list)
            bot.send_audio(message.chat.id, audio = open(music, 'rb'))


        else:
            bot.send_message(message.chat.id, 'Я не зная что ответить 😢😢😢')


bot.polling()