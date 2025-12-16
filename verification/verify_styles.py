import re
import sys

def verify_styles():
    try:
        with open('styles.css', 'r') as f:
            css_content = f.read()
    except FileNotFoundError:
        print("Error: styles.css not found.")
        return False

    checks = {
        "Smooth Scrolling": r"html\s*\{[^}]*scroll-behavior:\s*smooth",
        "Focus Visible": r":focus-visible\s*\{[^}]*outline:\s*[^;]*#ff8c00",
        "Reduced Motion Media Query": r"@media\s*\(\s*prefers-reduced-motion:\s*reduce\s*\)",
        "Reduced Motion Scroll Behavior": r"scroll-behavior:\s*auto", # Inside media query check logic is harder with regex, just checking presence for now
        "Reduced Motion Animation": r"animation:\s*none",
        "Reduced Motion Transition": r"transition:\s*none"
    }

    results = {}
    all_passed = True

    print("Verifying styles.css...")

    # Check for HTML smooth scrolling
    if re.search(checks["Smooth Scrolling"], css_content):
        results["Smooth Scrolling"] = "PASS"
    else:
        results["Smooth Scrolling"] = "FAIL"
        all_passed = False

    # Check for Focus Visible
    if re.search(checks["Focus Visible"], css_content):
        results["Focus Visible"] = "PASS"
    else:
        results["Focus Visible"] = "FAIL"
        all_passed = False

    # Check for Reduced Motion Block
    reduced_motion_match = re.search(checks["Reduced Motion Media Query"], css_content)
    if reduced_motion_match:
        results["Reduced Motion Media Query"] = "PASS"

        # simple heuristic: check if the subsequent content contains the resets
        # ideally we'd parse the CSS structure, but simple search after the match index is better than nothing
        rest_of_file = css_content[reduced_motion_match.end():]

        if re.search(checks["Reduced Motion Scroll Behavior"], rest_of_file):
             results["Reduced Motion Scroll Behavior"] = "PASS"
        else:
             results["Reduced Motion Scroll Behavior"] = "FAIL"
             all_passed = False

        if re.search(checks["Reduced Motion Animation"], rest_of_file):
             results["Reduced Motion Animation"] = "PASS"
        else:
             results["Reduced Motion Animation"] = "FAIL"
             all_passed = False

    else:
        results["Reduced Motion Media Query"] = "FAIL"
        all_passed = False
        results["Reduced Motion Scroll Behavior"] = "FAIL (Skipped)"
        results["Reduced Motion Animation"] = "FAIL (Skipped)"

    for check, result in results.items():
        print(f"{check}: {result}")

    return all_passed

if __name__ == "__main__":
    if verify_styles():
        print("\n✅ Verification SUCCESS")
        sys.exit(0)
    else:
        print("\n❌ Verification FAILED")
        sys.exit(1)
