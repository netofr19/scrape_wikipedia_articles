import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url, depth=5):

    if depth == 0:
        return None

    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id='firstHeading')
    print(f"Title={title.text}")
    print(url)

    content = soup.find(id="bodyContent").find_all('p')
    if len(content[0].text) > 1:
        print(f"Content={content[0].text}...")
    else:
        print(f"Context=This page doesn't have any body content.")

    print("\n")

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'], depth-1)


if __name__ == "__main__":
    scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping", depth=6)
