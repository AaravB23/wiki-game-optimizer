import wikipediaapi as wikiapi
import asyncio

async def main():
    wiki = wikiapi.AsyncWikipedia(
            user_agent='WikiRabbitHole (aaravbhatt76223@gmail.com)', language='en')
    page_py = wiki.page('Python_(programming_language)')
    print("Page - Exists: %s" % await page_py.exists())

    print(await page_py.text)

asyncio.run(main())
