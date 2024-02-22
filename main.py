import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

url = 'https://news.ycombinator.com/newest'

async def fetch_title(session, url):
    async with session.get(url) as response:
        content = await response.text()
        soup = BeautifulSoup(content, "html.parser")
        return soup

async def get_most_recent(soup):
    title_data = []
    news_names = soup.find_all('span', class_='titleline')

    for title in news_names:
        title_data.append(title.text)

    return title_data

async def crawl(url):
    async with aiohttp.ClientSession() as session:
        soup = await fetch_title(session, url)
        recent_titles = await get_most_recent(soup)

        i = 1
        for title in recent_titles:
            print(f"{i}. {title}")
            i += 1

st = time.time()
asyncio.run(crawl(url))
et = time.time()
print(et-st)