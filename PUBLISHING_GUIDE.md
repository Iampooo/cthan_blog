# ✍️ CT's Publishing & Tweaking Guide

Welcome to your new publishing environment. This guide explains how to write new articles, handle translations, and tweak the visual design of the site.

---

## 1. Publishing a New Article

All articles live inside the `src/content/articles/` directory.

To publish a new post, simply create a new Markdown (`.md`) file in this folder. Astro automatically reads the file and generates the webpage.

### Required Frontmatter
Every post **must** have a block of YAML "frontmatter" at the very top of the file. This tells the website how to categorize and display your post.

```yaml
---
type: "essay"          # Must be exactly one of: 'book', 'essay', 'memo', 'learn'
title: "Your Title"    # The display title of the post
date: 2024-03-10       # Standard ISO date format (YYYY-MM-DD)
lang: "en"             # Language of the post: 'en' for English, 'zh' for Chinese
tags: ["tech", "life"] # Optional array of strings
draft: false           # Optional: Set to true to hide the post from the live site
---
```

*(Note: The `description` field is completely optional and is no longer used for the blog feed, but you can keep it for your own notes or SEO if you wish!)*

---

## 2. Bilingual Translations (The Toggle)

The site has a seamless `[ 中 / EN ]` toggle built directly into the reading layout.

To utilize this, you simply rely on **file naming conventions**. No complex linking is required.

1. Write your primary post, e.g., `the-art-of-writing.md`. Ensure its frontmatter has `lang: "zh"`.
2. Write your translated post and append `-en` to the filename, e.g., `the-art-of-writing-en.md`. Ensure its frontmatter has `lang: "en"`.

**How it works:**
- The website sees `the-art-of-writing.md` and displays it on the `/blog` timeline.
- Because `the-art-of-writing-en.md` exists, the website intrinsically links the two together via the `[ 中 / EN ]` button inside the article.
- The `-en` version is automatically hidden from the main `/blog` timeline to keep your feed clean!

---

## 3. Writing Syntax (Markdown + KaTeX + Notes)

Your website supports rich Markdown.

* **Equations:** Use `$math$` for inline math, and `$$math$$` for centered block equations.
* **Sidenotes (Gutter Notes):** Use the `^[Your note text here]` syntax anywhere in your paragraphs. The Javascript will automatically sweep these up, convert them to superscript numbers, and flawlessly position the note text in the left or right margins exactly parallel to where you placed the tag!

---

## 4. Tweaking the Design (CSS)

If you ever want to adjust the design, almost everything is controlled via `src/styles/global.css`.

### Adjusting Colors
Open `global.css`. At the very top inside the `@layer base` section, you will see two `:root` blocks. One for light mode, one for `.dark` mode. 

```css
:root {
  --bg: #F7F4EF;          /* Background color */
  --text: #1C1917;        /* Primary text color */
  --accent: #7C6F5B;      /* Sidenotes, small text */
  --link: #4F5EA8;        /* Link color */
  /* etc... */
}
```
Change these hex codes, and the entire site updates instantly.

### Adjusting Font Sizes
Currently, your Chinese text is rendered slightly smaller than your English text to balance the visual x-heights of the different fonts.

Inside `global.css`, look for the `FONT SIZE CUSTOMIZATION GUIDE` comment block. 

```css
body { font-size: 13px; }
@media (min-width: 1024px) { body { font-size: 15px; } }

html[lang="zh"] body { font-size: 13px; }
@media (min-width: 1024px) { html[lang="zh"] body { font-size: 15px; } }
```
Adjust these values to tweak how large the base text renders on Phones vs Desktop (`1024px`).

### Adjusting Layout Widths
If you want the reading column wider or narrower, edit `src/layouts/Article.astro`.

Find `<div class="grid lg:grid-cols-[1fr_minmax(auto,680px)_1fr]...`
Change the `680px` to whatever pixel width you desire for the central text column!
