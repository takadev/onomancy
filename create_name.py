import sys
import requests
import codecs
import re
import urllib

args = sys.argv

if len(args) < 3:
    sys.exit()

gender = args[1]
if gender != "m" and gender != "f":
    sys.exit()

first_name = args[2]

last_name = "金子"
url = "http://www.iinamae.net/nm/"
boy_txt = "boy.txt"
girl_txt = "girl.txt"
cookie = { 
    "sei":last_name,
    "sex":1,
    "yomi":first_name,
    "mode":"hibiki"
}
if gender == 'f':
    cookie["sex"] = 2

s = requests.session()
res1 = s.post(url, data=cookie)
res1.raise_for_status()
iiname_id = s.cookies.get("iinamae")

post = {
    #"iiname":iiname_id,
    "yomi":first_name,
    "mode":"hibiki"
}
res2 = s.post(url, data=post, headers={'Referer': url})
print(res2.content.decode('euc-jp'))
