# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.0.0] - 2021-10-18: Refactor Settings; New Sites & Plugins; v1 CSS; Themes

### Added

- Quick: A2CPS [Site] (#271, #272, #380)
- GH-245/FP-1097: v1–v2 Migration Stylesheet (#274)
- GH-73: Blockquote, Offset [...] Plugins (#275)
- Quick: Support Non-Bootstrap Link & Picture Plugins (#278)
- FP-1097: A2CPS: Add Snippets (#288)
- GH-89: (Minimal) System Monitor Plugin (a.k.a. SysMon) (#297)
- GH-298: Add "See All" Link Component (#300)
- Quick: Support Snippets & Add 1 Useful Snippet (#301)
- GH-75: Data List - Styles / Component / Plugin (#305, #308, #326, #336)
- GH-310: Breadcrumbs [...] (#311)
- GH-310: [...] Standard Template (#311)
- GH-98: Typography (#312, #314, #316, #318)
- GH-83: Callout Plugin (#324)
- GH-88: System Specs Plugin (#323, #330)
- UTRC-356: New UTRC [...] (#367, #368, TACC/Core-CMS-Resources#80)
- Quick: (UTRC-356) Add CSS Mixins for "Overlay" (#362, #368)
- GH-191: Theme (for ProTX Light Header & TACC Blue Header) (#192)
- `taccsite_custom`
  - FP-1238/GH-68: Frontera: [...] Add Standard Template (TACC/Core-CMS-Resources#69)
  - Quick: Frontera: Save Newsletter Snippets (TACC/Core-CMS-Resources#63)
  - GH-70: ProTX & A2CPS: [...] Add Standard Template (TACC/Core-CMS-Resources#73)
  - FP-1217: New UTRC Logo (TACC/Core-CMS-Resources#83)
  - GH-191: ProTX: Support 'has-dark-logo' theme (TACC/Core-CMS-Resources#87)
  - [Texascale: Load Blog a.k.a.] Hotfix: Texascale: Post-FP-1194 Fix (Restore Blog) (#95)

### Changed

- GH-73: [Update Sample Plugin to be Consistent with other Plugins] (#275)
- Quick: Support Variable in x-truncate CSS (#304)
- Quick: GH-253: Tweak Style Guide CSS (#325, #326)
- GH-331: Cleanup Fullwidth Template (#332)
- [Major: Split Settings and Secrets] (#341, #345, #347, #348, TACC/Core-CMS-Resources#77)
- [Quick: Add UTRC Site] (#345, #357)
- [FP-1194: Synchronize User Login between Core Portal and CMS] (#341, #346, #356)
- Quick: (UTRC-356) Migrate Banner Overlay Styles from Core (to Frontera) (#361, #368)
- `taccsite_custom`
  - FP-1238/GH-68: Frontera: Cleanup Templates [...] (TACC/Core-CMS-Resources#69)
  - Quick: Support & Move Snippets (TACC/Core-CMS-Resources#66)
  - GH-70: ProTX & A2CPS: Cleanup Templates [...] (TACC/Core-CMS-Resources#73)

### Fixed

- GH-283/GH-284: Fix Facebook Share Bug (Smaller TACC Logo) (#283)
- Hotfix/FP-1194: Use gettext_lazy Not gettext (fixed tup-cms deploy) (#344)
- GH-353: Fix Missing Bold for Guide Pages (#354)
- FP-1234: Add Missing Top Margin for Headings (#359)
- Hotfix: (UTRC-356) Let Banner Section Padding Match Other Sections (#363, #368)
- Hotfix: (UTRC-356) Avoid Grid Blowout (#365, #368)
- Hotfix: (UTRC-356) Darker Core Body Text (#366, #368)
- Hotfix: Static Images for Getting Started Guide (#369)
- FP-1232: Fix Inconsistent Search Bar Icon Size (#371)
- `taccsite_custom`
  - GH-81: Fix Favicons Not Loading (#82)

### Removed

- `taccsite_custom`
  - GH-89: Remove SysMon Snippet (TACC/Core-CMS-Resources#67)

## [2.5.2] - 2021-07-16: Fix Publish Bug; Texascale 2020; Polish

### Added

- Major: Texascale 2020 (#256)
- GH-253: Initial Pattern Library Template & Styles (#25)
- Quick: Set Version & Add Changelog (#252)

### Changed

- Quick: Polish Sample (Greet User) Plugin (#263)

### Fixed

- FP-1099: Only rebuild index on Page type for publish or unpublish events (#262)

## [2.1.1] - 2021-06-15: Hotfix for Consistent Search Bar Size

### Changed

- GH-230: Quick: Ensure search bar font sizes match (#231)

## [2.1.0] - 2021-06-14: New Frontera Homepage, Projects, CSS Plugin; Bugfixes

### Added

- Quick: New CSS Plugin Test - Custom Media Queries are Constant (#246)
- GH-233: Frontera Hero Banner Styles - Quick (#234)
- GH-195: Clone Portal Nav (#211)
- GH-67: TACC sample plugin (#190)
- FP-982: Add `rebuild_index` haystack signal processor (#189)
- GH-157: Frontera Redesign Phase 0 (#187)
- GH-171: Support CSS that is forwards compatible (#173)
- Quick: Create & Skip empty Core cms directory (#176)
- `taccsite_custom`
    - Quick: Add `tup-cms` dir (TACC/Core-CMS-Resources#45)
    - Quick: Add empty Core `cms` directory (TACC/Core-CMS-Resources#38)
    - Quick: Add home template to `neuronex-cms` secrets (TACC/Core-CMS-Resources#32)

### Changed

- FP-526: Update Portal Nav (Fix Sample Markup, Remove Old Config) (#251)
- Quick: Deprecate `site_shared` (#218)
- Quick: Simplify CSS Build Config & Fix Warnings (#199)
- Quick: Update for `taccsite_custom` repo rename (#197)
- Quick: Remove body background warn color for new sites (#175)
- Quick: FP-893/FP-977: Support new templates (#162)
- FP-947: Support favicon as custom asset (#160)
- `taccsite_custom`:
    - TACC/Core-CMS-Resources#35: Redesign Frontera home page (TACC/Core-CMS-Resources#39)
    - Quick: Remove body background warn color for new sites (TACC/Core-CMS-Resources#37)
    - TACC/Core-CMS-Resources#33: Sysmon quick redesign (#36)
    - Quick: Rename `3dem` to `neuronex` (TACC/Core-CMS-Resources#30)

### Fixed

- Quick: Simplify CSS Build Config & Fix Warnings (#199)
- Quick: Run `npm audit fix` & `yarn install` (#170)
- Quick: Settings changes to make search indexing work (#169)
- Quick: Propagate template rename to stylesheet (#167)
- `taccsite_custom`:
    - Hotfix: Add missing `__init__.py` (TACC/Core-CMS-Resources#40)
    - Quick: Import missing CSS tool (TACC/Core-CMS-Resources#43)
    - Quick: Fix `neuronex` setting (TACC/Core-CMS-Resources#31)

### Removed

- Noop: Delete outdated README.md (#200)
- FP-526: Update Portal Nav (Fix Sample Markup, Remove Old Config) (#251)

## [2.0.0] - 2021-03-31
v2.0.0 Production release as of Mar 31, 2021.

[unreleased]: https://github.com/TACC/Core-CMS/compare/v3.0.0...HEAD
[3.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.0.0
[2.5.2]: https://github.com/TACC/Core-CMS/releases/tag/v2.5.2
[2.1.1]: https://github.com/TACC/Core-CMS/releases/tag/v2.1.1
[2.1.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.1.0
[2.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.0.0
