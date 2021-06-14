# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.1.0] - 2021-06-14: Frontera Home Redesign; New Projects; New CSS Plugin; Bugfixes

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

[unreleased]: https://github.com/TACC/Core-CMS/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.1.0
[2.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v2.0.0
