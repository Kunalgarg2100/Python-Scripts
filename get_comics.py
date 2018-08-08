
import requests
import urllib
from bs4 import BeautifulSoup
import sys,os

path = sys.argv[2]
max_pages = sys.argv[1]
source_code = requests.get("https://xkcd.com/")
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"lxml")

pl = int(soup.findAll('li')[6].find('a').attrs['href'].strip('/')) + 1

def comicspage(path,max_pages):
    global pl
    max_pages = int(max_pages)
    page = 1
    img_box = []
    while page <= max_pages:
        url = "https://xkcd.com/" + str(pl) + "/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")
        for link in soup.findAll('div',{'id':'comic'}):
            ans = 'https:' + link.find('img').attrs['src']
            name = link.find('img').attrs['alt']
            print("Downloading {}.png".format(name))
            urllib.request.urlretrieve(ans,os.path.join(path,os.path.basename(ans)))
            img_box.append(ans)
        page += 1
        pl -= 1

comicspage(path,max_pages)
