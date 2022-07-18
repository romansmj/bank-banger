import telebot
from telebot import types
TOKEN = '5370408271:AAEXGaVJZv1khYOGGm9xnCmaD5YSwdlU4GM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) # handle '/start' message when user starts Bank Banger bot

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True) # 'markup' is a keyboard
    # buttons:
    item1 = types.KeyboardButton('🚀Услуги')
    item2 = types.KeyboardButton('📞Контакты')
    item3 = types.KeyboardButton('💲Цены')
    item4 = types.KeyboardButton('👩Позови оператора')
    # add buttons to markup:
    markup.add(item1, item2, item3, item4)
    # welcome message:
    bot.send_message(message.chat.id, 'Привет👋 Чем могу помочь?', reply_markup = markup)

@bot.message_handler(content_types=['text']) # handle every text information from user

def send_message(message): # responses
    if message.chat.type == 'private':
        if message.text == '🚀Услуги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🤷Банкротство физ. лиц')
            item2 = types.KeyboardButton('🏪Банкротство юр. лиц')
            back = types.KeyboardButton('↩ В главное меню')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Услуги', reply_markup = markup)

        elif message.text == '📞Контакты':
            bot.send_message(message.chat.id, 'Наш телефон: +7(800)5553535\nНаш адрес: Москва, ул. Пушкина, д. Колотушкина с.1')

        elif message.text == '💲Цены':
            bot.send_message(message.chat.id, 'Цены')

        elif message.text == '👩Позови оператора':
            bot.send_message(message.chat.id, 'Соединяю с оператором...')

        elif message.text == '↩ В главное меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True) 
            item1 = types.KeyboardButton('🚀Услуги')
            item2 = types.KeyboardButton('📞Контакты')
            item3 = types.KeyboardButton('💲Цены')
            item4 = types.KeyboardButton('👩Позови оператора')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Чем ещё могу помочь?', reply_markup = markup)

bot.polling(none_stop = True) # entry point. 'none_stop' keeps bot online