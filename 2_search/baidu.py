import pyppeteer
import asyncio
import logging

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('search')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
stream = logger.addHandler(ch)

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()

    await new_page.setViewport({'width': 1080, 'height': 800})
    logger.info('goto baidu.com')
    await new_page.goto('https://www.baidu.com')
    logger.info('screenshot as an png')
    await new_page.screenshot({'path': 'baidu.png', 'fullPage': True})

    logger.info('search java on baidu')
    await new_page.type('input#kw', 'java')
    await new_page.click('input#su.bg')
    logger.info('screenshot results as an png')
    await new_page.screenshot({'path': 'baidu_results.png', 'fullPage': True})

    await browser.close()


asyncio.run(main())
