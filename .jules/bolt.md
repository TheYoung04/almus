# Bolt's Journal - Critical Learnings

## 2024-05-22 - Layout Shift Prevention
**Learning:** Adding `width` and `height` attributes to images is crucial for CLS prevention, but MUST be paired with `height: auto` in CSS to prevent distortion when `max-height` constraints are present.
**Action:** Always verify `height: auto` is present when adding dimension attributes to responsive images.
