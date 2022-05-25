import asyncio
import pyppeteer

async def intercept(request: pyppeteer.network_manager.Request):
    print('request url: {}'.format(request.url))
    if request.url.endswith('.png') or request.url.endswith('.jpg'):
        await request.abort()
    else:
        await request.continue_()


async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()

    await new_page.setRequestInterception(True)
    new_page.on('request', lambda req: asyncio.ensure_future(intercept(req)))

    await new_page.setViewport({'width': 1280, 'height': 800})
    await new_page.goto('https://www.ifeng.com')
    await new_page.screenshot({'path': 'ifeng.png', 'fullPage': True})

    await browser.close()

asyncio.run(main())

