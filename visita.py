import os, random, time, asyncio
from playwright.async_api import async_playwright

URL = os.environ["ENLACE"]
N = int(os.environ.get("VISITAS", "2"))
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 Version/17.5 Mobile Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 Chrome/131.0 Mobile Safari/537.36",
]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for i in range(N):
            ctx = await b.new_context(
                user_agent=random.choice(UAS), locale="es-ES",
                viewport={"width": 390, "height": 780},
            )
            page = await ctx.new_page()
            try:
                await page.goto(URL, wait_until="domcontentloaded", timeout=40000)
                await page.wait_for_timeout(3000)
                for _ in range(3):
                    await page.mouse.click(200, 400)
                    await page.wait_for_timeout(600)
                await page.wait_for_timeout(1500)
                try:
                    await page.get_by_text("VALE", exact=True).first.click(timeout=6000)
                except Exception:
                    pass
                await page.wait_for_timeout(4000)
                await page.mouse.wheel(0, 500)
                await page.wait_for_timeout(2000)
            except Exception as e:
                print("fallo", e)

asyncio.run(main())
