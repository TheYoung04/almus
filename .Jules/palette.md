## 2024-10-24 - Motion & Navigation Accessibility
**Learning:** Smooth scrolling provides great context for navigation anchors but can trigger motion sickness in some users.
**Action:** Always wrap `scroll-behavior: smooth` in a `prefers-reduced-motion: no-preference` query (or reset it in a `reduce` query) to ensure we respect user choices while delighting others.
