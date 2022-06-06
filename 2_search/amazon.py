import asyncio
import pyppeteer
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
    logger.info('goto amazon.com')
    await new_page.goto('https://www.amazon.com')
    await new_page.screenshot({'path': 'amazon.png', 'fullPage': True})

    logger.info('start to search on amazon')
    await new_page.type('#twotabsearchtextbox', 'nyan cat pullover')
    await new_page.screenshot({'path': 'amazon_type.png', 'fullPage': True})
    await new_page.click('.nav-search-submit')
    await new_page.screenshot({'path': 'amazon_click.png', 'fullPage': True})
    logger.info('wait for results')
    await new_page.waitForSelector('.s-result-list>.sg-col-4-of-16')
    logger.info('save result into a png')
    await new_page.screenshot({'path':'amazon_nyan_cat_pullovers_list.png', 'fullPage': True})

    logger.info('go to next page')
    await new_page.click('.s-pagination-next')
    await new_page.waitForSelector('.s-result-list>.sg-col-4-of-16')
    logger.info('save next page into a png')
    await new_page.screenshot({'path':'amazon_nyan_cat_pullovers_next.png', 'fullPage': True})

    await browser.close()

asyncio.run(main())
