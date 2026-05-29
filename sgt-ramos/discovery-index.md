# Discovery Index
## *SGT George Ramos: The Mathematics of Vietnam*
### Complete Evidentiary Package — Forensic Literary Historiography Project

---

## What This Index Is

This discovery index catalogs every piece of supporting evidence for the manuscript, its claims, and its submission process. "Discovery" is used here in both its legal and archival senses:

- **Legal:** The organized disclosure of evidence to a reviewing party, structured so the chain of custody, methodology, and source attribution are transparent and verifiable.
- **Archival:** The process of identifying, documenting, and preserving materials so they remain accessible, authentic, and traceable over time.

The index is organized in four tiers: Process Documents (how the submission works), Quantitative Evidence (data and methodology), Case Evidence (individual veteran documentation), and Literary Evidence (the manuscript and its scoring infrastructure). Every item has a status, a source, and a verification tier.

---

## EXHIBIT A — Submission Process Documentation

### A-1. Legal-Style Submission Roadmap (PDF Flowchart)
**File:** `submission_flowchart_styled.pdf`  
**Status:** Finalized  
**Description:** One-page visual roadmap of the six-step submission protocol — from email transmission through portal registration, upload event, SIP→AIP→DIP repository ingest, and final electronic footprint creation. Designed to function simultaneously as a legal chain-of-custody record, an archival deposit protocol, and a grant-readiness demonstration.  
**Legal value:** Establishes the procedural framework for converting each institutional submission into a timestamped, hashed, multi-source provenance record.  
**Relationship to other exhibits:** Operationalizes the Electronic Footprint Protocol described in the Artifact Submission Package (see project documents). Every submission to the institutions listed in the Institution Directory follows this flowchart.

**Six steps documented:**
1. **Transmission** — Controlled sender account, SHA-256 hash in message body, headers preserved. *Establishes intent, date, and first custody event.*
2. **Portal Registration** — Institutional account creation, identity tied to submission record. *Ties depositor to the institutional record.*
3. **Upload Event** — Manuscript, metadata, sidecar manifest, receipt/accession ID captured. *Creates the primary electronic footprint.*
4. **Repository Ingest** — SIP → AIP → DIP preservation lifecycle, fixity checks, provenance metadata. *Institutional custody transfer.*
5. **Electronic Footprint** — Timestamp, fixity log, provenance trail, public or internal accession ID. *The auditable chain of custody.*
6. **Strategic Use** — The completed footprint supports archival preservation, academic review, and grant development simultaneously.

---

## EXHIBIT B — Quantitative Evidence

### B-1. DCAS Audit — Hispanic Casualty Classification Analysis
**Source:** U.S. Department of Defense, Defense Casualty Analysis System (DCAS)  
**Methodology:** Bayesian Improved Surname Geocoding (BISG), RAND RR-1162 protocol  
**Status:** Analysis complete; pending external peer review  
**Key finding:** 349 casualties coded Hispanic (0.6%) vs. 2,309–3,000 estimated (5.5–7.2%) — 84.9% classification failure rate across 58,220 U.S. Vietnam-era casualties  
**Files:** `DCAS_Audit_Results.xlsx`, `DCAS_Data_Acquisition_Tracker.xlsx`  
**Verification tier:** CB-HSIVF T1 (government database, primary source)  
**Legal value:** The finding is derived from a federal database using a federal agency's own preferred methodology (CFPB fair-lending standard). The government cannot reject the methodology without rejecting its own regulatory practice.

### B-2. PSID Variable Registry — Benefits Denial and Deportation Cycle
**Source:** Panel Study of Income Dynamics (University of Michigan / NORC), federally funded  
**Status:** Variable registry complete; logistic regression pending PSID restricted data agreement  
**Key variables:**

| Variable | Description | Deportation Cycle Stage |
|---|---|---|
| `ER32054` | Vietnam Draft Category (restricted) | Trigger Enforcement |
| `ER11972` | Naturalization status | Legal Status |
| `ER16235`, `ER16270`, `ER20181`, `ER20216`, `ER23782`, `ER23817` | Benefits denied due to non-citizenship (6 waves) | Benefits Access Barrier |
| `ER57652` | First year in U.S. | Migration History |
| `ER11928` | Children outside U.S. | Family Separation |

**Planned analysis:** Logistic regression — draft-eligible non-citizen male heads (Category 1) vs. benefits denial rates, controlling for service era and household composition  
**Verification tier:** CB-HSIVF T1 (federally funded longitudinal survey)

