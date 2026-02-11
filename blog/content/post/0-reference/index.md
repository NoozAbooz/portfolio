---
title: Reference
description: Note-to-self on writing blog posts with Hugo
draft: false
---

Running a dev server:

```bash
hugo server -D
```

Adding tags: https://github.com/KKKZOZ/hugo-admonitions?tab=readme-ov-file#usage

> [!NOTE] This is a note.

> [!WARNING]- This is a warning. Click me
> More info once expanded

## Show caption text on hover
Method 1: The <abbr title="HyperText Markup Language">HTML</abbr> is used for web pages.
```html
The <abbr title="HyperText Markup Language">HTML</abbr> is used for web pages.
```

Method 2: Using the title attribute on a [link with a tooltip](https://example.com "Visit example.com for more info")
```markdown
[link with a tooltip](https://example.com "Visit example.com for more info")
```

Method 3: <span title="Your hover text here">Seemingly-normal text</span>
```html
<span title="Your hover text here">Text with hover tag</span>
```