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
		index = 1
		for tag in tags:
			if index > 7:
				break 
			print(tag.text)
			if index == 7:
				yinyang = soup.find("p", text=re.compile("陰陽配列は"))
				print(yinyang)
				print()
			index+=1