# Zero-To-One Workflow

Use this workflow when the user starts from a product idea, intent, market observation, or tool concept.

## Principle

Do not begin with a feature list. Begin with usage scenes and validate the core experience before building supporting modules.

## Flow

1. Define the scene.
   - Actor, trigger, situation, current workaround, desired outcome, emotional bar, and success signal.
2. Derive the product skeleton.
   - Core objects, core loop, primary surfaces, navigation, state model, and minimum interactions.
3. Build the smallest interactive prototype.
   - Prefer working UI over static documents when the request includes product design or tooling.
   - Mock data is acceptable when it validates interaction and judgment.
4. Capture feedback.
   - Ask the user to judge clarity, usefulness, trust, speed, taste, and missing leverage.
5. Contract the validated core.
   - Convert only the accepted core behavior into contracts.
6. Harden selectively.
   - Add auth, persistence, permissions, settings, empty/error states, import/export, analytics, and operational safeguards only after the core experience holds.

## Output Rule

The main output should be a usable skeleton or a brief that can produce one. Avoid large PRDs before the user has seen or judged the interaction.

## Done Criteria

- The core scene can be exercised end to end.
- The user can give experience feedback from something concrete.
- The accepted behavior has contracts and verification steps.
- Supporting modules are explicitly deferred or scheduled.
