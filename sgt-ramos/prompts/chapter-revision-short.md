# Chapter Revision Prompt — Short Version (Ch30–43)

## HOW TO USE
For fast runs — especially when the only goal is +/-450 words of sensory/atmospheric material without net bloat. Paste system-role.txt as your system header first, then fill the tokens and run.

---

```
ROLE
Forensic literary editor, LITCENTRAL-aligned. Improve restraint, atmospheric/sensory
density, and code-switch usage while staying within a tight word budget.

CONTEXT
- Chapter ID:           {{chapter_id}}
- Act:                  {{act_label}} (I–IV)
- Tier:                 {{tier_classification}} (Omega Elite / Gold / Silver)
- Current word count:   {{word_count_current}}
- Target word count:    {{target_word_count}} (± {{tolerance}} words)
- Dialogue percentage:  {{dialogue_pct}}%
- Behavioral vectors (if available):
    Agency {{agency}} | Risk {{risk}} | Compassion {{compassion}}
    Alignment {{alignment}} | Code-switch {{code_switch}} | Spiritual {{spiritual}}
- LITCENTRAL notes for this chapter:
  {{LITCENTRAL_NOTES}}

CHAPTER TEXT
{{CHAPTER_TEXT}}

OBJECTIVE
Revise this chapter so that:
- Over-explanation and theme-signposting are reduced (restraint up).
- Atmospheric and sensory detail is strengthened at key moments
  (especially smell, sound, embodied reactions).
- Code-switching is purposeful: tied to identity, power, or moral/emotional pivot.
- Net word count lands as close as possible to the target.

TASKS

1) QUICK DIAGNOSTIC (MAX 6 BULLETS)
   - Where the prose over-explains or restates what the reader already knows.
   - Where sensory detail is thin but the scene would benefit from it.
   - Where code-switching could deepen character, conflict, or institutional voice.

2) REVISION PLAN (ONE PARAGRAPH, 5–7 SENTENCES)
   State:
   - Approximate words to CUT and what kind (e.g., explanatory tails,
     redundant theme statements, technical catalog).
   - Approximate words to ADD and where (e.g., pre-dawn air before refusal,
     withdrawal under fire, intimate interior beats).
   - Specific lines where code-switching will be added or tuned and why.
   No line-by-line commentary. High level only.

3) REVISED CHAPTER (FULL TEXT)
   Single continuous draft. Requirements:
   - Fold all changes in; do not annotate or bracket edits.
   - Cut "the way the information/chemistry/feeling of X…" where subtext carries it.
   - Add atmospheric/sensory material inside perception and action, not as a list.
   - Code-switched lines: emotionally or institutionally necessary, not decorative.

4) MICRO CHANGELOG (BULLETS ONLY)
   A. Restraint
      - Number of over-explanatory sentences removed (approximate).
      - 2–3 one-line before → after summaries (no full quotes).
   B. Sensory
      - 3–5 bullets naming where sensory detail was strengthened.
        (e.g., "Pre-dawn approach now carries jasmine + fuel + metal taste in mouth")
   C. Code-switch
      - Each new/revised code-switched line:
        Speaker + language + one-phrase purpose
        (e.g., "Trong – Vietnamese – institution speaking through him, then failing")
   D. Word count
      - Words cut:
      - Words added:
      - Approximate net change and whether target band was hit.

CONSTRAINTS
- Do not change verified historical facts.
- Do not shift basic scene sequence or outcome.
- Keep cultural, military, and linguistic authenticity.
- When in doubt: cut the explanation, keep the image or action.
```
