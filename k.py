import pyowm
import telebot
from telebot import apihelper

owm = pyowm.OWM('88a9735342fa3da81a56e0b2277f86ac',language = "ru")
bot = telebot.TeleBot("1246880972:AAE2Qm2nY3JaOpQDYm4C8JLHFb0zs_eFkzA")
apihelper.proxy = {'https':'socks5://89.205.83.56:1080'}


@bot.message_handler(content_types=['text'])
def send_echo(message):
  try:
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    wind = w.get_wind()["speed"]
    humi = w.get_humidity()

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "°C" + "\n"
    answer += "\nСкорость ветра " + str(wind) + "м/с" + "\n"
    answer += "Влажность " + str(humi) + "%" +"\n"
    
    if temp < 1:
      answer += "Бррр" 
    elif temp < 10:
      answer += "Лучше посидеть дома, с чаем и под одеялом"
    elif temp < 20:
      answer += "Одень теплые носки"
    elif temp < 30:
      answer += "Погода отличная, можно гулять"
    else:
      answer += "Идем жарить сосиски, под солнцем"

    bot.send_message(message.chat.id, answer)
  except:
    bot.send_message(message.chat.id,'Ошибка! Город не найден.')
bot.polling( none_stop = True)
input()