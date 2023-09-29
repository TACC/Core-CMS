# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased][unreleased]

...

## [4.0.0] - 2023-09-28: Django 3 & 4 Upgrade; New Features; New Styles

## Added

* feat: add djangocms_tacc_image_gallery by @wesleyboar in https://github.com/TACC/Core-CMS/pull/654
* feat: core-styles v2.9.1 to v2.11.0 by @wesleyboar in https://github.com/TACC/Core-CMS/pull/671
* feat(dev/tup-cms): django3, blog/news styles + related patterns by @wesleyboar in https://github.com/TACC/Core-CMS/pull/581
* Update Django to v3.2 by @jarosenb in https://github.com/TACC/Core-CMS/pull/625
* feat: v3.12.0-alpha.10 by @wesleyboar in https://github.com/TACC/Core-CMS/pull/675
* feat: add instagram, hide twitter by @wesleyboar in https://github.com/TACC/Core-CMS/pull/680
* enhance: improve admin UI permissions error text by @wesleyboar in https://github.com/TACC/Core-CMS/pull/693
* feat(management): text & media editor groups by @wesleyboar in https://github.com/TACC/Core-CMS/pull/600
* feat: texascale, cms v3.12.0 beta by @wesleyboar in https://github.com/TACC/Core-CMS/pull/713
* feat: social media quick share links (inactive) by @wesleyboar in https://github.com/TACC/Core-CMS/pull/711
* Bump Django version to 4.2 by @jarosenb in https://github.com/TACC/Core-CMS/pull/707
* feat: restore css and js blocks by @wesleyboar in https://github.com/TACC/Core-CMS/pull/716

## Fixed

* fix(css): anchor around image not supporting margin by @wesleyboar in https://github.com/TACC/Core-CMS/pull/670
* fix: render/style responsive video/audio player (…) by @wesleyboar in https://github.com/TACC/Core-CMS/pull/685
* fix: do not serve ui demo unless it exists by @wesleyboar in https://github.com/TACC/Core-CMS/pull/688
* fix: serve ui demo if it exists by @wesleyboar in https://github.com/TACC/Core-CMS/pull/692
* hotfix: set SESSION_COOKIE_SECURE = True by @rstijerina in https://github.com/TACC/Core-CMS/pull/695
* fix: our dev dependencies are actually for prod by @wesleyboar in https://github.com/TACC/Core-CMS/pull/708
* fix: ui demo for core and clients by @wesleyboar in https://github.com/TACC/Core-CMS/pull/706

## Documented

* docs: simpler readme + add small docs by @wesleyboar in https://github.com/TACC/Core-CMS/pull/665
* docs: paper trail for v3-10_v3-11/ (…) by @wesleyboar in https://github.com/TACC/Core-CMS/pull/682
* docs: fix broken link (customize admin ui text) by @wesleyboar in https://github.com/TACC/Core-CMS/pull/694
* docs: manage styles and scripts by @wesleyboar in https://github.com/TACC/Core-CMS/pull/717
* hotfix: turn off github pages for now by @wesleyboar in https://github.com/TACC/Core-CMS/pull/722

**Full Changelog**: https://github.com/TACC/Core-CMS/compare/v3.11.6...v4.0.0

## [3.12.0-beta.5] - 2023-09-28: Revert Django 4 Upgrade