### B-3. LITCENTRAL Manuscript Analytics Dashboard
**Source:** Author-constructed analytics system  
**Status:** Active, 43 chapters scored  
**Key metrics:**
- Behavioral vectors: Agency, Risk, Compassion, Alignment, Code-switch, Spiritual (Cronbach's α = 0.938, N=11 pilot)
- Omega composite: Ω = 71.443 + 0.124(CLS) + 0.118(BIS) + 0.089(SII) + 0.067(MRF), R² = 0.947
- AutoCrit: Overall 88.3 / Strong Writing 100.0 / Dialogue 93.8 / Repetition 77.6
- CL-MoE mean: 0.115 / CME_mainstream: 0.435
- Tier distribution: 21 Omega Elite, remainder Gold/Silver

**File:** `SGTRamos_LITCENTRAL_FULL.html` (383KB static dashboard)  
**Verification tier:** CB-HSIVF T3 (author-constructed, methodology documented, external audit pending)

### B-4. BISG Methodology Note
**Source:** RAND Corporation (RR-1162), Consumer Financial Protection Bureau rulemaking  
**Status:** Published, peer-reviewed  
**Relevance:** Establishes that BISG is the federal government's own preferred methodology for population-level ethnic identification from administrative records. Applying it to DCAS uses the government's tool against the government's data.  
**Concordance rate:** 90–96% with self-reported race for major groups  
**Verification tier:** CB-HSIVF T1

---

## EXHIBIT C — Case Evidence (Veteran Case Registry)

**Registry:** MNV-01 through MNV-15  
**Verification tiers:** CB-HSIVF T1 (primary federal source) through T4 (community testimony)  
**Cross-reference databases:** CMOHS, The Wall USA, Coffelt Database, BIRLS, EOIR, DHS deportation records

### Priority Cases (Full Documentation)

**MNV-01 / MNV-02 — Valente and Manuel Valenzuela**  
Colorado-based Marines, CO-MX border corridor, active advocacy, pending legal status. Migration history and citizenship variables link to PSID framework. Deportation cycle stage: Status Authorization / Post-Removal.

**MNV-03 — Sae Joon Park**  
Post-Vietnam service, deported 2025, public confrontation with DHS Secretary Noem. September 2025 / December 2025 statements from federal officials documented as contradictions in TruthEngine360 AI Search Log. VA July 2025 XC-file policy change cross-referenced. Deportation cycle stage: Notice / Hearing.

**MNV-04 — Manuel Mike Segura**  
*Pre-IIRIRA case (1985)* — deported before 1996 law most scholarship treats as the origin point. Tijuana death, VA benefits denial, BIRLS lookup pending. Establishes that the deportation pattern predates the current legal framework. Deportation cycle stage: Post-Removal (deceased). Verification tier: CB-HSIVF T2.

**MNV-05 — Jesus Salvador Durán**  
Medal of Honor recipient, 37-year recognition gap (Pentagon Valor Review 2014). Appears in DCAS, CMOHS Hispanic/Latino recipients database, congressional record. The recognition latency directly feeds Omega Elite chapter scoring on institutional admission of oversight. Verification tier: CB-HSIVF T1.

**MNV-06 through MNV-15 — Supporting Cases**  
Documented at T1–T4 verification tiers. Full case files in TruthEngine360 Veteran Case Registry.

---

## EXHIBIT D — Literary Evidence

### D-1. Manuscript — v97_UPDATED.jsx
**Format:** JSX/Markdown, 43 chapters, 241,117 words  
**Acts:** I–IV  
**Authoritative version:** v97  
**Status:** Revision cycle active (Ch30–43 in progress)  
**Verification:** All historical claims in manuscript are classified by verification tier in companion documentation

### D-2. TruthEngine360 Intelligence Database
**Components:**
- COMMANDDASHBOARD (KPIs, deportation-cycle stage mapping)
- PSID Variable Registry (immigration and benefits variables, 9 deportation stages)
- Veteran Case Registry (MNV-01–MNV-15)
- AI Search Log (structured queries, source attribution, pending/verified status)

**Status:** Active, updated continuously during research cycle  
**Verification tier:** Mixed T1–T4 depending on source

### D-3. AUMER Cohort Documentation
**Source:** Author-constructed cohort study  
**Status:** Workbooks compiled  
**Files:** AUMER cohort workbooks (referenced in research tracker)

### D-4. Chapter Revision Prompts (Ch30–43)
**Purpose:** Structured revision protocol ensuring each chapter revision is data-informed (LITCENTRAL metrics), evidence-constrained (TruthEngine360 case documentation), and quality-controlled (restraint scoring, sensory density, code-switch calibration)  
**Status:** Template finalized, application in progress

---

## Discovery Summary Table

| Exhibit | Document | Source Type | Verification Tier | Status |
|---|---|---|---|---|
| A-1 | Submission Flowchart (PDF) | Author-constructed | T3 | Final |
| B-1 | DCAS Audit | Federal database (DoD) | T1 | Complete |
| B-2 | PSID Variable Registry | Federal survey (UM/NORC) | T1 | Pending regression |
| B-3 | LITCENTRAL Dashboard | Author-constructed | T3 | Active |
| B-4 | BISG Methodology Note | RAND / CFPB | T1 | Published |
| C-1 | MNV-01/02 Valenzuela | Multi-source | T2 | Active |
| C-2 | MNV-03 Park | Federal + press | T1/T2 | Active |
| C-3 | MNV-04 Segura | Multi-source | T2 | Complete |
| C-4 | MNV-05 Durán | Federal (CMOHS/DCAS) | T1 | Complete |
| C-5 | MNV-06–15 | Mixed | T1–T4 | Active |
| D-1 | Manuscript v97 | Author | T3 | Active revision |
| D-2 | TruthEngine360 | Mixed | T1–T4 | Active |
| D-3 | AUMER Cohort | Author-constructed | T3 | Compiled |
| D-4 | Ch30–43 Revision Protocol | Author | T3 | In progress |

---

## Chain of Custody Statement

All documents in this discovery index are maintained by the author with version control, SHA-256 file hashing (for PDFs and final manuscript versions), and timestamped email transmission records (for institutional submissions). The submission flowchart (Exhibit A-1) governs the process by which each exhibit, when submitted to an institution, acquires an additional layer of institutional provenance — accession numbers, portal receipts, and fixity logs — that extends the chain of custody beyond the author's own records into the institutional record.

This index is updated at each major revision milestone and resubmitted to the electronic footprint log as a versioned document.

**Current version:** 1.0  
**Date:** 2026-05-28  
**Author:** Gabriel Arce  
**Project:** *SGT George Ramos: The Mathematics of Vietnam*
