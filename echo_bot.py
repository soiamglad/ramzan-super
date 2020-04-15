import pyowm
import telebot
from telebot import apihelper

owm = pyowm.OWM('88a9735342fa3da81a56e0b2277f86ac',language = "ru")
bot = telebot.TeleBot("1246880972:AAE2Qm2nY3JaOpQDYm4C8JLHFb0zs_eFkzA")
apihelper.proxy = {'https':'socks5://173.244.200.156:10444'}


@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(place)
    w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
    wind = w.get_wind()["speed"]

    answer = "В городе " + place + " сейчас " + w.get_detailed_status() + "\n"
	answer = "Температура сейчас в районе " + str(temp) + "°C" + "\n"
	answer = "Ветер сейчас в районе " + str(wind) + "м/с" + "\n\n"
	
	if temp <10:
	    print( "Лучше посидеть дома, с чаем и под одеялом" )
	elif temp <20:
	    print( "Одень теплые носки") 
	elif temp <30:
	    print( "Погода отличная, можно гулять")
	else:
	    print( "Идем жарить сосиски, под солнцем")
	    
bot.polling( none_stop = True )
