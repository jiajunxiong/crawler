import re
import requests
from lxml import html
from bs4 import BeautifulSoup

r = requests.get("http://stock.jrj.com.cn/2018/07/09213924789278.shtml")
soup = BeautifulSoup(r.content, "html.parser")

for td in soup.findAll("div", class_="texttit_m1"):
    for p in td.findAll("p"):
        content=p.text
        content=re.sub(r'\((.*?)\)', "", content)
        print (content)
