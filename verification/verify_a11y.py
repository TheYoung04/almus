from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")

        # Check if skip link exists
        skip_link = page.locator(".skip-link")
        if skip_link.count() == 0:
            print("❌ Skip link not found")
            exit(1)
        print("✅ Skip link found")

        # Check if it's hidden initially (by position)
        box = skip_link.bounding_box()
        # Since it's top -9999px, y should be negative
        if box['y'] >= 0:
            print(f"❌ Skip link should be hidden initially, but y is {box['y']}")
            exit(1)
        print("✅ Skip link hidden initially")

        # Tab to focus
        page.keyboard.press("Tab")

        # Check if focused
        if not skip_link.is_visible(): # Wait, is_visible checks display/visibility/opacity/bounding box
            # It should be visible now because top: 0
            # Playwright might wait for transition
            pass

        # Let's check focus
        focused = page.evaluate("document.activeElement.className")
        if "skip-link" not in focused:
            print(f"❌ First tab did not focus skip link. Focused element class: {focused}")
            exit(1)
        print("✅ First tab focused skip link")

        # Check visibility after focus
        # We need to wait for transition or check computed style
        page.wait_for_timeout(500) # Wait for transition
        box = skip_link.bounding_box()
        if box['y'] < 0:
             print(f"❌ Skip link should be visible after focus, but y is {box['y']}")
             exit(1)
        print("✅ Skip link visible after focus")

        browser.close()

if __name__ == "__main__":
    run()
