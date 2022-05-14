import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()

    await new_page.setViewport({'width': 1280, 'height': 800})
    await new_page.goto('https://www.google.com')
    await new_page.screenshot({'path': 'google.jpeg', 'fullPage': True})

    await browser.close()

asyncio.run(main())
