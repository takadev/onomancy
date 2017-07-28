import sys
import requests
import codecs
import re
import bs4
import urllib
import urllib.request
from urllib.parse import urlparse
 
args = sys.argv

if len(args) < 3:
    sys.exit()

gender = args[1]
if gender != "m" and gender != "f":
    sys.exit()

first_name = args[2]

last_name = "金子"
url = "http://www.iinamae.net/nm/"
last_name_enc = last_name.encode("euc-jp")
first_name_enc = first_name.encode("euc-jp")

param = {
    "mode":"hibiki",
    "pg":1,
    "sei":urllib.parse.quote(last_name_enc),
    "yomi":urllib.parse.quote(first_name_enc),
    "view":200
}
if gender == 'f':
    param["sex"] = 1

s = requests.session()
f = open(first_name + '.txt', 'w')

while True:
    param_str = "&".join("%s=%s" % (k,v) for k,v in param.items())
    res2 = s.get(url, params=param_str, headers={'Referer': url})
    html = res2.content.decode('euc-jp')
    soup = bs4.BeautifulSoup(html, 'html.parser')

    tags = soup.find_all("a", title=re.compile("鑑定"))
    if len(tags) == 0:
        break

    for tag in tags:
        f.write(tag.text + '\n')

    param["pg"] += 1

f.close()
s.close()