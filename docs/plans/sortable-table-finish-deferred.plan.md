---
name: Sortable table finish (deferred)
overview: "After Phase 0 merge: steps 5–7 — JS-built filters, cleanup, CKEditor allowlist PR to main."
status: deferred
---

# Sortable table: Phase 0, then steps 5–7

**Deferred until Phase 0 PRs are merged.** Pick up from here for dynamic filters + hack retirement.

## Phase 0: Ship current code

Merge as-is: Core-CMS sortableTable, Core-Styles promote util, tup-ui snippet pins.

## Step 5: Dynamic filter markup in JS

Table-only in CMS; JS builds fieldset/controls/output; ARIA set in code.

## Step 6: Clean up

Remove snippet promote; dedupe JS; bump SHAs.

## Step 7: CKEditor ARIA — separate branch → `main`

`extraAllowedContent` for published `aria-*`; not a blocker for step 5.

## Order

Phase 0 → Step 5 → Step 6; Step 7 can parallel after Phase 0.
