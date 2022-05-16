import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()

    # set the viewport so we know the dimensions of the screen
    await new_page.setViewport({'width': 800, 'height': 600})

    # go to a page setup for mouse event tracking
    await new_page.goto('http://unixpapa.com/js/testmouse.html')

    # click an area
    await new_page.click('a.page', { 'button': 'left' })

    await new_page.screenshot({'path': 'mouse.png'})
    await browser.close()

asyncio.run(main())
