import telebot 
import serial
import time
from telebot import types
uno = serial.Serial("COM3",19200) #номер порта и скорость работы с ним
bot = telebot.TeleBot('') #токен бота который выдал botfather
@bot.message_handler(commands=['start']) #обработчик команды старт
def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #Кнопки клавиатуры
	item3 = types.KeyboardButton("Включить вентелятор")
	item4 = types.KeyboardButton("Выключить вентелятор")
	item5 = types.KeyboardButton("Температура")
	item6 = types.KeyboardButton("Влажность")
	markup.add(item1, item2, item3, item4,item5,item6)
	bot.send_message(message.chat.id,"Приветствую",reply_markup=markup) #отправить приветственное сообщение и прикрепить клавиатуру

@bot.message_handler(commands=['rename'])
def rename(message):
    bot.send_message(message.chat.id,"Что вы хотите переименовать?")

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Включить свет':
            bot.send_message(message.chat.id,"Уже включаю") #ответ на запрос 
            i = 0
            while i < 25: #отправка 25-ти комманд для 100%-го отклика от ардуино
                i = i + 1
                uno.write(b'1')

        elif message.text == 'Выключить свет':
            bot.send_message(message.chat.id,"Уже выключаю")
            i = 0
            while i < 25:
                i = i + 1
                uno.write(b'2')

        elif message.text == 'Включить вентелятор':
            bot.send_message(message.chat.id,"Уже включаю")
            i = 0
            while i < 25:
                i = i + 1
                uno.write(b'3')

        elif message.text == 'Выключить вентелятор':
            bot.send_message(message.chat.id,"Уже выключаю")
            i = 0
            while i < 25:
                i = i + 1
                uno.write(b'4')

        elif message.text == 'Температура':
            i = 0
            a = 0
            while i < 50 : #50 запросов на получение данных о состоянии датчика влажности и температуры
                i = i + 1
                uno.write(b'5') #отправляем запрос на получение данных
                time.sleep(0.001) #ждем 
                if uno.in_waiting > 0: #если данные получены
                    a = uno.read(size = 2) #записываем 2 байта последних пришедших данных в переменную а
                    print(a) #выводим полученое в консоль
                pass #заканчиваем цикл
            bot.send_message(message.chat.id,"Температура в комнате " + str(int(a)) + "ºC") #отправляем полученые данные в чат 

        elif message.text == 'Влажность' :
            i = 0
            a = 0
            while i < 50 :
                i = i + 1
                uno.write(b'6')
                time.sleep(0.001)
                if uno.in_waiting > 0:
                    a = uno.read(size = 2)
                    print(a)
                pass
            bot.send_message(message.chat.id,"Влажность в комнате " + str(int(a)) + "%")

bot.polling(none_stop=True) #бот работет постоянно
