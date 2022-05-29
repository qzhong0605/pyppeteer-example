import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    new_page = await browser.newPage()

    await new_page.setViewport({'width': 1200, 'height': 800})
    await new_page.goto('https://checklyhq.com')
    image_href = await new_page.Jeval('img.hero-image', 'sel => {return sel.src.replace("/", "")}')

    view_source = await new_page.goto(image_href)
    view_buffer = await view_source.buffer()
    # write png
    print('save png as hero_image.png')
    with open('hero_image.png', 'wb') as image_fp:
        image_fp.write(view_buffer)

    await browser.close()

asyncio.run(main())
