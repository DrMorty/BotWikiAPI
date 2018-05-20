# -*- coding: utf-8 -*-
import config
import telebot
import wikipedia
import requests	
import time 
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start']) #
def handle_start(message):
	bot.reply_to(message, "What language do you want to use? Type /help to see all permissions")
@bot.message_handler(commands=['help'])
def handle_help(message):
	bot.reply_to(message, "English(en), Russian(ru), Japanese(ja), Cebuano(ceb), Swedish(sv), German(de),French(Fr), Dutch(nl),Italian(it), Spanish(es),Polish(pl), Vietnamese(vi), Bashkir(ba)")


@bot.message_handler(content_types=["text"])
def read_language(message):
	Z = message.text
	wikipedia.set_lang(Z)
	if Z == "en" or Z == "En":
		txt = [ "What do you want to find?", "Is this name correct? Y/N", "Make another request"]
	if Z == "ru" or Z == "RU":
		txt = ["Что вы хотите найти?", "Правильно ли введено название? Д/Н",
				"Повторите ваш запрос"]
	if Z == "ja" or Z ==  "JA":
		txt = ["何を探したいのか？", "この名前の正しいのか？ あり/いいえ", "別のリクエストをする"]
	if Z == "ceb" or Z ==  "CEB":
		txt =  ["Unsay gusto nimo pangitaon?", "Husto ba kining ngalana? oo / dili", "Paghimo'g laing hangyo"]
	if Z == "sv" or Z ==  "SV":
		txt = ["Vad vill du hitta?", "Är detta namn korrekt? Ja / Nej", "Gör en annan förfrågan"]
	if Z == "de" or Z ==  "DE":
		txt = ["Was willst du finden?", "Ist dieser Name richtig? Ja/ Nein", "Eine andere Anfrage machen"]
	if Z == "it" or Z ==  "IT":
		txt = ["Cosa vuoi trovare?", "Il nome è corretto? Si / No", "Fai un'altra richiesta"]
	if Z == "es" or Z ==  "ES":
		txt = ["¿Qué quieres encontrar?", "¿Es correcto este nombre? Si / No", "Haz otra solicitud"]
	if Z == "pl" or Z ==  "PL":
		txt = ["Co chcesz znaleźć?", "Czy to jest poprawne imię? Tak / Nie", "Zrób kolejną prośbę"]
	if Z == "vi" or Z ==  "VI":
		txt = [ "Bạn muốn tìm gì?", "Đây có phải là tên đúng không? Vâng/ Không", "Thực hiện một yêu cầu khác"]
	if Z == "ba" or Z ==  "BA":
		txt = ["Тел табаһығыҙ һеҙ?", "Был исем дөрөҫ? Д/юҡ"	, "тағы бер запрос яһаныҡ"]
	if Z == "fr" or Z ==  "FR":
		txt = ["Que voulez-vous trouver?", "Ce nom est-il correct? Oui/Non", "Faire une autre demande"]

	bot.send_message(message.chat.id, txt[0],'')
@bot.message_handler(content_types=["text"])
def check_name(message):
	N = message.text
	tmp = wikipedia.page(N)
	bot.send_message(message.chat.id, tmp.title)
	bot.send_message(message.chat.id, txt[1], '')

@bot.message_handler(content_types=["text"])
def result(message):
	ans = message.text
	Answers = ("yes", 'Yes', 'YES','Y', 'y', 'да', 'д', 'Д', 'ДА', 'Да' 'ja', 'JA', 'Oui', 'oui',
				 '是的','oo', 'Oo', 'sí', 'tak', 'あり', "Si", 'si', 'Vâng', 'vâng', 'Ja')
	if ans in Answers:
		bot.send_message(message.chat.id, wikipedia.summary(N))
		bot.send_message(message.chat.id,tmp.url)
	elif ans == "Exit" or ans == "exit":
		bot.send_message(message.chat.id, "Goodbye!")
	else:
		bot.send_message(message.chat.id, txt[2], '')

while True:
	try:
		bot.polling(none_stop=True)
	except requests.exceptions.ConnectionError as e:
		time.sleep(15)