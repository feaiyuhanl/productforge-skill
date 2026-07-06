# Interactive UI Prototype

Use this file only after `mvp-artifacts.md` selects UI as the validation artifact.

Do not use this file for skill, CLI, API, workflow, notebook, or document-backed products unless their core judgment genuinely depends on visual layout or direct on-screen interaction.

## Skeleton Scope

An interactive UI skeleton should include:

- Primary user path.
- Core objects and states.
- Minimal navigation.
- Realistic sample data.
- Loading, empty, and error states when they affect trust.
- One clear way for the user to judge the visual and interaction experience.

## Exclusions

Do not build supporting modules first unless the selected UI scene requires them:

- Authentication.
- Billing.
- Admin settings.
- Full data persistence.
- Multi-role permission systems.
- Complete reporting.

## Design Bar

- The first screen should be the actual product experience, not a marketing page.
- UI should expose the already-clarified decision model and feedback loop.
- Copy should help the user act, not explain the tool's internal process.
- Prototype fidelity should be high enough for judgment but no higher than needed for the next decision.

## Evidence

After building or specifying a UI skeleton, provide:

- Core scene exercised.
- What is real vs mocked.
- Feedback questions for the user.
- Missing contracts before production hardening.
