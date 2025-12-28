from playwright.sync_api import sync_playwright

def verify_skip_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        page.goto("file:///app/index.html")

        # Initial state: Skip link should be hidden (off-screen)
        # We can check its computed style or position
        skip_link = page.locator(".skip-link")

        # Force focus on the skip link to simulate tab navigation
        skip_link.focus()

        # Wait for transition if any
        page.wait_for_timeout(500)

        # Take a screenshot of the top of the page
        page.screenshot(path="verification/skip_link_visible.png", clip={"x": 0, "y": 0, "width": 800, "height": 200})

        print("Screenshot captured: verification/skip_link_visible.png")

        browser.close()

if __name__ == "__main__":
    verify_skip_link()
