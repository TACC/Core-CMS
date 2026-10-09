# Test Releases

Manual test steps per release, for the testing team to verify before/after deploy.

> [!NOTE]
> RCs (release candidates) are what get tested, so an RC doc is the source of truth. A final release doc should just point to the RC doc(s) that already cover its content, not repeat them.

## Sections

- **Standard Features** — run on every portal deploy unless the RC doc has none.
- **Pre-Tested Features** — already verified in the linked PR(s) (UI evidence, client/site testing, or explicit PR notes). Repeat only for a spot-check.
- **Optional Features** — run only when the portal uses the feature (see that section’s NOTE).
- **Deployment** — developer/deployment checks, not portal UI smoke tests.
