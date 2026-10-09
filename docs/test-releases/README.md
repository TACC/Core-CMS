# Test Releases

Manual test steps per release, for the testing team to verify before/after deploy.

> [!NOTE]
> RCs (release candidates) are what get tested, so an RC doc is the source of truth. A final release doc should just point to the RC doc(s) that already cover its content, not repeat them.

## Sections

- **Standard Features**\
    Run on every portal deploy unless the RC doc has none. New features and PRs without a named client/production test site go here.
- **Pre-Tested Features**\
    Tweaks or fixes already verified on a **named client or production site** in the PR (link evidence; not local `/test/` or dev-only), or a **mechanical split** of an existing test page with no behavior change (link prior RC evidence). Repeat only if you want a spot-check.
- **Optional Features**\
    Run only when the portal uses the feature (see notes for feature).
- **Deployment**\
    Developer/deployment checks, not portal UI smoke tests.
