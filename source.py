#Simple Web Scraping

import requests
from bs4 import BeautifulSoup as soup

path = requests.get("https://news.ycombinator.com/news")
soupObj = soup(path.text, "html.parser")
links = (soupObj.select(".storylink")) #grabbing all links
votes = (soupObj.select(".score")) #grabbing scores