import wikipedia
print("What language do you want to use? Type /languages to see all permissions" )
Z = input()
Answers = ("yes", 'Yes', 'YES','Y', 'y', 'да', 'д', 'Д', 'ДА', 'Да' 'ja', 'JA', 'Oui', 'oui',
				 '是的','oo', 'Oo', 'sí', 'tak', 'あり', "Si", 'si', 'Vâng', 'vâng', 'Ja')
lang = dict()
def summary():
	global Z
	global Answers
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
	print(txt[0], '')
	N = input()
	tmp = wikipedia.page(N)
	print(tmp.title)
	print(txt[1], '')
	ans = input()
	if ans in Answers:
		print(wikipedia.summary(N))
		print(tmp.url)
	elif ans == "Exit" or "exit":
		break()
	else:
		print(txt[2], '') 
		summary()
summary()