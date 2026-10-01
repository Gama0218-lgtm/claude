# Chapter Revision Prompt — Full Version (LITCENTRAL-Aligned)

## HOW TO USE
Copy everything below the divider. Replace all `{{variable}}` tokens with actual values from LITCENTRAL before submitting. Paste the system-role.txt content as your system/role header first.

---

```
TITLE: Chapter Revision & Forensic Changelog (LITCENTRAL-Aligned)

CONTEXT:
You are revising one chapter of a 43-chapter, 245k-word literary-historical manuscript
about Chicano Vietnam veterans and deported veterans. LITCENTRAL provides chapter-level analytics:

- Chapter ID:          {{chapter_id}}
- Act:                 {{act_label}} (I–IV)
- Tier:                {{tier_classification}} (Omega Elite / Gold / Silver)
- Word count (current):{{word_count_current}}
- Dialogue percentage: {{dialogue_pct}}%
- Behavioral vector scores:
    Agency:      {{agency}}
    Risk:        {{risk}}
    Compassion:  {{compassion}}
    Alignment:   {{alignment}}
    Code-switch: {{code_switch}}
    Spiritual:   {{spiritual}}
- Omega composite Ω:   {{omega}}
- Sub-scores:
    CLS: {{cls}}
    BIS: {{bis}}
    SII: {{sii}}
    MRF: {{mrf}}
- Other metrics (if available):
    Restraint score:   {{restraint_score}} / 100
    CL-MoE mean:       {{cl_moe_mean}}
    CME_mainstream:    {{cme_mainstream}}

REVISION OBJECTIVE:
1) Maintain structural integrity and historical accuracy.
2) Improve restraint (fewer explanatory tails, less over-signaling).
3) Increase atmospheric and sensory density in targeted moments without drifting into exposition.
4) Calibrate code-switch and register shifts to match SII and MRF goals.
5) Respect a strict word budget:
   - Target word count: {{target_word_count}} (± {{tolerance}} words)
   - You may CUT or ADD, but report net delta.

INPUTS:
A. Current chapter text:
{{CHAPTER_TEXT}}

B. LITCENTRAL flags / notes for this chapter (if any):
{{LITCENTRAL_NOTES}}

TASKS:

1) DIAGNOSTIC SNAPSHOT
   In 5–7 bullet points, identify key issues in:
   - Restraint vs. over-explanation
   - Sensory coverage (smell, sound, touch, taste, sight, body/inner state)
   - Code-switching (Spanish/Vietnamese/English) and register shifts
   - MRF: moments where reconnaissance/technical vocabulary can pivot into
     emotional or moral register
   Explicitly name at least 3 candidate locations for atmospheric/sensory
   enhancement that are NOT backstory dumps or lectures.

2) REVISION PLAN (WORD-BUDGETED)
   Specify planned CUTS:
   - Estimate total words to remove.
   - Describe sentence types targeted (e.g., "explanatory tails",
     "radio-pack technical catalog", "over-signaled theme statements").
   Specify planned ADDS:
   - Estimate total words to add.
   - Focus: smells, textures, soundscapes, embodied reactions, environmental details.
   - Identify at least 2 code-switch additions that serve SII and/or MRF.
   Ensure planned net delta ≈ 0 or whatever {{target_word_count}} requires.

3) REVISION EXECUTION (FULL PASS)
   Present the fully revised chapter text as a single continuous polished draft.
   Enforce:
   - No "the way the X of a thing…" explanatory tails.
   - No meta-explanations of chemistry/feeling/information transfer where
     subtext will suffice.
   - Sensory details embedded in action and perception, not listed.

4) CHANGELOG (FORENSIC)
   A. Restraint moves
      - Number of over-explanation cuts.
      - 2–3 concrete before → after examples with word deltas.
   B. Code-switch moves
      For each new or revised code-switched line:
      - Speaker | Language | Function (institution voice / self-diagnosis /
        intimacy / defiance) | Metric served (SII, MRF, etc.)
   C. Sensory constants
      - Confirm coverage: sight, sound, smell, taste, touch, body/inner.
      - Note signature recurrent motifs (e.g., jasmine + napalm in pre-dawn wind)
        and their placement in the chapter's emotional arc.
   D. MRF beats
      For each strongest new/revised MRF passage:
      - Trace how vocabulary pivots from reconnaissance/technical to
        emotional/moral in 2–4 sentences, without labeling registers.
   E. Net word delta
      - Words cut: {{words_cut_estimate}}
      - Words added: {{words_added_estimate}}
      - Net change: {{net_delta}}  (target: {{target_word_count}})

CONSTRAINTS:
- Do not introduce anachronistic language or technology.
- Do not alter verified historical facts without stating the change in the changelog.
- Maintain Chicano, military, and Vietnamese cultural/linguistic authenticity.
- Prioritize trust in the reader over explanation.
```
