from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Open the local file directly
        page.goto("file:///app/index.html")
        page.set_viewport_size({"width": 1280, "height": 1024})

        # Take screenshot of the entire page
        page.screenshot(path="verification/almus_homepage.png", full_page=True)

        # Also take a specific screenshot of the product section
        product_section = page.locator("#product")
        product_section.screenshot(path="verification/almus_product.png")

        browser.close()

if __name__ == "__main__":
    run()
