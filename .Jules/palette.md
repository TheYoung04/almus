## 2024-05-23 - Initial Setup
**Learning:** Started work on Sos Cili Almus. Codebase is simple HTML/CSS. Identified missing keyboard accessibility features.
**Action:** Will implement focus indicators and smooth scrolling.
## 2024-05-23 - Enhanced Keyboard Accessibility
**Learning:** Added 'scroll-behavior: smooth' and high-contrast ':focus-visible' outline. Verified with Playwright script. The 'invisible' UX of keyboard navigation is now properly supported.
**Action:** Always check keyboard navigation flow.
## 2024-10-24 - Motion & Navigation Accessibility
**Learning:** Smooth scrolling provides great context for navigation anchors but can trigger motion sickness in some users.
**Action:** Always wrap `scroll-behavior: smooth` in a `prefers-reduced-motion: no-preference` query (or reset it in a `reduce` query) to ensure we respect user choices while delighting others.
