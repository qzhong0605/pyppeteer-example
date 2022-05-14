import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    page = await browser.newPage()

    # 1. create pdf from URL
    await page.goto('https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#pdf')
    await page.pdf({'path': 'api.pdf', 'format': 'A4'})
    print('save api.md as api.pdf')

    # 2. create pdf from static html
    html_content = """<body>
<h1>An example static HTML to PDF</h1>
</body>
    """
    await page.setContent(html_content)
    await page.pdf({'path': 'html.pdf', 'format': 'A4'})
    print('save html as html.pdf')

    await browser.close()

asyncio.run(main())
