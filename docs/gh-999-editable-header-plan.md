# GH-999: Editable header (`header-content`)

Plan for [#999 Let CMS Admin Edit Header](https://github.com/TACC/Core-CMS/issues/999) and stacked work on [`feat/GH-999-let-cms-admin-edit-header`](https://github.com/TACC/Core-CMS/pull/1083).

## Goals

| Priority | Item | This stack |
| --- | --- | --- |
| 1 | CMS-editable logo | [#1083](https://github.com/TACC/Core-CMS/pull/1083) (current) |
| 2 | Nav collapse breakpoint | Follow-up issue (not this stack) |
| 3 | Custom branding | PR 3 (TACC Header Branding plugin) |
| 4–6 | Portal nav, search, branding order | Later thin plugins / options |

**Backwards compatibility:** If `header-content` has no plugins, render the header exactly as today (settings-driven branding + logo + nav).

**Precedence:** CMS plugin wins when present; otherwise settings (`LOGO` / `PORTAL_LOGO`, `BRANDING` / `PORTAL_BRANDING`).

## Portal logo (HeaderLogoPlugin)

- **One plugin:** [`HeaderLogoPlugin`](taccsite_cms/contrib/taccsite_header_logo/cms_plugins.py) extends Picture (same model, no migration). Toolbar: **TACC Header → Header logo** — full Picture fields/templates; default `id="header-logo"` when Attributes omit `id`.
- **Render:** Standard Picture template at `{% static_placeholder "header-content" %}`.
- **Empty placeholder:** `or` fallback [`header_logo_via_settings.html`](taccsite_cms/templates/header_logo_via_settings.html) (`LOGO` / `PORTAL_LOGO`).
- **Branding images (PR 3):** nested Pictures under TACC Header Branding — not top-level.
- **Follow-up:** Match `PORTAL_LOGO` / `header_logo_via_settings.html` defaults to Header logo form defaults (margin, height, link) and Core-Styles — deferred until willing to test Core-Styles.

## PR stack

1. **#1083 → `main`:** `header-content` static placeholder, superuser-only edit, settings fallback.
2. **PR 1.75** (base: feature branch): `HeaderLogoPlugin` — correct markup + CMS edit UX (targets #1083 branch).
3. **PR 2** (base: feature branch): Full-header orchestrator (`header_nav.html`, etc.).
4. **PR 3** (base: after PR 2): TACC Header Branding plugin; add to `CMS_PLACEHOLDER_CONF`.

After #1083 merges, rebase the feature branch onto `main` before the stack lands on `main`.

## Template files

Portal/Guide repos duplicate header markup ([Confluence](https://confluence.tacc.utexas.edu/x/LoCnCQ)). **`base.html` keeps `{% include "header.html" %}` only.**

| File | Role |
| --- | --- |
| [`header.html`](../taccsite_cms/templates/header.html) | Branding + nav; full `{% static_placeholder "header-content" or %}` + settings fallback. |
| [`header_logo.html`](../taccsite_cms/templates/header_logo.html) | Core-Portal `/cms/header/logo/markup/` — logo-only via [`render_header_logo`](../taccsite_cms/templatetags/header_tags.py) or settings. |
| [`header_logo_via_settings.html`](../taccsite_cms/templates/header_logo_via_settings.html) | Settings-only logo (`or` fallback). |
| [`render.py`](../taccsite_cms/contrib/taccsite_header_logo/render.py) | `render` — published logo plugin only (reuse in PR 2). |
| `header_nav.html` | **PR 2** — extract `<nav>…</nav>`. |

## Testing

### #1083 + PR 1.75

1. **Backwards compatibility:** Empty `header-content` → settings logo; branding/nav unchanged.
2. **Superuser — logo:** Add **Header logo** plugin (image + optional link). Publish. Nav shows custom logo; placeholder still editable in `?edit`.
3. **Superuser — footer:** `footer-content` unchanged.
4. **Non-superuser:** Cannot edit static placeholders.
5. **Limits:** One `HeaderLogoPlugin` in `header-content` (`global` 2 reserved for PR 3).
6. **Core-Portal markup URL:** `/cms/header/logo/markup/` uses published `header-content` logo plugin or settings (not draft/edit toolbar).
7. **Permissions after deploy:** Group perms; re-check step 4.

### PR 2 (orchestrator)

1. Empty placeholder → same as today.
2. Header logo plugin → full nav + settings branding.
3. Edit UX for `header-content` at header level.

### PR 3 (branding plugin)

1. Branding plugin + header logo → both slots; settings branding hidden when plugin present.
