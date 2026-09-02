import wikipediaapi as wikiapi
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("EMAIL")

async def main():
    wiki = wikiapi.AsyncWikipedia(
            user_agent="wiki-game-optimizer (%s)" % email, language='en')

    print("Enter exactly the name of the starting Wikipedia page: ")
    start_pg = wiki.page(input())
    print("Enter exactly the name of the ending Wikipedia page: ")
    end_pg = wiki.page(input())

    if(not await start_pg.exists()):
        print("Starting wiki page not found.")
        return
    if(not await end_pg.exists()):
        print("Ending wiki page not found.") 
        return
    
    links = await start_pg.links
    for title in sorted(links.keys()):
        print("%s: %s" % (title, links[title]))

asyncio.run(main())
