import sys
import re
import urllib.parse
import requests
import bs4

args = sys.argv
gender = "m"

if len(args) >= 2:
	gender = args[1]

if gender != "m" and gender != "f":
	sys.exit()

def getcolor(colorname):
	colors = {
		'red': '\033[31m',
		'green': '\033[32m',
		'yellow': '\033[33m',
		'blue': '\033[34m',
		}
	def func2(c):
		return print(colors[colorname] + c + '\033[0m')

	return func2

red    = getcolor('red')
green  = getcolor('green')
yellow = getcolor('yellow')
blue   = getcolor('blue')

last_name = "金子"
param = urllib.parse.quote(last_name)
base_url = "https://enamae.net/" + gender + "/" + param + "__"
boy_txt = "boy.txt"
girl_txt = "girl.txt"

name_txt = boy_txt
name_suffix = 'くん'
if gender == 'f':
	name_txt = girl_txt
	name_suffix = 'ちゃん'

with open(name_txt, "r") as fin:
	for first_name in fin:
		first_name = first_name.strip()
		url = base_url + urllib.parse.quote(first_name)

		r = requests.get(url)
		soup = bs4.BeautifulSoup(r.text, 'html.parser')

		print(first_name + name_suffix)
		tags = soup.find_all('h3')

		disp = True
		index = 1
		for tag in tags:
			if index > 7:
				break

			if tag.text.find('凶') > -1:
				disp = False

		if disp == False:
			continue

		index = 1
		for tag in tags:
			if index > 7:
				break 
			if tag.text.find('吉凶混合') > -1:
				green(tag.text)
			elif tag.text.find('特殊格') > -1:
				print(tag.text)
			elif tag.text.find('大吉') > -1:
				red(tag.text)
			elif tag.text.find('吉') > -1:
				yellow(tag.text)
			elif tag.text.find('凶') > -1:
				blue(tag.text)

			if index == 7:
				print(tag.text)
				yinyang = soup.find("p", text=re.compile("陰陽配列は"))
				if yinyang is not None:
					print(yinyang.text)
				print()
			index+=1