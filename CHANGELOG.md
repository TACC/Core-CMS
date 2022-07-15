# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.7.12] - 2022-07-15: Fix Submodule Pointer

### Fixed

- chore(submod): use submod main commit for v3.7.11 (#516)

## [3.8.0] - 2022-07-14: Form Plugin, Document Release & NPM Link, Fix Banner

### Added

- feat(tup-308): working form plugin (aka tup-230) (#498)

### Changed

- docs(README): npm link instructions (#511)
- chore: author release process [...] (#514)

### Fixed

- fix(ecep-cms): global accent colors full suite
- fix(core-styles, frontera, utrc): fp-1723 section banner overflow mgmt (#513)

## [3.7.11] - 2022-07-06: v3.7.0 Fixes, New Core-Styles, ECEP/TUP/FP Tweaks

### Added

- Task/ecepweb-205-logos (#509)
- feat(frontera): accent color vars (d5748c9)
- TUP-271: [update to latest core-styles] (#495, #496, #489, #494, a49d9e7, d3f0a0b)

### Changed

- FP-1550: Document Custom Text in Admin UI (#467)
- feat(tup-151): center news articles (#488)
- chore(core-styles): build css via JS not CLI (#497)
- docs(README): [update npm link & core-styles] (981e7f9, ad0306b, a3a0acb, 4249f5b)

### Fixed

- Fix/v3.7.0 major bugs a.k.a. After/tup 271 (#507)
- fix(node): allow greater node & npm versions
- Bugfix/fp 1542 do not use a2cps url (#493)
- fix: load fa icons even if no portal (#504)

### Removed

- feat(tup): no LDAP (#499)

## [3.4.0-1-g0c5cbd1] - 2022-07-01: Support Annual Texascale Stylesheets]

### Added

- V3.4.0/fp 1439 yearly site theme for texascale (#508)

## [3.6.0-8-gd1dbcab] - 2022-06-23: Form Plugin UI Fixes, Add ADCP Resources Dir

### Added

- Update submodule to include APCD [...] (#502)

### Fixed

- V3.6.0/form plugin fixes (#501)

## [3.6.0-4-gb293de7] - 2022-06-21: Form Plugin

### Added

- feat(frontera): accent color vars (eb7c282)
- feat(v3.6.0): tup 230 make form plugin work (#500)

## [3.7.0] - 2022-05-13: Patterns, News/Blog App, SciVis & APCD, Improvements

### Added

- Quick: ECEP Custom Styles w/ Caveats (#478)
- Added the sciviscolor updates to the subrepo. (ba3a60f)
- ECEP-114: Members Page (Nav Pattern, Typography, Sticky Position) (#464, #481)
- ECEP-113: News/Blog (Core, ECEP, Texascale) (#466)
- Update submodule to include APCD (#486)

### Changed

- GH-149: Polish base.html markup (#151)
- Quick: Un-Deprecate Bootstrap Picture (#474)
- chore(tup-231): re-order and reduce comments (#484)
- Improve handling of missing custom settings (#485)
- docs(README): taccsite_custom clarity (4070121)
- docs(README): improve git submod use instructions (cb56b56)

### Fixed

- chore: fix typo in typography template (07fcb5c)
- TUP-231: Part 1 of N to Core-UI (Fix Core-CMS / Core-Styles Mismatch) (#482)
- Task/fp 1378 consistent space above footer (#480)

## [3.6.0] - 2022-04-15: CSS to Core-Styles, BM Logo Tweaks, Dependency Updates

### Changed

- FP-1496: CSS Build to Core-Styles (#448, c4e1a8ec, e5d4b2b, 8e2467e, 13f9833)
- BM-29/30: Brainmap Logo Tweaks (SGCI/UTHSCSA) (#476)

### Fixed

- Quick: Fix redirect_url so News Category Template Does Not Crash (81a01c1, 7afcef9)

### Removed

- Quick: Remove Unused JavaScript (#475)

### Security

- FP-1564: Update Core-CMS Dependencies (#471, 1eaccec, 00fa517)

## [3.5.2] - 2022-03-23: Fix v3.5.1 ProTX Bug

### Fixed

- Hotfix: Remove Old ProTX Templates from Its Settings (#470)

## [3.5.1] - 2022-03-23: Fix v3.5.0 Deploy Fail

### Fixed

- Hotfix/Resolve README CMS Deploy Fail (#469)

## [3.5.0] - 2022-03-17: Plugin Transfer, Classes; ECEP CMS; Fix v3.15, Safe ES

formerly known as v3.19.0 published on Thu Mar 17 10:58:00 2022 -0500

### Added

- Test: Install djangocms-transfer (#411)
- FP-1414: More Classnames for Django CMS Style Plugin (#419)
- GH-110: Add PR template (#454)
- `taccsite_cms`
    - Added [...] new ECEP portal CMS. (00eca44, 156a3d1)

### Changed

- FP-1461: Convert Core CMS to Poetry (#468)

### Fixed

- FP-1423: System Specs Layout Bug at Medium Width Screen (#444)
- FP-1341: Update README.md Since Settings Refactor (#417) 
- FP-1525: UTRC: Fix Homepage Whitespace (#447)
- FP-1359: Callout Plugin Active+Focus State Anomaly within Dark Section (#449)
- FP-1524: Section Pattern: [Fix] Extended Background (#446)
- FP-1470: Section Pattern: Third Style (and Fix to Dark Style) (#458)
- FP-1451: Open CMS External Links in New Window (Works on Portal) (#453)
- FP-1410: Shrink Guide Images & Add Links to Open in New Tab (https://github.com/TACC/Core-CMS/pull/462)

### Security

- FP-1540: Hotfix: Update ES to Fix Security Issue (#456)

## [3.4.0] - 2022-02-17: New Section Pattern; Critical Dependency Fix; Other

formerly known as v3.15.0 published on Wed Feb 16 15:32:04 2022 -0600

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

## [3.3.0] - 2022-01-25: Deprecate Callout Plugin; Guide Page Fix; Other Fixes

formerly known as v3.14.0 published on Tue Jan 25 21:38:47 2022 -0600

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

## [3.2.0] - 2021-12-21: BM Branding; UI Patterns; Search Bar Design; UTRC Font

formerly known as v3.12.1 published on Fri Dec 17 13:30:44 2021 -0600

### Added

- BM-22: BrainMap: Add UTHSC-SA Logo [and Remove SGCI Logo Text] (#414)
- FP-1289 Image Grid Pattern (#415)
- FP-1291: C-Recognition Pattern (#416)
- FP-1290: Card UI Pattern (Frontera About Page) (#420)

### Changed

- FP-1287: Redesign & Refactor Search Bar (#383)
- UTRC-357/FP-1268: Retire v1 Styles (Use v2 Styles) (#360)
- Quick: Move Code & Samp CSS from Site to Doc Page (#424)

## [3.1.1] - 2021-11-18: Remove Sentence from Getting Started Doc

formerly known as v3.5.1 published on Thu Nov 18 12:55:28 2021 -0600

### Fixed

- Quick: Remove sentence from Getting Started doc (#410)

## [3.1.0] - 2021-11-15: Navbar Toggle Color; OOTB Remote Login; v3.3.0 Fixes

formerly known as v3.5.0 published on Fri Nov 12 15:41:38 2021 -0600

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

## [3.0.2] - 2021-11-04: Brainmap Project; Fix Standard Template; Fix Header Links

formerly known as v3.3.0 published on Thu Nov 4 16:48:33 2021 -0500

### Added

- `taccsite_custom`
    - BM-5/BM-19: Add Brainmap Project (#393, #398)
    - Quick: (for BM-19) New CSS Branding Logo Class (#392)
    - task/FP-263: Add Frontera Favicon (update submodule) (#394)

### Changed

- Quick: [v3.0.7] Changelog (#389, #390, #391)
- Noop: Reduce verbosity of nested dropdown comment (#396)
- Noop: Fix Comment Typo & Move Styles Down Under It (#364)

### Fixed

- Bugfix/FP-1277: Extra Margin from Container by User on Standard Template (#370)
- FP-1235: Do not support dropdown menu text as link (#395)
- Hotfix: Fix Branding Links not Opening in New Window (#397)

## [3.0.1] - 2021-10-26: Hotfixes (mostly for Frontera); Rename Unused Component

formerly known as v3.0.7 published on Wed Oct 27 18:15:43 2021 -0500

### Changed

- (Noop) task/FP-1260 Rename Component ReadMore to ShowMore (#376)

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

## [2.2.0] - 2021-07-16: Fix Publish Bug; Texascale 2020; Polish

formerly known as v2.5.2 published on Thu Jul 1 16:10:38 2021 -0500

### Added

- GH-253: Initial Pattern Library Template & Styles (#25)
- Quick: Set Version & Add Changelog (#252)
- `taccsite_custom`
    - Major: Texascale 2020 (#256)

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

[unreleased]: https://github.com/TACC/Core-CMS/compare/v3.8.0...HEAD
[3.7.12]: https://github.com/TACC/Core-CMS/releases/tag/v3.7.12
[3.8.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.8.0s
[3.7.11]: https://github.com/TACC/Core-CMS/releases/tag/v3.7.11
[3.4.0-1-g0c5cbd1]: https://github.com/TACC/Core-CMS/releases/tag/v3.4.0-1-g0c5cbd1
[3.6.0-8-gd1dbcab]: https://github.com/TACC/Core-CMS/releases/tag/v3.6.0-8-gd1dbcab
[3.6.0-4-gb293de7]: https://github.com/TACC/Core-CMS/releases/tag/v3.6.0-4-gb293de7
[3.7.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.7.0
[3.6.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.6.0
[3.5.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.5.2
[3.5.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.5.1
[3.5.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.5.0
[3.4.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.4.0
[3.3.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.3.0
[3.2.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.2.0
[3.1.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.1.1
[3.1.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.1.0
[3.0.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.0.2
[3.0.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.0.1
[3.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.0.0
[2.2.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.2.0
[2.1.1]: https://github.com/TACC/Core-CMS/releases/tag/v2.1.1
[2.1.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.1.0
[2.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.0.0
