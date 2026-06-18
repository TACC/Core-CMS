# GH-999: Editable header

Related:

- [#999](https://github.com/TACC/Core-CMS/issues/999)
- [#1083](https://github.com/TACC/Core-CMS/pull/1083)

## Status as of 2026-06

| State               | Description                       |
| ------------------- | --------------------------------- |
| one placeholder     | `header-logo` static placeholder  |
| if plugin is added  | `TaccsiteHeaderLogoPlugin` is only option |
| if plugin not added | renders settings-based logo       |
| nav and markup URL  | both use `header_logo.html`       |

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

| Idea                                         | Problem                                             |
| -------------------------------------------- | --------------------------------------------------- |
| One slot + custom `render_`* in many regions | Preview/Structure break; Picture edits need refresh |
| Nest plugins under logo but render elsewhere | Preview/Structure break; Picture edits need refresh |
| `static_placeholder` away from visible logo  | Bad WYSIWYG; toolbar/Structure bugs                 |
| Per-region render registry without A or B    | Publish-only; bad edit UX                           |
| Prematurely code Option A                    | Two plugins for one logo                            |
| `cache = False` only                         | Doesn’t fix render vs placeholder split             |
| Draft in `render_`*, placeholder elsewhere   | Image swap lag; duplicate surfaces                  |
| Edit-only placeholder at top of header       | Structure JS errors; no real preview                |
