# AGENTS.md

Static multi-page HTML presentation (vibe-coding slides). No framework, no build step, no bundler.

## Run / preview
- Serve the folder with any static server, e.g. `python3 -m http.server 8000`, then open `http://localhost:8000/part-N.html`.
- There is **no npm/build/test** — just edit files and reload.

## Critical: no Tailwind / no CSS framework
- This repo does **not** load Tailwind or any CSS utility framework.
- Slide HTML is generated in JS (`js/part-N.js`). Generated markup MUST use **inline `style="..."`**, not Tailwind class names (`flex`, `items-center`, `px-5`, `rounded-xl`, etc.).
- Tailwind classes have no CSS and are silently dropped, breaking layout. This was the cause of part-1 rendering differently from other parts — it used Tailwind classes and was converted to inline styles to match parts 3/4/5.

## CSS layout
- `css/common.css` — shared styles: slider dots, nav buttons, particles, slide base, corner accents, animations. Edit shared things here.
- `css/part-N.css` — per-part theme/animations only.
- Each `part-N.html` links `css/common.css` + `css/part-N.css` + `js/part-N.js`.

## Slider dots (keep consistent)
- Every part has `<div id="dotContainer" class="dotContainer">` in the footer; JS finds it via `getElementById('dotContainer')`.
- Active/inactive dot states are defined in `css/common.css` as BOTH `.dot`/`.dot.active` (parts 2,6) and `.dot-active`/`.dot-inactive` (parts 1,3,4,5). Don't remove either pair.

## Per-part content
- Each `js/part-N.js` holds its own `slides` data array and calls `initPresentation(slides)`. Slides are hardcoded, not fetched.

## Gotcha: browser cache
- After editing CSS, a normal reload may show stale styles. Hard refresh: `Ctrl+Shift+R` (Win/Linux) / `Cmd+Shift+R` (Mac).
