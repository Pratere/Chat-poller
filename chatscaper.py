from urllib.request import urlopen as ou
from bs4 import BeautifulSoup as soup

url = "https://www.cnet.com/how-to/how-to-view-text-only-versions-of-web-sites/"

doc = ou(url)

html = doc.read()

doc.close()

page_soup = soup(html, "html.parser")

containers = page_soup.findAll("p",{"class":"speakableText*"})

print(containers)
