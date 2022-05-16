import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()

    await new_page.goto('https://trix-editor.org/')
    await new_page.focus('trix-editor')
    await new_page.keyboard.type('Just adding a title')
    await new_page.screenshot({'path': 'keyboard.png', 'fullPage': True})
    await browser.close()

asyncio.run(main())
