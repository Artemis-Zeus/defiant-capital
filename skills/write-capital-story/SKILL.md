---
name: write-capital-story
description: Turn an evidence-complete Defiant Capital topic into a story outline (架构稿, bound to C###—S### evidence) and a single recordable voiceover script (script/master.md). Use when planning story structure, writing or rewriting the voiceover script, adding hooks or audience reference points, or auditing pacing without weakening evidence and legal boundaries.
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

## Produce the two layers

### Story outline (架构稿)

Write or update `05-story-outline.md` first: chapter cards, information-release order, and the `[C###]` binding for every fact that enters the script. This is the fact-mapping layer; keep visible claim markers here.

### Voiceover script (口播稿)

Write `script/master.md` as the single narration script—no separate net-draft file. Requirements:

- No `C###`/`S###` numbers in the body; bind facts through the outline instead.
- End every chapter with a citation blockquote listing this chapter's sources by name only (site/book/report/journal title plus year); never include URLs or numbers.
- Preserve exact attribution, legal qualifiers, and number/date scope in the narration itself.
- Break long sentences at natural breaths. Prefer people, actions, and consequences over abstract summaries.

The outline and the script must stay version-aligned; do not let script edits drift from the outline's fact binding.

## Audit

Run:

```bash
python3 scripts/audit_claims.py topics/active/<slug>
python3 scripts/audit_voiceover.py topics/active/<slug>/script/master.md
```

Treat claim-closure failures in the research layer as blocking. Treat sentence length, report-language, number density, and time jumps as editorial warnings requiring human listening.

Do not copy another creator's catchphrases, recurring jokes, branded units, or sentence patterns. Learn only transferable structure, information release, contrast, and oral rhythm.
