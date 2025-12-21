from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")
        page.set_viewport_size({"width": 1280, "height": 1024})

        # Focus the skip link to make it visible
        page.keyboard.press("Tab")

        # Wait for transition (0.3s) + buffer
        page.wait_for_timeout(500)

        # Take a screenshot
        page.screenshot(path="verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run()
