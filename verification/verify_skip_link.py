from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Open the local file
        page.goto(f"file://{os.getcwd()}/index.html")

        # Focus the skip link
        page.focus(".skip-link")

        # Take a screenshot
        page.screenshot(path="verification/skip_link_focused.png")

        browser.close()

if __name__ == "__main__":
    run()
