# GH-999: Editable Header

Related:

- [#999](https://github.com/TACC/Core-CMS/issues/999)
- [#1083](https://github.com/TACC/Core-CMS/pull/1083)

## Status as of 2026-06

| State               | Description                       |
| ------------------- | --------------------------------- |
| one placeholder     | `header-logo` static placeholder  |
| if plugin is added  | `TaccsiteHeaderLogoPlugin` is only option |
| if plugin not added | renders settings-based logo       |

The branding and navs and search are still settings-based.

## Known Limitations

| Issue | Summary | Why Allow This? |
| --- | --- | --- |
| [#1185](https://github.com/TACC/Core-CMS/issues/1185) | Header logo without a link is **missing** `class="portal-logo"` on `<img>`. | Default form links logo to home, so typical sites are unaffected. |

## How to Add Other Header Plugins

Requirements:

- (for [CMS editor UX](#cms-editor-ux)) plugins render where `{% static_placeholder %}` sits
- (to skip [Failed Ideas](#failed-ideas)) pick one option from below

### A. Wrapper Plugin

| Pros                           | Cons                                           |
| ------------------------------ | ---------------------------------------------- |
| One placeholder                | Extra container plugin                         |
| Layout management consolidated | Build/Maintain wrapper                         |
|                                | Must deprecate or migrate legacy `header-logo` |

### B. Multiple Placeholders

| Pros                               | Cons                               |
| ---------------------------------- | ---------------------------------- |
| Typical CMS usage                  | Several placeholders to configure  |
|                                    | Layout management not consolidated |
| Can keep using `header-logo` as is |                                    |

## CMS Editor UX

Requirements:

- Static placeholder always visible in Structure mode.
- Edit plugin: auto-refreshes page preview.
- Add/Delete plugin: auto-refreshes page preview.
- Structure mode button toggles render of Structure sidebar.

## Failed Ideas

| Idea | Problem |
| --- | --- |
| `ContentRenderer` / template tag for the logo instead of `{% static_placeholder %}` at the logo | Structure and preview break; Picture edits need refresh (removed in [#1189](https://github.com/TACC/Core-CMS/pull/1189)) |
| Published markup from code, placeholder somewhere else | Duplicate logo surfaces; draft image lags behind preview |
| Child plugins under the logo, HTML rendered elsewhere | Structure/preview break |
| `{% static_placeholder %}` not where the logo shows | Bad WYSIWYG; toolbar/Structure bugs |
| Per-region render registry (not Option A or B) | Live site publish-only; bad edit UX |
| Option A wrapper before more header plugins exist | Two plugins for one logo |
| Plugin `cache = False` only | Does not fix placeholder vs programmatic render |
| Edit-only placeholder at top of header | Structure JS errors; no real preview |
