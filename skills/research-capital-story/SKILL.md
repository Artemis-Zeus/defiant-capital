---
name: research-capital-story
description: Research and evidence-map a Defiant Capital topic before outlining or drafting. Use when evaluating a new capital story, building or repairing a topic dossier, collecting sources, constructing C###—S### claims, or determining whether a protagonist's choices and the audience's scale/context questions are sufficiently evidenced.
---

# Research a capital story

Read `AGENTS.md`, `docs/project-spec.md`, `docs/research-and-sources.md`, `docs/source-collection-standard.md`, and `docs/narrative-production-standard.md`. Then read the target topic directory completely.

## Workflow

1. State one proposed protagonist and one continuous causal chain.
2. Test whether the topic has reliable evidence, escalation, reversal, mechanism value, and enough detail for a long video.
3. Build the person and institution table before expanding the event timeline.
4. For every core person, collect identity/resources, goal/incentive, knowledge at the time, available alternatives, actual action, and resulting relationship reversal.
5. Collect four audience reference types: entity scale, period conditions, number scale, and real alternatives.
6. Split every important fact into one independently testable `C###` claim.
7. Record each source as `S###` with link, date, minimal excerpt, translation, exact locator, limitations, and supported claims.
8. Mark claims only as 线索、待核验、已交叉验证、权威定论 or 存在争议.
9. Search for disconfirming evidence and plausible non-dramatic explanations.
10. Run `python3 scripts/audit_claims.py topics/active/<slug>`.

## Exit gate

Do not hand off to drafting until:

- the protagonist's decisive actions are evidenced;
- the information available before each decisive action is evidenced;
- the core result, scale, dates, and legal status are closed in the claim matrix;
- the audience can understand what the entity is, why the amount matters, and why the choice looked attractive then;
- unresolved gaps and wording limits are explicit.

Do not invent dialogue, motives, relationships, dates, causal links, or numerical comparisons. If evidence is insufficient, preserve the gap instead of smoothing it over.
