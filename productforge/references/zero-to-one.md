# Zero-To-One Workflow

Use this workflow when the user starts from a product idea, intent, market observation, or tool concept.

## Principle

Do not begin with a feature list or a UI screen. Begin with the functional experience: who needs what job done, what they provide, what the product does, what comes back, how success is recognized, and how failure is handled.

## Flow

1. Clarify the intent boundary.
   - Product type, target actor, job to be done, non-goals, constraints, existing assets, and unknowns that would change direction.
   - Ask only when the missing answer changes product direction or implementation risk; otherwise state assumptions and continue.
2. Define scenes.
   - Actor, trigger, situation, current workaround, desired outcome, emotional bar, and success signal.
3. Close the use cases.
   - For each core use case, specify input, action, output, success check, failure behavior, and acceptance signal.
   - Keep the first loop narrow enough to exercise end to end in one review session.
4. Map the MVP capability system.
   - Core objects, operations, states, rules, and boundaries.
   - Separate must-have capabilities from wrappers, polish, integrations, and later hardening.
5. Choose the validation artifact.
   - Select the smallest artifact that lets the user judge the core experience: skill skeleton, CLI command, API contract, workflow playbook, notebook, document template, or UI.
   - Use UI only when visual layout, navigation, or direct manipulation is central to the product judgment.
6. Build or specify the smallest executable skeleton.
   - Mock data is acceptable when it validates behavior and judgment.
   - The artifact should expose what is real, what is mocked, and what decision it is meant to unlock.
7. Capture feedback.
   - Ask the user to judge usefulness, clarity, trust, speed, taste, missing leverage, and whether the use-case loop actually closes.
8. Contract the validated core.
   - Convert only accepted behavior into contracts.
9. Harden selectively.
   - Add auth, persistence, permissions, settings, empty/error states, import/export, analytics, and operational safeguards only after the core experience holds.

## Output Rule

The first output should be a decision-oriented zero-to-one brief: intent boundary, scenes, use-case closure, MVP capability map, validation artifact choice, and next executable skeleton. Avoid large PRDs and avoid UI prototypes before the user has accepted UI as the right validation artifact.

## Done Criteria

- The core use-case loop can be exercised end to end.
- The user can give experience feedback from the chosen artifact.
- The accepted behavior has contracts and verification steps.
- Supporting modules are explicitly deferred or scheduled.