> **Warning**
> To use this release, ensure your [CMS project is upgraded](https://github.com/TACC/Core-CMS-Resources/blob/ca1366b/docs/upgrade-project.md).

### Fixed

* Revert "Bump Django version to 4.2 (#707)" (467a327)

## [3.12.0-beta.4] - 2023-09-27:  Django 4 Upgrade plus Misc. Features

> **Warning**
> To use this release, ensure your CMS project database uses Postgres v14.9.

> **Warning**
> To use this release, ensure your [CMS project is upgraded](https://github.com/TACC/Core-CMS-Resources/blob/ca1366b/docs/upgrade-project.md).

### Added

* feat: restore css and js blocks (#716)
* Bump Django version to 4.2 (#707)
* feat: social media quick share links (inactive) (#711)
* feat(management): text & media editor groups (#600)
* feat: texascale, cms v3.12.0 beta (#713)
* feat(taccsite_custom): neuronex-cms→_3dem_cms@3.12 (479ea0c)

## Documentation

* docs: [miscellaneous] (bea4943, bd7064b, 808fb14, 502fa3a, f1af7ad, 842cb66)

### Fixed

* Revert "feat: do not let news editors add plain images (#691)" (#715)

## [3.12.0-beta.3] - 2023-08-28: Fix UI Demo (For Real)

> **Warning**
> To use this release, ensure your [CMS project is upgraded](https://github.com/TACC/Core-CMS-Resources/blob/ca1366b/docs/upgrade-project.md).

### Fixed

* fix: our dev dependencies are actually for prod (#708)
* fix: ui demo for core and clients (#706)

## [3.12.0-beta.2] - 2023-08-22: Re-Sync taccsite_custom Pointer

> **Warning**
> To use this release, ensure your [CMS project is upgraded](https://github.com/TACC/Core-CMS-Resources/blob/ca1366b/docs/upgrade-project.md).

> **Warning**
> The UI demo will **not** load. Failed in [TACC/tup-ui#301](https://github.com/TACC/tup-ui/pull/301).

### Fixed

* fix(taccsite_custom): point submodule to main (1775c45)

## [3.12.0-beta.1] - 2023-08-22: ⚠️ Set `SESSION_COOKIE_SECURE = True`, Fix UI Demo

> **Warning**
> Unable to build. Use https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-beta.2 instead.

> **Warning**
> The UI demo is **not** successfully fixed by #692.

### Fixed

* ~~fix: serve ui demo if it exists (#692)~~
* hotfix: set SESSION_COOKIE_SECURE = True (#695)
* docs: fix broken link (customize admin ui text) (#694)

### Changed

* feat: do not let news editors add plain images (#691)
* chore(taccsite_custom): delete migrated cms's (#690)
* enhance: improve admin UI permissions error text (#693)

## [3.11.6] - 2023-08-22: Set `SESSION_COOKIE_SECURE = True`

### Fixed

* fix(taccsite_custom): wrong pointer in v3.11.3 (#668)

## [3.9.5] - 2023-08-22: Set `SESSION_COOKIE_SECURE = True`

### Fixed

* hotfix: set SESSION_COOKIE_SECURE = True (off of v3.9.4) (#702)

## [3.9.4] - 2023-08-22: Approx. Retroactive APCD-CMS Nov 2022 Release

> **Note**
> This is an attempt to tag the CMS as of the [most recent prod. deploy](https://github.com/TACC/Core-Portal-Deployments/commit/d82170a) of [APCD at `3a439bad`](https://github.com/TACC/Core-CMS-Custom/blob/3a439bad/apcd-cms/Dockerfile#L1) with [TACC/Core-CMS at #567](https://github.com/TACC/Core-CMS/pull/567) plus v3.9.3's #643.

### All

* fix(ckeditor): text editor opens too slow (#643)
* feat(core-styles): v0.10.0 (#567)
* feat: fp-1837 limit nav menu item visibility by group (#566)
* feat(taccsite-cms): demdata-cms, old build solution (#564)
* feat(css): fp-1828 move apcd styles to core (#565)
* chore(core-styles): tup-293 dependency updates (#563)
* feat: fp-1500 serve ui pattern lib (as static files) (#562)
* fix: tup-340 portal nav not loading (#561)
* fix(css): fp-1791 button auto width & django cms form button tweak (#560)
* docs(readme): update INCLUDES_ setting gotchas (83c19245)
* docs(example-cms): add new INCLUDES_ settings (88773a09)
* chore: latest core-cms-resources & core-styles v0.9.0 (#559)
* chore: fp-1903 sync tup-ui login component changes to core-styles (#531)
* feat: tup-340 allow include portal nav and/or search bar via settings (#557)
* Task/FP-1854 - Add RT package and update poetry version (#558) (like #602)
* feat(taccsite_custom): BM-26 new logo and favicon (#556)
* docs(README): Core CMS Resources v Core CMS Custom (be110b09)
* docs(changelog): v3.9.1 missing sub-title (ff737a3f)
* fix(core-styles): v0.8.7 (path fix) (f33957e6)

## [3.12.0-alpha.12] - 2023-08-18: Fix Core-CMS-Custom Support

> **Warning**
> To use this release, ensure your [CMS project is upgraded](https://github.com/TACC/Core-CMS-Resources/blob/ca1366b/docs/upgrade-project.md).

### Fixed

* fix: do not serve ui demo unless it exists (#688)
* fix: render/style responsive video/audio player (off of main) (#685)

### Changed

* docs: paper trail for v3-10_v3-11/ (off of main) (#682)
* chore: the LinkedIn link should be https (e6d5cc4d)
* feat: add instagram, hide twitter (#680)
* docs: cms admin uses ad hoc styles, so can tacc (#679)
* style: remove extra letters in changelog (c14fe36e)

## [3.11.5] - 2023-08-15: Document `v3-10_v3-11`, Fix Responsive Video Player

### Fixed

* docs: paper trail for v3-10_v3-11/ (#681)
* fix: render/style responsive video/audio player (#684)

## [3.12.0-alpha.11] - 2023-07-25: Fix v3.12.0-alpha.10 Crash (Incomplete)

> **Warning**
> This does not fix all custom projects.
> - [It fixes only **some** projects.](https://github.com/TACC/Core-CMS/pull/676)
> - [It documents **how to fix** others.](https://github.com/TACC/Core-CMS-Resources/blob/ca1366b/docs/upgrade-project.md)
> - [It does **not** work on TACC/Core-CMS-Custom.](https://github.com/TACC/Core-CMS-Custom/pull/175)

### Fixed

* fix: v3.12.0-alpha.10 crash (ignore docs, add redirects) (#676)

## [3.12.0-alpha.10] - 2023-07-18: ⚠️ Conditional Blog/News Markup, Better README

> **Warning**
> Websites deployed with this return 500 error. Use [3.12.0-alpha.11] instead.

### Fixed

* fix(dev/tup-cms): blog/news markup (bugs found on ecep) #674

### Changed

* Update Django to v3.2 (#625) (#581)
* feat(dev/tup-cms): django3, blog/news styles + related patterns (#581)
* docs: simpler readme + add small docs (#665)

## [3.12.0-alpha.9] - 2023-07-13: Remove Migrated Projects from Submodule

## Removed

* chore(taccsite_custom): remove migrated projects (afb6f21)

## [3.12.0-alpha.8] - 2023-07-13: Re-Sync dev/tup-cms, main, taccsite_custom

### Fixed

* re-sync `dev/tup-cms` and `main` and their submodule pointers

## [3.12.0-alpha.7] - 2023-07-12: Core-Styles v2.9.1 to v2.11.0

### Added

* feat: core-styles v2.9.1 to v2.11.0 (#671)

## [3.12.0-alpha.6] - 2023-07-12: Display a.img-fluid as Inline Block

### Fixed

* fix(css): anchor around image not supporting margin (#670) (7b51038)

### Removed

* chore(taccsite_custom): delete acpd-cms dir (c615079)
* chore(taccsite_custom): delete tup-cms dir (fa3c101)
* chore(taccsite_custom): delete demdata (#666)

## [3.12.0-alpha.5] - 2023-06-22: Remove demdata-cms, Merge v3.11.3

### Added

* feat: v3.11.3 (#664)

### Changed

* feat: add djangocms_tacc_image_gallery (#654)[^1]
* feat(taccsite_custom): demdata-cms, css from tup (#606)

---

[^1]: Already available since https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.3 and https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.4 but now it comes officially from the trunk.

## [3.12.0-alpha.4] - 2023-06-16: Gallery Updates, Style Fixes, taccsite_custom Update

### Added

* feat: s-image-grid → lightgallery (#663)

### Changed

* feat(taccsite_custom): explicit source css imports (7f25379)

### Fixed

* fix: update [image gallery] plugin to v0.1.3 (1358d36)
* fix(core-styles): v2.9.1 (4894e4f)
* fix(taccsite_custom): brainmap logo missing text (7cda385)

## [3.12.0-alpha.3] - 2023-06-15: Install Image Gallery Plugin

### Added

* feat: add djangocms_tacc_image_gallery (un-styled) (#654)

## [3.12.0-alpha.2] - 2023-06-15: Fix v3.10 Accent Color From Purple Back to Blue

### Fixed

* feat(css): accent color from purple to blue (#660)
* fix(css): bump text editor css core-styles to v2.9 (#661)

## [3.12.0-alpha.1] - 2023-06-14: Django 3; Redesign Blog/News + Related Patterns

### Added

* feat: styles v2.9.0 → s-image-grid → lightgallery (#655)
* feat(css): figure, caption, etc styles; whole site (#624)
* feat(css): migrate tup-cms styles to core-cms (part 2) (#620)
* feat(css): migrate tup-cms styles to core-cms (part 1) (#616)
* Task/tup 395 cmd news styles from tup cms (#612)
* feat(core-styles): change accent color from purple to blue (#617)
* feat: tup-398, improve blog css & layout toggle (#613)
* feat(djangocms_blog): simple article link & "to be published" (#599)
* feat(blog): tup-395, styles (#587)
* feat: auto-responsive video embed (#590)
* Task/tup 395 cmd news layout switch (#589)
* feat(core-styles): base, cms, docs, portal re-org (#586)

### Changed

* Update to Django 3.2 (for TUP CMS) (#626)
* chore: load static not staticfiles (#629)
* chore(core-styles): tup-cms table updates (#603)

### Fixed

* Bugfix/news tags all black (#622)
* fix: add+use core-styles.wysiwyg.css not copied code (#618)
* fix: portal nav not to touch cms menu if no search (#615)
* fix(templates): djangcms_picture, alignment issues (#588)

## [3.11.4] - 2023-07-11: Fix v3.11.3 Bad Submodule Pointer (taccsite_custom)

### Fixed

* fix(taccsite_custom): wrong pointer in v3.11.3 (#668)

## [3.11.3] - 2023-06-16: ⚠️ CSS Import Paths, Brainmap Logo, Core-Styles v2.9.1

> **Warning**
> This accidentally breaks all https://github.com/TACC/Core-CMS-Resources projects.
> Use https://github.com/TACC/Core-CMS/releases/tag/v3.11.4 or greater instead.

### Changed

* feat(taccsite_custom): explicit source css imports (7f25379)

### Fixed

* fix(core-styles): v2.9.1 (4894e4f)
* fix(taccsite_custom): brainmap logo missing text (7cda385)

## [3.11.2] - 2023-06-15: Fix Accent Color From Purple Back to Blue

### Fixed

* feat(css): accent color from purple to blue (#660)
* fix(css): bump text editor css core-styles to v2.9 (#661)

## [3.11.1] - 2023-06-13: Do Not Assign Non-Existent Color Variable

### Fixed

* fix: unreleased link to main not head (8bd1c58)
* fix: v3.11.0 css overwrite by non-existent color (#658)

## [3.11.0] - 2023-06-12: Optional Core-Styles v2, Open New Window Script Feat's

### Added

* feat(core-styles): v2 (#569) (5e32c8a)
* feat: poetry 1.4.0 (#653) (a98dfe1)
* feat(js): DES-2496 auto new tab, regex + callbacks (#651) (3e448cc)

### Fixed

* fix: taccsite_system_monitor is not deprecated (301c7cf)
* chore(settings): fix inaccurate comment (2e80a70)
* docs(CHANGELOG): formatting of 3.10.2 changes (5f07c9e)

## [3.11.0-beta.2] - 2023-05-23: Core-Styles v2 Backwards-Compatible

### Added

* feat(core-styles): v2 (#569) + support CMS that needs v0 (#605)

### Fixed

* fix(tup-cms): make search field required input (#646)
* chore(taccsite_custom): main after merge (f3994b3)

## [3.11.0-beta.1] - 2023-05-22: Core-Styles v2 Backwards-Compatible

### Added

* feat(core-styles): v2 (#569) + support CMS that needs v0 (#605)

## [3.11.0-alpha.1] - 2023-06-02: Open New Window Script Regex and Callback

### Added

* feat(js): DES-2496 auto new tab, regex + callbacks (#651)

## [3.10.2] - 2023-06-01: Require Search Input, Fix Override of New Window Open

### Fixed

* fix(templates): bump home_portal `<hN>` levels (#640)
* fix(brainmap-cms): #556 missing items from #570 (#645)
* fix(tup-cms): make search field required input (#646)
* chore(deps): bump socket.io-parser from 4.2.1 to 4.2.3 (#647)
* fix(js): DES-2498 auto new window ignores redirect by (#649)

## [3.10.1] - 2023-05-10: Fixes for Core-CMS v3.10 and ProTX CMS v3.9

### Fixed

* fix(css): add missing theme vars (#634)
* bugfix: security for example-cms docker compose (#627)
* fix: (protx-cms) getting-started <hN> levels (f2efa45)
* fix: (frontera) system_monitor colors (#635)
* fix(taccsite_custom): wrong commit pointer (31a2e7e)

## [3.10.0] - 2023-05-08: Example, WYSIWYG, DemData, Icons, 404, SVGs, Query

### Added

* Task/update example cms defaults (#577)
* feat(settings): wysiwyg customization (#595)
* Pulled in DemData site resources. (a88925d)
* feat(djangocms_icon): support cortal font & svg logos (#611)
* feat: minimal 404 error page (ea034fc) (95aefe1)
* feat: svg logos, branding & social, plus templates (#608)
* feat(img): social media logo svgs (1a90e16)
* feat(settings): tup-437, SEARCH_QUERY_PARAM_NAME (#604)

### Changed

* chore(core-styles): v0.13.0 (b462ea2)
* chore: retire env()-based themes (Core-CMS v3.9) (#632)
* chore(settings): tacc search above elasticsearch (a54bd43)
* chore(settings): most of elasticsearch in one spot (e03418f)
* docs(management): create "User groups (page)" first (2b222c2)
* chore(taccsite_cms): texascale, robots.txt status (b22aaa8)
* docs: improve release process steps

### Fixed

* fix(texascale): restore pre-v3.9.1 heading styles (5934b2e)
* fix: explicit INCLUDES_PORTAL_NAV & …_SEARCH_BAR (01d2505)
* fix: portal nav not to touch cms menu if no search (#614)
* fix(bin): console log undefined to real array (7dbab46)
* fix: pattern demo repair suite (#568)
  * changes default accent from blue to purple (fe3c242)

## [3.9.3] - 2023-05-12: Fix Text Editor Opening Too Slow

### Fixed

* fix(ckeditor): text editor opens too slow (#643)

## [3.9.2] - 2023-02-14: Poetry URL & Version (Hotfix)

### Fixed

* fix: poetry install url & version (#602)

## [3.9.1] - 2022-09-16: Core Styles v0.8.7 (Hotfix)

### Fixed

* fix(core-styles): v0.8.7 (path fix) (f33957e)

## [3.9.0] - 2022-09-14: Custom Apps, A11y, UI Demo, Logging, Docs, Fixes

### Added

* Support custom apps through config. (#517)
* Task/ecepweb 210 members pages accessibility (#528)
* Task/ecepweb 209 news pages accessibility (#529)
* Task/ecepweb 209 news pages responsive design (#530)
* feat: fp-1736 allow form to send email (#536, #550)
* Task/fp 1499 ui pattern demo (#527)
* chore: fp-1778 apcd assets from Core-CMS-Resources (#543)
* task/FP-1780 -- core cms logging (#544)
* add ipython to django shell (#542)
* feat: ecep-215 o-float-content--left|right (#534)
* chore(ecep): archive and add page members snippets (9c6d5e4)
* FP-1790: apcd, favicon & fake logo (#547)
* feat(ecep): ecep-214 safe emails in content (#546)
* feat(core-styles): install 0.8.6 (#553)

### Changed

* chore(css): update docs & comments (#525)
* chore(ecep): hide news byline (ebfc9df, #519)
* docs: [miscellaneous] (d344b5d, cdcd9e1, 775429c, fa126ce, af2ef90, e4bf7ae)
* docs: add settings_local.example.py (#539)
* TUP-321: Make it Clearer How to Disable LDAP Settings (#537)
* feat(bm): FP-1798 link logo to home not ext site (94a17b3)

### Fixed

* fix(templates): programatic current year in footer (#538)
* Fix/tup 151 news article fixes and tweaks (#523)
* fix(django): implement djangocms-text-ckeditor#568 (#540, #541)
* fix: fp-1782 form plugin file upload (#545)
* Task/fp 1801 guides breadcrumbs headings (#549)
* Bug/fp 1798 external nav link (still) not open in new window (#548)
* feat(css): warn user of unsupported form field (#551)

## [3.8.2] - 2022-11-16: New BrainMap Logo URL & Accent Colors

### Changed

* feat(taccsite_custom): bm-41 new logo (off of cms v3.8.1) (#570)

## [3.8.1] - 2022-08-26: Change BrainMap Logo URL to Hoem Page not Ext. Page

### Changed

* feat(bm): FP-1798 link logo to home not ext site (0bf5e12)

## [3.7.12] - 2022-07-15: Fix Submodule Pointer

### Fixed

* chore(submod): use submod main commit for v3.7.11 (#516)

## [3.8.0] - 2022-07-14: Form Plugin, Document Release & NPM Link, Fix Banner

### Added

* feat(tup-308): working form plugin (aka tup-230) (#498)

### Changed

* docs(README): npm link instructions (#511)
* chore: author release process [...] (#514)

### Fixed

* fix(ecep-cms): global accent colors full suite
* fix(core-styles, frontera, utrc): fp-1723 section banner overflow mgmt (#513)

## [3.7.11] - 2022-07-06: v3.7.0 Fixes, New Core-Styles, ECEP/TUP/FP Tweaks

### Added

* Task/ecepweb-205-logos (#509)
* feat(frontera): accent color vars (d5748c9)
* TUP-271: [update to latest core-styles] (#495, #496, #489, #494, a49d9e7, d3f0a0b)

### Changed

* FP-1550: Document Custom Text in Admin UI (#467)
* feat(tup-151): center news articles (#488)
* chore(core-styles): build css via JS not CLI (#497)
* docs(README): [update npm link & core-styles] (981e7f9, ad0306b, a3a0acb, 4249f5b)

### Fixed

* Fix/v3.7.0 major bugs a.k.a. After/tup 271 (#507)
* fix(node): allow greater node & npm versions
* Bugfix/fp 1542 do not use a2cps url (#493)
* fix: load fa icons even if no portal (#504)

### Removed

* feat(tup): no LDAP (#499)

## [3.4.0-1-g0c5cbd1] - 2022-07-01: Support Annual Texascale Stylesheets]

### Added

* V3.4.0/fp 1439 yearly site theme for texascale (#508)

## [3.6.0-8-gd1dbcab] - 2022-06-23: Form Plugin UI Fixes, Add ADCP Resources Dir

### Added

* Update submodule to include APCD [...] (#502)

### Fixed

* V3.6.0/form plugin fixes (#501)

## [3.6.0-4-gb293de7] - 2022-06-21: Form Plugin

### Added

* feat(frontera): accent color vars (eb7c282)
* feat(v3.6.0): tup 230 make form plugin work (#500)

## [3.7.0] - 2022-05-13: Patterns, News/Blog App, SciVis & APCD, Improvements

### Added

* Quick: ECEP Custom Styles w/ Caveats (#478)
* Added the sciviscolor updates to the subrepo. (ba3a60f)
* ECEP-114: Members Page (Nav Pattern, Typography, Sticky Position) (#464, #481)
* ECEP-113: News/Blog (Core, ECEP, Texascale) (#466)
* Update submodule to include APCD (#486)

### Changed

* GH-149: Polish base.html markup (#151)
* Quick: Un-Deprecate Bootstrap Picture (#474)
* chore(tup-231): re-order and reduce comments (#484)
* Improve handling of missing custom settings (#485)
* docs(README): taccsite_custom clarity (4070121)
* docs(README): improve git submod use instructions (cb56b56)

### Fixed

* chore: fix typo in typography template (07fcb5c)
* TUP-231: Part 1 of N to Core-UI (Fix Core-CMS / Core-Styles Mismatch) (#482)
* Task/fp 1378 consistent space above footer (#480)

## [3.6.0] - 2022-04-15: CSS to Core-Styles, BM Logo Tweaks, Dependency Updates

### Changed

* FP-1496: CSS Build to Core-Styles (#448, c4e1a8ec, e5d4b2b, 8e2467e, 13f9833)
* BM-29/30: Brainmap Logo Tweaks (SGCI/UTHSCSA) (#476)

### Fixed

* Quick: Fix redirect_url so News Category Template Does Not Crash (81a01c1, 7afcef9)

### Removed

* Quick: Remove Unused JavaScript (#475)

### Security

* FP-1564: Update Core-CMS Dependencies (#471, 1eaccec, 00fa517)

## [3.5.2] - 2022-03-23: Fix v3.5.1 ProTX Bug

### Fixed

* Hotfix: Remove Old ProTX Templates from Its Settings (#470)

## [3.5.1] - 2022-03-23: Fix v3.5.0 Deploy Fail

### Fixed

* Hotfix/Resolve README CMS Deploy Fail (#469)

## [3.5.0] - 2022-03-17: Plugin Transfer, Classes; ECEP CMS; Fix v3.15, Safe ES

formerly known as v3.19.0 published on Thu Mar 17 10:58:00 2022 -0500

### Added

* Test: Install djangocms-transfer (#411)
* FP-1414: More Classnames for Django CMS Style Plugin (#419)
* GH-110: Add PR template (#454)
* `taccsite_cms`
  * Added [...] new ECEP portal CMS. (00eca44, 156a3d1)

### Changed

* FP-1461: Convert Core CMS to Poetry (#468)

### Fixed

* FP-1423: System Specs Layout Bug at Medium Width Screen (#444)
* FP-1341: Update README.md Since Settings Refactor (#417) 
* FP-1525: UTRC: Fix Homepage Whitespace (#447)
* FP-1359: Callout Plugin Active+Focus State Anomaly within Dark Section (#449)
* FP-1524: Section Pattern: [Fix] Extended Background (#446)
* FP-1470: Section Pattern: Third Style (and Fix to Dark Style) (#458)
* FP-1451: Open CMS External Links in New Window (Works on Portal) (#453)
* FP-1410: Shrink Guide Images & Add Links to Open in New Tab (https://github.com/TACC/Core-CMS/pull/462)

### Security

* FP-1540: Hotfix: Update ES to Fix Security Issue (#456)

## [3.4.0] - 2022-02-17: New Section Pattern; Critical Dependency Fix; Other

formerly known as v3.15.0 published on Wed Feb 16 15:32:04 2022 -0600

### Added

* FP-1318: Create Section Pattern via Style Plugin (#430)

### Changes

* Quick: (Texascale) Do Not Let Search Engines Index 2022 Pages (#443)
* FP-1318: Revisit Section Pattern (#433)

### Fixed

* FP-1502: Fix Callout Title Height (#441)

### Removed

* UTRC-357/FP-1268: (UTRC) Remove old templates (#439)

### Security

* FP-1285: CMS Critical Dependency Upgrade (#437)

## [3.3.0] - 2022-01-25: Deprecate Callout Plugin; Guide Page Fix; Other Fixes

formerly known as v3.14.0 published on Tue Jan 25 21:38:47 2022 -0600

### Added

* FP-1415: Callout Pattern with Fixes sans Plugin (#427)
  * Callout Plugin - Crop Images within Ratio (GH-329)

### Changed

* FP-1417: Callout CSS to Style Child Elements via Tag not Class (#425)
* FP-1416: Callout Image Resize w/ JS not CSS (#421) (#422)

### Fixed

* FP-1422: (UTRC) Remove White Border Under Header (#435)
* FP-1418: Callout Link Clickable Area Fix (#423)
* FP-1416: Callout Image Resize w/ CSS not JS (#421) (#422)
  * Callout Plugin - Fix Image Resize Caveat (GH-327)
  * Element Transform Fails on Child Plugin Markup w/out Hack (GH-320)
* FP-1435: Updates on Getting Started page (#428)
* FP-1408: (Frontera) Fix Clickable Area of Article List Link (#429)
* Remove a "Task/" from CHANGELOG entry (d773289)
* Minor: Fix: x-layout CSS docblock typo (#434)

### Removed

* Deleted `resize_figure_to_fit` feature of Callout Plugin. (#421) (#422)
* Deleted `elementTransformer` module and `SizeContentToFit` class. (#421)

### Deprecated

* Callout Plugin is unsupported. Replace with Callout Pattern. (#427)
* Marked README.md as outdated & added link to new draft. (61b310b)

## [3.2.0] - 2021-12-21: BM Branding; UI Patterns; Search Bar Design; UTRC Font

formerly known as v3.12.1 published on Fri Dec 17 13:30:44 2021 -0600

### Added

* BM-22: BrainMap: Add UTHSC-SA Logo [and Remove SGCI Logo Text] (#414)
* FP-1289 Image Grid Pattern (#415)
* FP-1291: C-Recognition Pattern (#416)
* FP-1290: Card UI Pattern (Frontera About Page) (#420)

### Changed

* FP-1287: Redesign & Refactor Search Bar (#383)
* UTRC-357/FP-1268: Retire v1 Styles (Use v2 Styles) (#360)
* Quick: Move Code & Samp CSS from Site to Doc Page (#424)

## [3.1.1] - 2021-11-18: Remove Sentence from Getting Started Doc

formerly known as v3.5.1 published on Thu Nov 18 12:55:28 2021 -0600

### Fixed

* Quick: Remove sentence from Getting Started doc (#410)

## [3.1.0] - 2021-11-15: Navbar Toggle Color; OOTB Remote Login; v3.3.0 Fixes

formerly known as v3.5.0 published on Fri Nov 12 15:41:38 2021 -0600

### Added

* COOKS-108: Navbar Toggler Icon Color [per Theme] (#402)

### Changed

* Update settings.py: Haystack Connection INDEX_NAME (#374)
* Update settings.py: CEP_AUTH_VERIFICATION_ENDPOINT (#375)

### Fixed

* COOKS-108: Navbar Toggler Icon Color [Fix for "Has Dark Logo" Theme] (#402)
* Hotfix/FP-1234: Texascale: Remove Category Page Title Margin Top (#388)
* Hotfix/FP-1338: Offset Content to be Full Width on Narrow Window (#406)
* Hotfix/FP-1332: Horz. Scrollbar Caused by Sections (#403)
* Hotfix/FP-1331: Do Not Hide Header Drodpowns (#404)
* Hotfix/FP-1330: Frontera: Fix Favicon Load on Standard Template (#401)
* Hotfix/FP-1333: Callout Title Color (#405)

## [3.0.2] - 2021-11-04: Brainmap Project; Fix Standard Template; Fix Header Links

formerly known as v3.3.0 published on Thu Nov 4 16:48:33 2021 -0500

### Added

* `taccsite_custom`
  * BM-5/BM-19: Add Brainmap Project (#393, #398)
  * Quick: (for BM-19) New CSS Branding Logo Class (#392)
  * task/FP-263: Add Frontera Favicon (update submodule) (#394)

### Changed

* Quick: [v3.0.7] Changelog (#389, #390, #391)
* Noop: Reduce verbosity of nested dropdown comment (#396)
* Noop: Fix Comment Typo & Move Styles Down Under It (#364)

### Fixed

* Bugfix/FP-1277: Extra Margin from Container by User on Standard Template (#370)
* FP-1235: Do not support dropdown menu text as link (#395)
* Hotfix: Fix Branding Links not Opening in New Window (#397)

## [3.0.1] - 2021-10-26: Hotfixes (mostly for Frontera); Rename Unused Component

formerly known as v3.0.7 published on Wed Oct 27 18:15:43 2021 -0500

### Changed

* (Noop) task/FP-1260 Rename Component ReadMore to ShowMore (#376)

### Fixed

* FP-1270: Provide Header CSS that Only Docs Needs (#381)
* (UTRC) FP-1234: Add Missing Top Margin for Headings (#359)
* Quick: Complete Core fix for section header colors (#385)
* Hotfix: Local Images for Getting Started Guide (#369)
* `taccsite_custom`
  * Hotfix: Frontera: White Text for Home Banner H3's (#100)
  * Hotfix: Frontera: (UTRC-356) Homepage Banner Bkgd (x-overlay Mixin Syntax) (#386)

## [3.0.0] - 2021-10-18: Refactor Settings; New Sites & Plugins; v1 CSS; Themes

### Added

* Quick: A2CPS [Site] (#271, #272, #380)
* GH-245/FP-1097: v1–v2 Migration Stylesheet (#274)
* GH-73: Blockquote, Offset [...] Plugins (#275)
* Quick: Support Non-Bootstrap Link & Picture Plugins (#278)
* FP-1097: A2CPS: Add Snippets (#288)
* GH-89: (Minimal) System Monitor Plugin (a.k.a. SysMon) (#297)
* GH-298: Add "See All" Link Component (#300)
* Quick: Support Snippets & Add 1 Useful Snippet (#301)
* GH-75: Data List - Styles / Component / Plugin (#305, #308, #326, #336)
* GH-310: Breadcrumbs [...] (#311)
* GH-310: [...] Standard Template (#311)
* GH-98: Typography (#312, #314, #316, #318)
* GH-83: Callout Plugin (#324)
* GH-88: System Specs Plugin (#323, #330)
* UTRC-356: New UTRC [...] (#367, #368, TACC/Core-CMS-Resources#80)
* Quick: (UTRC-356) Add CSS Mixins for "Overlay" (#362, #368)
* GH-191: Theme (for ProTX Light Header & TACC Blue Header) (#192)
* `taccsite_custom`
  * FP-1238/TACC/Core-CMS-Resources#68: Frontera: [...] Add Standard Template (TACC/Core-CMS-Resources#69)
  * Quick: Frontera: Save Newsletter Snippets (TACC/Core-CMS-Resources#63)
  * TACC/Core-CMS-Resources#70: ProTX & A2CPS: [...] Add Standard Template (TACC/Core-CMS-Resources#73)
  * FP-1217: New UTRC Logo (TACC/Core-CMS-Resources#83)
  * TACC/Core-CMS-Resources#191: ProTX: Support 'has-dark-logo' theme (TACC/Core-CMS-Resources#87)
  * [Texascale: Load Blog a.k.a.] Hotfix: Texascale: Post-FP-1194 Fix (Restore Blog) (#95)

### Changed

* GH-73: [Update Sample Plugin to be Consistent with other Plugins] (#275)
* Quick: Support Variable in x-truncate CSS (#304)
* Quick: GH-253: Tweak Style Guide CSS (#325, #326)
* GH-331: Cleanup Fullwidth Template (#332)
* [Major: Split Settings and Secrets] (#341, #345, #347, #348, TACC/Core-CMS-Resources#77)
* [Quick: Add UTRC Site] (#345, #357)
* [FP-1194: Synchronize User Login between Core Portal and CMS] (#341, #346, #356)
* Quick: (UTRC-356) Migrate Banner Overlay Styles from Core (to Frontera) (#361, #368)
* `taccsite_custom`
  * FP-1238/TACC/Core-CMS-Resources#68: Frontera: Cleanup Templates [...] (TACC/Core-CMS-Resources#69)
  * Quick: Support & Move Snippets (TACC/Core-CMS-Resources#66)
  * TACC/Core-CMS-Resources#70: ProTX & A2CPS: Cleanup Templates [...] (TACC/Core-CMS-Resources#73)

### Fixed

* GH-283/GH-284: Fix Facebook Share Bug (Smaller TACC Logo) (#283)
* Hotfix/FP-1194: Use gettext_lazy Not gettext (fixed tup-cms deploy) (#344)
* FP-1234: Add Missing Top Margin for Headings (#359)
* Hotfix: (UTRC-356) Let Banner Section Padding Match Other Sections (#363, #368)
* Hotfix: (UTRC-356) Avoid Grid Blowout (#365, #368)
* Hotfix: (UTRC-356) Darker Core Body Text (#366, #368)
* Hotfix: Static Images for Getting Started Guide (#369)
* FP-1232: Fix Inconsistent Search Bar Icon Size (#371)
* `taccsite_custom`
  * TACC/Core-CMS-Resources#81: Fix Favicons Not Loading (TACC/Core-CMS-Resources#82)

### Removed

* `taccsite_custom`
  * GH-89: Remove SysMon Snippet (TACC/Core-CMS-Resources#67)

## [2.2.0] - 2021-07-16: Fix Publish Bug; Texascale 2020; Polish

formerly known as v2.5.2 published on Thu Jul 1 16:10:38 2021 -0500

### Added

* GH-253: Initial Pattern Library Template & Styles (#25)
* Quick: Set Version & Add Changelog (#252)
* `taccsite_custom`
  * Major: Texascale 2020 (#256)

### Changed

* Quick: Polish Sample (Greet User) Plugin (#263)

### Fixed

* FP-1099: Only rebuild index on Page type for publish or unpublish events (#262)

## [2.1.1] - 2021-06-15: Hotfix for Consistent Search Bar Size

### Changed

* GH-230: Quick: Ensure search bar font sizes match (#231)

## [2.1.0] - 2021-06-14: New Frontera Homepage, Projects, CSS Plugin; Bugfixes

### Added

* Quick: New CSS Plugin Test - Custom Media Queries are Constant (#246)
* GH-233: Frontera Hero Banner Styles - Quick (#234)
* GH-195: Clone Portal Nav (#211)
* GH-67: TACC sample plugin (#190)
* FP-982: Add `rebuild_index` haystack signal processor (#189)
* GH-157: Frontera Redesign Phase 0 (#187)
* GH-171: Support CSS that is forwards compatible (#173)
* Quick: Create & Skip empty Core cms directory (#176)
* `taccsite_custom`
  * Quick: Add `tup-cms` dir (TACC/Core-CMS-Resources#45)
  * Quick: Add empty Core `cms` directory (TACC/Core-CMS-Resources#38)
  * Quick: Add home template to `neuronex-cms` secrets (TACC/Core-CMS-Resources#32)

### Changed

* FP-526: Update Portal Nav (Fix Sample Markup, Remove Old Config) (#251)
* Quick: Deprecate `site_shared` (#218)
* Quick: Simplify CSS Build Config & Fix Warnings (#199)
* Quick: Update for `taccsite_custom` repo rename (#197)
* Quick: Remove body background warn color for new sites (#175)
* Quick: FP-893/FP-977: Support new templates (#162)
* FP-947: Support favicon as custom asset (#160)
* `taccsite_custom`:
  * TACC/Core-CMS-Resources#35: Redesign Frontera home page (TACC/Core-CMS-Resources#39)
  * Quick: Remove body background warn color for new sites (TACC/Core-CMS-Resources#37)
  * TACC/Core-CMS-Resources#33: Sysmon quick redesign (#36)
  * Quick: Rename `3dem` to `neuronex` (TACC/Core-CMS-Resources#30)

### Fixed

* Quick: Simplify CSS Build Config & Fix Warnings (#199)
* Quick: Run `npm audit fix` & `yarn install` (#170)
* Quick: Settings changes to make search indexing work (#169)
* Quick: Propagate template rename to stylesheet (#167)
* `taccsite_custom`:
  * Hotfix: Add missing `__init__.py` (TACC/Core-CMS-Resources#40)
  * Quick: Import missing CSS tool (TACC/Core-CMS-Resources#43)
  * Quick: Fix `neuronex` setting (TACC/Core-CMS-Resources#31)

### Removed

* Noop: Delete outdated README.md (#200)
* FP-526: Update Portal Nav (Fix Sample Markup, Remove Old Config) (#251)

## [2.0.0] - 2021-03-31

v2.0.0 Production release as of Mar 31, 2021.

[unreleased]: https://github.com/TACC/Core-CMS/compare/v4.0.0...main
[4.0.0]: https://github.com/TACC/Core-CMS/releases/tag/v4.0.0
[3.12.0-beta.5]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-beta.5
[3.12.0-beta.4]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-beta.4
[3.12.0-beta.3]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-beta.3
[3.12.0-beta.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-beta.2
[3.12.0-beta.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-beta.1
[3.12.0-alpha.12]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.12
[3.12.0-alpha.11]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.11
[3.12.0-alpha.10]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.10
[3.12.0-alpha.9]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.9
[3.12.0-alpha.8]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.8
[3.12.0-alpha.7]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.7
[3.12.0-alpha.6]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.6
[3.12.0-alpha.5]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.5
[3.12.0-alpha.4]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.4
[3.12.0-alpha.3]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.3
[3.12.0-alpha.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.2
[3.12.0-alpha.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.12.0-alpha.1
[3.11.6]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.6
[3.11.5]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.5
[3.11.4]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.4
[3.11.3]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.3
[3.11.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.2
[3.11.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.1
[3.11.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.0
[3.11.0-beta.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.0-beta.2
[3.11.0-beta.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.0-beta.1
[3.11.0-alpha.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.11.0-alpha.1
[3.10.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.10.2
[3.10.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.10.1
[3.10.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.10.0
[3.9.5]: https://github.com/TACC/Core-CMS/releases/tag/v3.9.5
[3.9.4]: https://github.com/TACC/Core-CMS/releases/tag/v3.9.4
[3.9.3]: https://github.com/TACC/Core-CMS/releases/tag/v3.9.3
[3.9.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.9.2
[3.9.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.9.1
[3.9.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.9.0
[3.8.2]: https://github.com/TACC/Core-CMS/releases/tag/v3.8.2
[3.8.1]: https://github.com/TACC/Core-CMS/releases/tag/v3.8.1
[3.8.0]: https://github.com/TACC/Core-CMS/releases/tag/v3.8.0
[3.7.12]: https://github.com/TACC/Core-CMS/releases/tag/v3.7.12
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
