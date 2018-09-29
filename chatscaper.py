from urllib.request import urlopen as ou
from urllib.request import urlretrieve as ort
from bs4 import BeautifulSoup as soup
from time import *

url = "https://www.twitch.tv/shroud"
for i in range(5):
    doc = ou(url)
    print(doc)
    sleep(10)

    # ort(url, "html{0}.txt".format(i))

    html = doc.read()


    page_soup = soup(html, "html.parser")

    f = open("Currenthtml{0}.txt".format(i), "w")
    f.write(html)

containers_div = page_soup.findAll("span",{"class":"text-fragment"})

containers = page_soup.findAll("span",{"class":"text-fragment"})

doc.close()

# print(page_soup.span.text)

print(containers)
