from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        file_url = f"file://{os.path.abspath('index.html')}"
        page.goto(file_url)

        # Verify the image is present and visible
        product_section = page.locator('#product')
        product_image = page.locator('.product-image img')
        expect(product_image).to_be_visible()

        # Scroll to the product section
        product_section.scroll_into_view_if_needed()

        # Check if the src attribute contains .webp
        src = product_image.get_attribute('src')
        if 'product.webp' not in src:
            print(f"Error: Expected .webp image, found {src}")
            exit(1)

        print("Verified: Product image is using .webp format")

        # Take a screenshot of the product section
        page.screenshot(path="verification/screenshot_webp_product.png")
        browser.close()

if __name__ == "__main__":
    run()
