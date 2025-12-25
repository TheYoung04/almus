import os
import time
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_url = f"file://{os.path.abspath('index.html')}"
        print(f"Loading: {file_url}")
        page.goto(file_url)

        # 1. Press Tab to focus the first element
        page.keyboard.press("Tab")

        # Wait for transition (0.3s defined in CSS)
        page.wait_for_timeout(500)

        # 2. Check active element text
        active_text = page.evaluate("document.activeElement.innerText")
        print(f"First tab stop text: '{active_text}'")

        if "Langkau ke Kandungan" not in active_text:
            print("❌ Failure: First tab stop is not 'Langkau ke Kandungan'.")
            browser.close()
            exit(1)

        # 3. Check position
        box = page.evaluate("document.activeElement.getBoundingClientRect()")
        print(f"Bounding Box: {box}")

        # Allow small tolerance or exact 0
        if box['top'] < 0:
            print("❌ Failure: Skip link is still off-screen when focused.")
            browser.close()
            exit(1)

        # 4. Activate the link
        page.keyboard.press("Enter")

        # 5. Verify navigation to content
        if "#home" not in page.url:
             print(f"❌ Failure: URL did not update to include #home. Current: {page.url}")
             browser.close()
             exit(1)

        # Check where the focus is. Ideally it should be on #home or body,
        # but definitely NOT the skip link anymore (if it went away)
        # or it should be the content.
        # Without tabindex=-1, focus often stays on the anchor or resets.
        # Let's see what happens.
        active_id = page.evaluate("document.activeElement.id")
        print(f"Active element ID after navigation: '{active_id}'")

        print("✅ Success: Skip link verification passed.")
        browser.close()

if __name__ == "__main__":
    run()
