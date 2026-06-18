# GH-999: Editable header

Related:

- [#999](https://github.com/TACC/Core-CMS/issues/999)
- [#1083](https://github.com/TACC/Core-CMS/pull/1083)

## Status as of 2026-06

| State | Description |
| --- | --- |
| Placeholder | `header-logo` static placeholder |
| CMS logo | `TaccsiteHeaderLogoPlugin` only (Picture subclass) |
| Empty slot | Settings-based logo via `header_logo_via_settings.html` |
| Markup | Same `header_logo.html` in nav and `/cms/header/logo/markup/` |

Branding, nav, and search remain settings-based.

## Known limitations

| Issue | Summary | Why allow |
| --- | --- | --- |
| [#1185](https://github.com/TACC/Core-CMS/issues/1185) | Logo without a link may lack `class="portal-logo"` on `<img>`. | Add form defaults link to home. |

## Future header plugins (pick one)

Plugins must render where `{% static_placeholder %}` sits (see [Failed ideas](#failed-ideas)).

### A. Wrapper plugin

One placeholder; extra container plugin; may require migrating `header-logo`.

### B. Multiple placeholders

Typical CMS pattern; several placeholders; can keep `header-logo` as today.

## CMS editor UX

- Static placeholder visible in Structure mode at the logo.
- Add/edit/delete Header logo refreshes page preview.
- Structure toggle controls Structure sidebar.

## Failed ideas

| Idea | Problem |
| --- | --- |
| Custom `render_*` instead of `static_placeholder` | Breaks Structure/preview; duplicate publish path |
| Nest plugins under logo but render elsewhere | Preview/Structure break |
| `static_placeholder` away from visible logo | Bad WYSIWYG |
| Per-region render registry without A or B | Publish-only; bad edit UX |
| Premature Option A wrapper | Two plugins for one logo |
| `cache = False` only | Does not fix render vs placeholder split |
| Edit-only placeholder at top of header | Structure JS errors |
