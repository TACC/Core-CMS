# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.19.0] - 2022-03-17: Plugin Transfer, Classes; ECEP CMS; Fix v3.15, Safe ES

### Added

- Test: Install djangocms-transfer (#411)
- FP-1414: More Classnames for Django CMS Style Plugin (#419)
- GH-110: Add PR template (#454)
- Added [...] new ECEP portal CMS. (00eca44, 156a3d1)

### Fixed

- FP-1423: System Specs Layout Bug at Medium Width Screen (#444) 
- FP-1341: Update README.md Since Settings Refactor (#417) 
- FP-1525: UTRC: Fix Homepage Whitespace (#447)
- FP-1359: Callout Plugin Active+Focus State Anomaly within Dark Section (#449)
- FP-1524: Section Pattern: [Fix] Extended Background (#446)
- FP-1470: Section Pattern: Third Style (and Fix to Dark Style) (#458)
- FP-1451: Open CMS External Links in New Window (Works on Portal) (#453)
- FP-1410: Shrink Guide Images & Add Links to Open in New Tab (#462)

### Security

- FP-1540: Hotfix: Update ES to Fix Security Issue (#456)

## [3.15.0] - 2022-02-17: New Section Pattern; Critical Dependency Fix; Other

### Added

- FP-1318: Create Section Pattern via Style Plugin (#430)

### Changes

- Quick: (Texascale) Do Not Let Search Engines Index 2022 Pages (#443)
- FP-1318: Revisit Section Pattern (#433)

### Fixed

- FP-1502: Fix Callout Title Height (#441)

### Removed

- UTRC-357/FP-1268: (UTRC) Remove old templates (#439)

### Security

- FP-1285: CMS Critical Dependency Upgrade (#437)

## [3.14.0] - 2022-01-25: Deprecate Callout Plugin; Guide Page Fix; Other Fixes

### Added

- FP-1415: Callout Pattern with Fixes sans Plugin (#427)
    - Callout Plugin - Crop Images within Ratio (GH-329)

### Changed

- FP-1417: Callout CSS to Style Child Elements via Tag not Class (#425)
- FP-1416: Callout Image Resize w/ JS not CSS (#421) (#422)

### Fixed

- FP-1422: (UTRC) Remove White Border Under Header (#435)
- FP-1418: Callout Link Clickable Area Fix (#423)
- FP-1416: Callout Image Resize w/ CSS not JS (#421) (#422)
    - Callout Plugin - Fix Image Resize Caveat (GH-327)
    - Element Transform Fails on Child Plugin Markup w/out Hack (GH-320)
- FP-1435: Updates on Getting Started page (#428)
- FP-1408: (Frontera) Fix Clickable Area of Article List Link (#429)
- Remove a "Task/" from CHANGELOG entry (d773289)
- Minor: Fix: x-layout CSS docblock typo (#434)

### Removed

- Deleted `resize_figure_to_fit` feature of Callout Plugin. (#421) (#422)
- Deleted `elementTransformer` module and `SizeContentToFit` class. (#421)

### Deprecated

- Callout Plugin is unsupported. Replace with Callout Pattern. (#427)
- Marked README.md as outdated & added link to new draft. (61b310b)

## [3.12.1] - 2021-12-21: BM Branding; UI Patterns; Search Bar Design; UTRC Font

### Added

- BM-22: BrainMap: Add UTHSC-SA Logo [and Remove SGCI Logo Text] (#414)
- FP-1289 Image Grid Pattern (#415)
- FP-1291: C-Recognition Pattern (#416)
- FP-1290: Card UI Pattern (Frontera About Page) (#420)

### Changed

- FP-1287: Redesign & Refactor Search Bar (#383)
- UTRC-357/FP-1268: Retire v1 Styles (Use v2 Styles) (#360)
- Quick: Move Code & Samp CSS from Site to Doc Page (#424)

## [3.5.1] - 2021-11-18: Remove Sentence from Getting Started Doc

### Fixed

- Quick: Remove sentence from Getting Started doc (#410)

## [3.5.0] - 2021-11-15: Navbar Toggle Color; OOTB Remote Login; v3.3.0 Fixes

### Added

- COOKS-108: Navbar Toggler Icon Color [per Theme] (#402)

### Changed

- Update settings.py: Haystack Connection INDEX_NAME (#374)
- Update settings.py: CEP_AUTH_VERIFICATION_ENDPOINT (#375)

### Fixed

- COOKS-108: Navbar Toggler Icon Color [Fix for "Has Dark Logo" Theme] (#402)
- Hotfix/FP-1234: Texascale: Remove Category Page Title Margin Top (#388)
- Hotfix/FP-1338: Offset Content to be Full Width on Narrow Window (#406)
- Hotfix/FP-1332: Horz. Scrollbar Caused by Sections (#403)
- Hotfix/FP-1331: Do Not Hide Header Drodpowns (#404)
- Hotfix/FP-1330: Frontera: Fix Favicon Load on Standard Template (#401)
- Hotfix/FP-1333: Callout Title Color (#405)

## [3.3.0] - 2021-11-04: Brainmap Project; Fix Standard Template; Fix Header Links

### Added

- Quick: [v3.0.7] Changelog (#389, #390, #391)
- BM-5/BM-19: Add Brainmap Project (#393, #398)
- Quick: (for BM-19) New CSS Branding Logo Class (#392)
- task/FP-263: Add Frontera Favicon (update submodule) (#394)

### Changed

- Noop: Reduce verbosity of nested dropdown comment (#396)
- Noop: Fix Comment Typo & Move Styles Down Under It (#364)

### Fixed

- Bugfix/FP-1277: Extra Margin from Container by User on Standard Template (#370)
- FP-1235: Do not support dropdown menu text as link (#395)
- Hotfix: Fix Branding Links not Opening in New Window (#397)

## [3.0.7] - 2021-10-26: Hotfixes (mostly for Frontera); Rename Unused Component

### Changed

- task/FP-1260 Rename Component ReadMore to ShowMore (#376)

### Fixed

- FP-1270: Provide Header CSS that Only Docs Needs (#381)
- (UTRC) FP-1234: Add Missing Top Margin for Headings (#359)
- Quick: Complete Core fix for section header colors (#385)
- Hotfix: Local Images for Getting Started Guide (#369)
- `taccsite_custom`
  - Hotfix: Frontera: White Text for Home Banner H3's (#100)
  - Hotfix: Frontera: (UTRC-356) Homepage Banner Bkgd (x-overlay Mixin Syntax) (#386)

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
  - FP-1238/TACC/Core-CMS-Resources#68: Frontera: [...] Add Standard Template (TACC/Core-CMS-Resources#69)
  - Quick: Frontera: Save Newsletter Snippets (TACC/Core-CMS-Resources#63)
  - TACC/Core-CMS-Resources#70: ProTX & A2CPS: [...] Add Standard Template (TACC/Core-CMS-Resources#73)
  - FP-1217: New UTRC Logo (TACC/Core-CMS-Resources#83)
  - TACC/Core-CMS-Resources#191: ProTX: Support 'has-dark-logo' theme (TACC/Core-CMS-Resources#87)
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
  - FP-1238/TACC/Core-CMS-Resources#68: Frontera: Cleanup Templates [...] (TACC/Core-CMS-Resources#69)
  - Quick: Support & Move Snippets (TACC/Core-CMS-Resources#66)
  - TACC/Core-CMS-Resources#70: ProTX & A2CPS: Cleanup Templates [...] (TACC/Core-CMS-Resources#73)

### Fixed

- GH-283/GH-284: Fix Facebook Share Bug (Smaller TACC Logo) (#283)
- Hotfix/FP-1194: Use gettext_lazy Not gettext (fixed tup-cms deploy) (#344)
- FP-1234: Add Missing Top Margin for Headings (#359)
- Hotfix: (UTRC-356) Let Banner Section Padding Match Other Sections (#363, #368)
- Hotfix: (UTRC-356) Avoid Grid Blowout (#365, #368)
- Hotfix: (UTRC-356) Darker Core Body Text (#366, #368)
- Hotfix: Static Images for Getting Started Guide (#369)
- FP-1232: Fix Inconsistent Search Bar Icon Size (#371)
- `taccsite_custom`
  - TACC/Core-CMS-Resources#81: Fix Favicons Not Loading (TACC/Core-CMS-Resources#82)

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

[unreleased]: https://github.com/TACC/Core-CMS/compare/v3.19.0...HEAD
[3.19.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.19.0
[3.15.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.15.0
[3.14.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.14.0
[3.12.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.1
[3.5.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.5.1
[3.5.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.5.0
[3.3.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.3.0
[3.0.7]: https://github.com/TACC/Core-CMS/releases/tag/v3.0.7
[3.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.0.0
[2.5.2]: https://github.com/TACC/Core-CMS/releases/tag/v2.5.2
[2.1.1]: https://github.com/TACC/Core-CMS/releases/tag/v2.1.1
[2.1.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.1.0
[2.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.0.0
