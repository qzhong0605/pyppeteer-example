import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()
    await new_page.goto('https://www.google.com')

    title = await new_page.title()
    print('page tile is: {}'.format(title))

    await browser.close()

asyncio.run(main())
