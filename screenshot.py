from playwright.sync_api import sync_playwright # type: ignore

def tirar_screenshot(url, output="images/screenshot.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=output)
        browser.close()

