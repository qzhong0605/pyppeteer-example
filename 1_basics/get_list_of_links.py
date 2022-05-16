import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()

    await new_page.tracing.start({
        'path': 'trace.json',
        'categories': ['devtools.timeline']
    })

    await new_page.goto('https://news.ycombinator.com/news')
    titles = await new_page.JJeval('a.titlelink', 'anchors => {return anchors.map(anchor => anchor.href)}')

    print('Total number of links for news: {}'.format(len(titles)))
    for idx in range(len(titles)):
        print('{}. {}'.format(idx, titles[idx]))

    await new_page.tracing.stop()
    await browser.close()

asyncio.run(main())
