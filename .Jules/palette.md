## 2024-05-23 - Initial Setup
**Learning:** Started work on Sos Cili Almus. Codebase is simple HTML/CSS. Identified missing keyboard accessibility features.
**Action:** Will implement focus indicators and smooth scrolling.
## 2024-05-23 - Enhanced Keyboard Accessibility
**Learning:** Added 'scroll-behavior: smooth' and high-contrast ':focus-visible' outline. Verified with Playwright script. The 'invisible' UX of keyboard navigation is now properly supported.
**Action:** Always check keyboard navigation flow.
## 2024-10-24 - Motion & Navigation Accessibility
**Learning:** Smooth scrolling provides great context for navigation anchors but can trigger motion sickness in some users.
**Action:** Always wrap `scroll-behavior: smooth` in a `prefers-reduced-motion: no-preference` query (or reset it in a `reduce` query) to ensure we respect user choices while delighting others.
## 2024-10-24 - Fixed Header & Anchor Navigation
**Learning:** Fixed headers often obscure content when navigating via anchor links (`#section`). Adding `scroll-padding-top` to `html` matching the header height solves this elegantly without JavaScript or complex padding hacks on sections.
**Action:** Always check anchor navigation in sites with fixed headers and apply `scroll-padding-top`.
## 2024-10-24 - Skip Link Navigation
**Learning:** Fixed headers require 'z-index' planning for skip links. The skip link must have a higher z-index than the header to be visible. Also, target containers need 'tabindex="-1"' for programmatic focus to land correctly in all browsers.
**Action:** When implementing skip links, verify z-index stacking and ensure the target ID has 'tabindex="-1"'.
