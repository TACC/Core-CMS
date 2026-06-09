---
name: Sortable table finish (deferred)
overview: "Steps 5–6 done on branch; step 7 — CKEditor allowlist PR to main."
status: in-progress
---

# Sortable table: Phase 0, then steps 5–7

## Phase 0: Ship current code

Merge as-is: Core-CMS sortableTable, Core-Styles promote util, tup-ui snippet pins.

## Step 5: Dynamic filter markup in JS

**Done (branch):** Table-only in CMS; `data-sortable-filters` JSON on the table; JS builds fieldset/controls/output with ARIA in code. Legacy CMS-authored filter groups still work.

## Step 6: Clean up

**Done (branch):** Snippet promote removed; CDN pins use `Core-Styles@v2.57.0` and `Core-CMS@v4.40.0-rc6`.

## Step 7: CKEditor ARIA — separate branch → `main`

`extraAllowedContent` for published `aria-*`; not a blocker for step 5.

## Order

Phase 0 → Step 5 → Step 6; Step 7 can parallel after Phase 0.
