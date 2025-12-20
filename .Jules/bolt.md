# Bolt's Journal

## 2024-05-22 - Static Image Optimization
**Learning:** For static sites with layout-heavy images, adding explicit `width` and `height` alongside `loading="lazy"` is crucial. Even with CSS constraints, the browser needs intrinsic dimensions to calculate aspect ratio immediately and avoid CLS.
**Action:** Always check `img` tags for missing dimension attributes, especially for off-screen images where lazy loading is applied.
