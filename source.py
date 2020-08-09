#Simple Web Scraping

import requests
from bs4 import BeautifulSoup as soup

path = requests.get("https://news.ycombinator.com/news")
soupObj = soup(path.text, "html.parser")
links = (soupObj.select(".storylink")) #grabbing all links
votes = (soupObj.select(".score")) #grabbing scores

def news_by_votes(links, subtext):
  news = []

  for i, item, in enumerate(links):
    title = links[i].getText()
    href = links[i].get("href", None)
    vote = subtext[i].select(".score")
    
    if len(vote):
      points = int(vote[0].getText().replace(" points", ""))
      news.append({"Title": title, "Link": href, "votes": points})

    return news