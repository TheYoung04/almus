from playwright.sync_api import sync_playwright
import sys
import os

def test_skip_link():
    print("Verifying 'Skip to Content' link...")

    # Use the current working directory to find index.html
    cwd = os.getcwd()
    file_url = f"file://{cwd}/index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_url)

        # 1. Check if the link exists
        skip_link = page.locator('.skip-link')
        if skip_link.count() == 0:
            print("❌ FAIL: '.skip-link' element not found.")
            sys.exit(1)

        # 2. Check text content
        text = skip_link.inner_text()
        if "Langkau ke Kandungan" not in text:
            print(f"❌ FAIL: Expected text 'Langkau ke Kandungan', found '{text}'")
            sys.exit(1)

        # 3. Check visibility (should be hidden initially)
        # Note: 'hidden' in CSS often means off-screen or 0 opacity, which playwright might consider 'visible' if it's in the DOM and has size.
        # We'll check bounding box.
        box = skip_link.bounding_box()
        # If it's off-screen (e.g. top < 0)
        if box['y'] >= 0 and box['x'] >= 0:
             # It might be technically 'visible' to the user if we didn't style it yet.
             # We want to verify it IS visible on focus.
             # Let's assume for this test we expect it to be visually accessible when focused.
             pass

        # 4. Tab to it and check visibility
        page.keyboard.press("Tab")

        focused_element = page.evaluate("document.activeElement.className")
        if "skip-link" not in focused_element:
             print(f"❌ FAIL: First tab did not focus skip link. Focused: {focused_element}")
             # We won't exit here, maybe it's the second element? No, should be first.
             sys.exit(1)

        # Wait for transition
        page.wait_for_timeout(500)

        # Check if it's visible now (e.g. within the viewport)
        box = skip_link.bounding_box()
        if box['y'] < 0:
             print(f"❌ FAIL: Skip link focused but still off-screen. y={box['y']}")
             sys.exit(1)

        # 5. Click/Press Enter and check target
        page.keyboard.press("Enter")

        # Check URL hash
        if "#home" not in page.url:
             print(f"❌ FAIL: URL did not update to #home. URL: {page.url}")
             sys.exit(1)

        # Check focus moved to #home or main content
        # Since #home is the target, it should be focused or the viewport should be there.
        # With tabindex="-1", document.activeElement should be the target.
        active_id = page.evaluate("document.activeElement.id")
        if active_id != "home":
             print(f"❌ FAIL: Focus did not move to target element #home. Active ID: {active_id}")
             sys.exit(1)

        print("✅ SUCCESS: Skip link verified.")
        browser.close()

if __name__ == "__main__":
    test_skip_link()
