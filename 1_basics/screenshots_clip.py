import asyncio
import pyppeteer

view_port = {'width': 1280, 'height': 800}
options = {
    'path': 'clipped_stocktickers.png',
    'fullPage': False,
    'clip': {
        'x': 0,
        'y': 240,
        'width': 1000,
        'height': 100
    }
}

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()
    await new_page.setViewport(view_port)

    await new_page.goto('https://finance.yahoo.com/')
    await new_page.screenshot(options)

    await browser.close()

asyncio.run(main())
