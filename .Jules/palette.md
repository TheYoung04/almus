## 2024-05-23 - Initial Setup
**Learning:** Started work on Sos Cili Almus. Codebase is simple HTML/CSS. Identified missing keyboard accessibility features.
**Action:** Will implement focus indicators and smooth scrolling.
## 2024-05-23 - Enhanced Keyboard Accessibility
**Learning:** Added 'scroll-behavior: smooth' and high-contrast ':focus-visible' outline. Verified with Playwright script. The 'invisible' UX of keyboard navigation is now properly supported.
**Action:** Always check keyboard navigation flow.
## 2024-10-24 - Motion & Navigation Accessibility
**Learning:** Smooth scrolling provides great context for navigation anchors but can trigger motion sickness in some users.
**Action:** Always wrap `scroll-behavior: smooth` in a `prefers-reduced-motion: no-preference` query (or reset it in a `reduce` query) to ensure we respect user choices while delighting others.
## 2024-05-23 - Preventing CLS and Improving Conversion Flow
**Learning:** For single-product landing pages, preventing Cumulative Layout Shift (CLS) on the main product image is critical for perceived stability. Explicit `width` and `height` attributes ensure the browser reserves space before the image loads. Additionally, for external conversion links (like WhatsApp), opening in a new tab (`target="_blank"`) preserves the user's session on the landing page, allowing them to return easily if they abandon the conversion flow.
**Action:** Always verify `width` and `height` on hero/product images and check `target` attributes on external CTA buttons.
