# DCAS/BISG Methodology Brief
## *SGT George Ramos: The Mathematics of Vietnam*
### The 349 Rule: A Five-Stage Retrofit Pipeline, 1965–2008

**Prepared by:** Gabriel Arce, PhD Candidate, USC Sol Price School of Public Policy  
**AUMER Foundation | EIN: 47-3485977**  
**Date:** May 29, 2026

---

### The Finding

The Vietnam Conflict Extract Data File of the Defense Casualty Analysis System (DCAS) records 58,220 U.S. military fatal casualties. Of these, 349 are coded Hispanic. That figure breaks down as follows:

- **345** from Puerto Rico
- **4** from the U.S. Virgin Islands
- **0** from any of the 50 states

That distribution is mathematically impossible as an identity count. It is dispositive of a territorial proxy: the DCAS Hispanic field does not measure whether a decedent was Hispanic. It measures whether the decedent’s home of record was Puerto Rico or the U.S. Virgin Islands.

Of 3,377 DCAS Vietnam decedents whose surname or home-of-record places them in the Hispanic-attribution corridor, 2,132 pass the BIFSG-1970 threshold. Of those, **1,789 are coded WHITE** despite surnames including Esqueda, Hernandez, Cisneros, Ramirez, Gomez-Gutierrez, Ruvalcaba-Lopez, Guzman, Nava, Carrillo, and Gutierrez — all with BIFSG posteriors above 0.90. Their home-of-record states: Texas (711), California (640), New Mexico (148), Arizona (113), New York (98), Colorado (73).

The classification failure ratio is **84.9%**. The undercount is **6.6×** against the BISG floor estimate of 2,309.

---

### The Mechanism: Not a Wartime Error

The 349 figure was not produced during the Vietnam War. It was produced between approximately 2000 and **April 29, 2008** — the documented NARA accession date (RG 330, NAID 2240992) — through a five-stage administrative retrofit:

| Stage | Years | What Happened |
|---|---|---|
| DD-1300 | 1965–1975 | Report of Casualty captured Race only — no ethnicity field |
| CACDB | 1967– | OSD casualty database passthrough — race only |
| CACCF | 1973–1998 | Combat Area Casualties Current File — passthrough |
| OMB SPD-15 | 1977 (rev. 1997) | “Hispanic” established as federal standard — **prospective only** |
| DCAS Retrofit | ~2000–Apr 29, 2008 | DMDC applied Directive 15 retroactively to records that never carried it. Territory became the substitution proxy: PR + USVI → HISPANIC; 50 states → WHITE |

OMB Statistical Policy Directive No. 15 was issued May 12, 1977 — two years after the last Vietnam casualty was recorded. The federal category “Hispanic” did not exist when these men died. When DMDC was required to produce an ethnically coded extract decades later, they substituted what they had: territorial coding. The result is the 349.

---

### Three Independent Estimators

Three methodologically independent approaches all confirm the same range:

| Estimator | Range | Interpretation |
|---|---|---|
| BISG (surname + geography) | **2,309** | Institutional floor — Σ posteriors across threshold band |
| BIFSG (+ Tzioumis 2018 first-name priors) | **2,876–3,372** | Methodological corridor; median 3,272 |
| Project 100,000 demographic estimate | **2,526–5,156** | Fully contains BIFSG corridor — independent triangulation |

The published 349 is outside every reconstructed range. Statistical defensibility:
- T1 Resource Allocation: χ² = 28.64, permutation p = 0.0095 — PASS
- T4 Temporal Concentration: binomial p = 0.0021 — PASS
- T5 P100K ↔ BIFSG Convergence: 100% containment — PASS
- T3 Inter-Rater α = 0.755 (CI 0.612–0.878) — ACCEPTABLE
- Reproducibility hash: MD5 368b53d1…c97e72be | Python 3 / NumPy 1.26 / SciPy 1.13 | seed=42

---

### What This Research Claims — and What It Does Not

This research does not allege deliberate suppression of Hispanic casualties during the Vietnam War. The wartime records captured what the classification systems of that era could capture — which did not include a federal Hispanic category, because none existed until 1977.

What this research establishes is more precise and more difficult to dismiss:

> *When the government’s own agency (DMDC) was required to produce an ethnically classified extract of Vietnam casualties, it substituted a territorial proxy for the ethnic identity it did not have. The result is a published file in which every mainland Hispanic Vietnam veteran — men named Esqueda, Hernandez, Cisneros, Ramirez — is coded WHITE. The 349 is not a count of Hispanic casualties. It is a count of Puerto Rican and U.S. Virgin Islands casualties. The failure is not in the original recording. The failure is in a retroactive classification decision made between 2000 and 2008, and the fifty years of policy discussion that proceeded without correcting it.*

The method is public-record reconstruction, source triangulation, and forensic classification analysis. The reproducibility file, coding rules, and audit trail are available for independent verification. Any researcher using the same source hierarchy and coding rules can reproduce or falsify the result.

---

### Sources

- U.S. Department of Defense / NARA: *Vietnam Conflict Extract Data File, Defense Casualty Analysis System*, RG 330, NAID 2240992 (58,220 records; NARA accession April 29, 2008)
- U.S. Office of Management and Budget: *Statistical Policy Directive No. 15* (May 12, 1977); revised 1997
- Public Law 94-311 (June 16, 1976) — first federal mandate for data collection on persons of Spanish origin
- RAND Corporation: Elliott et al., *Using Geocoding and Surname Analysis to Estimate Race and Ethnicity*, RR-1162 (2009); Tzioumis (2018) first-name prior extension
- Consumer Financial Protection Bureau: BISG proxy methodology (adopted 2014, fair-lending enforcement standard)
- AR 340-18-2 (Army Functional Files System) — records retention schedule governing wartime casualty files
