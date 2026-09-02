import wikipediaapi as wikiapi
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("EMAIL")

async def main():
    wiki = wikiapi.AsyncWikipedia(
            user_agent="WikiRabbitHole (%s)" % email, language='en')
    page_py = wiki.page('ASCC1')
    print("Page - Exists: %s" % await page_py.exists())

    links = await page_py.links
    for title in sorted(links.keys()):
        print("%s: %s" % (title, links[title]))        

asyncio.run(main())
