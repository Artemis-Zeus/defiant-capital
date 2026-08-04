---
name: write-capital-story
description: Turn an evidence-complete Defiant Capital topic into a character-driven editor master and a recordable voiceover. Use when planning story structure, rewriting a report-like draft, converting master.md to voiceover.md, adding hooks or audience reference points, or auditing pacing without weakening C###—S### evidence and legal boundaries.
---

# Write a capital story

Read `AGENTS.md`, `docs/editorial-standards.md`, `docs/narrative-production-standard.md`, and the target topic's README, brief, timeline, sources, claims, risk review, outline, and existing scripts.

## Build the structure

1. Write one story promise and one question the ending will answer.
2. Choose one absolute protagonist. Give each major supporting character one observable function.
3. Arrange the body around the protagonist's consecutive choices, not around institutions or financial terms.
4. Use the generic chain—success, credit, expansion, warning, irreversible choice, external change, relationship reversal, cost, fate—as a diagnostic only.
5. Add only the background needed to answer who/what this is, how large it is, why the money matters, and why the choice was tempting at the time.
6. Make each chapter contain an action, a changed situation, and a forward question.
7. Explain one mechanism at a time and immediately return to who must act because of it.
8. End once: character fate first, one thematic judgment second.

## Produce two layers

### Editor master

Write `script/master.md`. Keep visible `[C###]` markers, exact attribution, legal qualifiers, number/date scope, and editor warnings.

### Voiceover

Write `script/voiceover.md` as the words the narrator will actually read. Remove visible claim markers and production notes, but preserve factual meaning and legal status. Break long sentences at natural breaths. Prefer people, actions, and consequences over abstract summaries.

Never replace the editor master with the voiceover. Keep both synchronized by version.

## Audit

Run:

```bash
python3 scripts/audit_claims.py topics/active/<slug>
python3 scripts/audit_voiceover.py topics/active/<slug>/script/voiceover.md
```

Treat claim-closure failures as blocking. Treat sentence length, report-language, number density, and time jumps as editorial warnings requiring human listening.

Do not copy another creator's catchphrases, recurring jokes, branded units, or sentence patterns. Learn only transferable structure, information release, contrast, and oral rhythm.
