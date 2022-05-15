import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()
    await new_page.goto('https://news.ycombinator.com/news')

    name = await new_page.Jeval('.hnname', 'el => el.innerText')
    print(name)

    await browser.close()

asyncio.run(main())
