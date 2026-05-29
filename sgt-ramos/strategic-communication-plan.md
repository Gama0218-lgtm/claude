# SGT Ramos: Strategic Communication Plan
## *The Mathematics of Vietnam* — Institutional Outreach, Grant Campaign & Notion Workspace

---

## SECTION 1: EXECUTIVE SUMMARY

**Project:** *SGT George Ramos: The Mathematics of Vietnam* — 245,000-word literary-historical manuscript documenting the systemic exclusion of Chicano and non-citizen veterans from the official record of the Vietnam War.

**The Core Claim (one sentence):** The Pentagon's own casualty database, audited by the Pentagon's own preferred demographic methodology, shows an 84.9% classification failure for Hispanic casualties — and the government's own longitudinal survey documents six consecutive waves of benefits denied to non-citizen veterans.

**Communication Goal:** Place the manuscript, its evidentiary infrastructure (DCAS audit, PSID variable registry, TruthEngine360, LITCENTRAL), and its 15 veteran case files into institutional custody across 20+ archives, universities, foundations, and policy organizations — generating an electronic footprint that functions as independent verification of the research record.

**Campaign Scale:**
- Phase 1 (manual): 10–20 institutions
- Phase 2 (semi-auto): 20–100 institutions
- Phase 3 (full scale): 100–300 institutions

---

## SECTION 2: COMMUNICATION OBJECTIVES

| # | Objective | Metric | Target Date |
|---|-----------|--------|-------------|
| 1 | Establish archival custody at 3+ Tier 1 institutions | Accession IDs received | Phase 1 end |
| 2 | Submit to 5+ grant funders with full evidentiary packet | Submission confirmations | 90 days |
| 3 | Achieve >15% institutional acknowledgment rate | Responses / submissions | Phase 1 review |
| 4 | Place manuscript chapter in peer-reviewed journal | Acceptance notice | 6 months |
| 5 | Generate DOI/handle for research datasets | Persistent identifier | Phase 2 start |
| 6 | Secure PSID restricted data agreement | Signed agreement | 60 days |
| 7 | Brief 1 policy office (USC Sol Price / Congressional) | Meeting confirmed | 90 days |

---

## SECTION 3: AUDIENCE MATRIX

### Tier 1 — Archival Custodians
*Primary institutions for permanent custody and independent verification*

| Institution | Type | Contact Angle | Key Message |
|-------------|------|---------------|-------------|
| USC Digital Library | University Archive | Special Collections | DCAS audit dataset + manuscript as primary source |
| UCLA Chicano Studies Research Center | Ethnic Studies Archive | Director of Collections | 15 veteran case files + BISG methodology |
| Smithsonian NMAAHC | Federal Archive | Collections Manager | Non-citizen veteran documentation gap |
| Library of Congress Manuscripts | Federal Archive | Veterans History Project | Oral history + service record chain |
| National Archives (RG 319/407) | Federal Archive | FOIA Liaison | Pentagon casualty record audit trail |

### Tier 2 — Grant Funders
*Funding the research infrastructure and dissemination*

| Funder | Program | Deadline Window | Ask |
|--------|---------|-----------------|-----|
| NEH Scholarly Editions | Federal | November cycle | $100K–$200K |
| Ford Foundation | Social Justice | Rolling | $250K–$500K |
| MacArthur Foundation | Public Interest Media | Rolling | $150K–$300K |
| USC Sol Price School | Policy Research | Internal | $50K–$100K |
| NEA Literature | Federal | Spring cycle | $25K–$50K |
| Vietnam Veterans of America Foundation | Veterans | Rolling | $25K–$75K |

### Tier 3 — Academic & Policy Channels
*Building intellectual legitimacy and policy relevance*

| Channel | Vehicle | Message Emphasis |
|---------|---------|------------------|
| Journal of American Ethnic History | Article submission | BISG methodology + DCAS audit |
| Latino Studies (Palgrave) | Article submission | LITCENTRAL + behavioral vectors |
| Armed Forces & Society | Article submission | Non-citizen veteran benefits denial |
| USC Sol Price School of Public Policy | Policy brief | Legislative gap + PSID evidence |
| Congressional Hispanic Caucus | Briefing memo | 84.9% stat + MNV case files |

### Tier 4 — Media & Public Record
*Extending reach and public accountability*

| Channel | Format | Timing |
|---------|--------|--------|
| ProPublica / Texas Tribune | Data story pitch | After Tier 1 accession |
| LA Times | Op-ed | After first grant submission |
| Vietnam Veterans of America (Magazine) | Feature story | Phase 2 |
| NPR Latino USA | Audio feature | Phase 2 |

---

## SECTION 4: CORE MESSAGE FRAMEWORK

### Message A — The Evidentiary Claim
> "The government's own databases — audited by the government's own preferred methodology — document an 84.9% classification failure for Hispanic casualties in the Vietnam War. This is not an allegation. It is a calculation the Defense Department can reproduce on its own systems."

**Use for:** Archives, legal framing, policy offices, FOIA-holding institutions

### Message B — The Human Record
> "Fifteen veteran case files — cross-referenced against Pentagon casualty records, PSID longitudinal data, and FOIA-obtained service records — document what administrative silence looks like when it accumulates across fifty years. This is the record the official record omitted."

**Use for:** Funders, ethnic studies archives, oral history programs, media

### Message C — The Literary Argument
> "*The Mathematics of Vietnam* is a 245,000-word manuscript scored at Omega Elite tier across LITCENTRAL's behavioral analytics — a system trained on 11-chapter pilot data yielding Cronbach's α=0.938. The story is forensic. The prose earns it."

**Use for:** Literary foundations, NEA, academic journals, university presses

---

## SECTION 5: SUBMISSION CAMPAIGN CALENDAR

### Phase 1 — Manual (Weeks 1–8)
*Goal: First 10–20 submissions. Learn. Refine. Confirm >15% acknowledgment.*

| Week | Action | Institution(s) | Deliverable |
|------|--------|----------------|-------------|
| 1 | Prepare packet + SHA-256 hashes | — | Signed custodian declaration |
| 1 | First submission | USC Libraries (INST-0001) | Footprint log entry #001 |
| 2 | Second submission | UCLA CSRC (INST-0002) | Footprint log entry #002 |
| 2 | PSID application submitted | University of Michigan ICPSR | Signed restricted data agreement |
| 3 | Third submission | Smithsonian NMAAHC (INST-0003) | Footprint log entry #003 |
| 3 | First grant submission | NEH Scholarly Editions | Portal confirmation |
| 4 | Fourth + fifth submissions | LOC + National Archives | Footprint log entries #004–005 |
| 4 | USC Sol Price briefing request | Public Policy dept. | Meeting request sent |
| 5 | Review: acknowledgment rate | All submitted | Decision: proceed to Phase 2? |
| 6 | Academic journal submission | Journal of American Ethnic History | Submission ID |
| 7 | Second grant submission | Ford Foundation | Portal confirmation |
| 8 | Phase 1 debrief | — | Updated institution-directory.json |

### Phase 2 — Semi-Automated (Weeks 9–24)
*Scale to 20–100 institutions using Python automation pipeline.*

- Deploy `generate_cover_letter.py` with tier-specific templates
- Run `assemble_packet.py` for SHA-256 manifest generation
- Log all submissions via `footprint_log.py`
- Target: MacArthur, NEA, veterans foundations in parallel
- Academic journal article published or under review

### Phase 3 — Full Scale (Weeks 25+)
*100–300 institutions. Email status parsing. Elasticsearch dashboard live.*

- Automated response tracking
- Kibana / Google Sheets dashboard
- DOI/handle registered for dataset
- Policy brief delivered to Congressional Hispanic Caucus

---

## SECTION 6: MESSAGE TEMPLATES BY AUDIENCE TYPE

### Template A — Archive / Special Collections
```
Subject: Submission for Archival Consideration — SGT George Ramos: The Mathematics of Vietnam

Dear [NAME], [TITLE],

I am submitting *SGT George Ramos: The Mathematics of Vietnam* — a 245,000-word 
literary-historical manuscript documenting the administrative exclusion of Chicano 
and non-citizen veterans from the official record of the Vietnam War — for archival 
consideration at [INSTITUTION].

The submission includes:
  • The complete manuscript (SHA-256: {{manuscript_hash}})
  • DCAS/BISG audit dataset (84.9% Hispanic classification failure, N=58,220)
  • PSID variable registry (6 waves, benefits denied due to non-citizenship)
  • 15 veteran case files (MNV-01 through MNV-15, verification tiers T1–T4)
  • Electronic footprint manifest (SIP-ready, PREMIS-compatible)

The research is stress-tested against [INSTITUTION]'s own holdings via FOIA 
request [{{foia_case_number}}]. We invite independent verification.

Submission accession ID and electronic receipt requested per our footprint protocol.

[SIGNATURE BLOCK]
```

### Template B — Grant Funder
```
Subject: Letter of Inquiry — The Mathematics of Vietnam Research Infrastructure

Dear [NAME],

[INSTITUTION]'s commitment to [FUNDER_FOCUS] makes this project a direct match.

In brief: the U.S. Department of Defense's own casualty database — audited using 
the same BISG methodology the CFPB applies in fair-lending enforcement — shows 
an 84.9% classification failure for Hispanic Vietnam casualties. The same 
government's PSID documents six consecutive survey waves of benefits denied to 
non-citizen veterans.

*The Mathematics of Vietnam* places these administrative failures inside a 
245,000-word literary manuscript scored at the highest tier of our behavioral 
analytics system. The story earns the evidence.

I am requesting {{ask_amount}} to support [DELIVERABLE_1], [DELIVERABLE_2], 
and [DELIVERABLE_3].

Full proposal available upon request. Evidentiary packet attached.

[SIGNATURE BLOCK]
```

### Template C — Policy / Academic
```
Subject: Policy Brief Request — Non-Citizen Veteran Benefits Denial: PSID Evidence

Dear [NAME],

I am writing to request a briefing appointment with [DEPARTMENT] to present 
findings from a six-wave longitudinal analysis of non-citizen veteran benefits 
denial using PSID restricted data (ER16235, ER16270, ER20181, ER20216, 
ER23782, ER23817).

Key finding: across six PSID survey waves spanning [YEARS], [N] non-citizen 
veterans reported benefits denial attributable directly to citizenship status — 
a statutory gap that has never been the subject of targeted legislative review.

Supporting documentation includes 15 cross-verified veteran case files and a 
full DCAS/BISG audit of Vietnam-era casualty classifications.

I would welcome 30 minutes to present the evidence.

[SIGNATURE BLOCK]
```

---

## SECTION 7: RESPONSE PROTOCOL

| Response Type | Action | Timeline | Log Update |
|---------------|--------|----------|------------|
| Accession ID received | Log as `accepted`, request PREMIS fixity report | 48 hours | `status: accepted`, `submission_id: [ID]` |
| Acknowledgment only | Send follow-up with full packet if not already sent | 2 weeks | `status: under_review` |
| Request for more info | Respond within 5 business days with specific exhibit | 5 days | Add `notes` entry |
| Rejection | Log as `declined`, note reason, identify alternative institution | 1 week | `status: declined`, `notes: reason` |
| No response (30 days) | Send one follow-up; if no response, archive and move to next | Day 30 | `status: archived` |
| Grant LOI requested | Full proposal due within window | Per funder | Grant pipeline updated |
| Meeting requested | Prepare 10-slide deck + 1-page summary | ASAP | Calendar entry + prep checklist |

---

## SECTION 8: GRANT APPLICATION TIMELINE

| Funder | Type | Submission Window | Status | Ask |
|--------|------|-------------------|--------|-----|
| NEH Scholarly Editions | Federal | November 2026 | Planned | $150K |
| NEA Literature | Federal | Spring 2026 | Planned | $35K |
| Ford Foundation | Foundation | Rolling | Planned | $350K |
| MacArthur Foundation | Foundation | Rolling | Planned | $200K |
| USC Sol Price School | Internal | Rolling | Priority | $75K |
| Vietnam Veterans of America Foundation | Nonprofit | Rolling | Planned | $50K |
| California Humanities | State | Spring 2026 | Planned | $25K |

**Grant narrative core (paste-ready for all applications):**
> *The Mathematics of Vietnam* combines a 245,000-word literary manuscript with a forensic evidentiary infrastructure — DCAS/BISG audit, PSID longitudinal registry, TruthEngine360 deportation cycle database, and LITCENTRAL behavioral analytics — to document the administrative and narrative exclusion of Chicano and non-citizen veterans from the official record of the Vietnam War. The project's BISG-audited DCAS finding (84.9% Hispanic casualty classification failure across 58,220 records) employs the same methodology used by the CFPB in fair-lending enforcement, making the manuscript's historical claims independently verifiable through federal government databases.

---

## SECTION 9: MEDIA & ACADEMIC OUTREACH

### Academic Journal Targets (Priority Order)
1. *Journal of American Ethnic History* — BISG/DCAS methodology article
2. *Latino Studies* (Palgrave) — LITCENTRAL behavioral analytics article  
3. *Armed Forces & Society* — Non-citizen veteran benefits denial article
4. *Digital Humanities Quarterly* — LITCENTRAL + TruthEngine360 as forensic ecosystem

### Article Argument (recommended — strongest for journal submission)
**Title:** "Correcting the Record by Permitting It: LITCENTRAL, TruthEngine360, and the Forensic Infrastructure of a Hidden Military History"

**Argument:** The manuscript's evidentiary infrastructure (LITCENTRAL behavioral analytics + TruthEngine360 deportation cycle mapping) constitutes a reproducible forensic methodology for literary-historical research — one that converts narrative claims into institutionally verifiable findings by routing them through the government's own administrative systems.

**Length:** 20–22 pages (7,000–8,500 words)
**Sections:** Abstract → Problem Statement → BISG/DCAS Methodology → PSID Variable Registry → TruthEngine360 Architecture → LITCENTRAL Scoring → Case Evidence (MNV-03, MNV-05) → Institutional Submission Protocol → Implications → Conclusion

---

## SECTION 10: NOTION WORKSPACE ARCHITECTURE

### 10.1 — Page Hierarchy

```
SGT Ramos: The Mathematics of Vietnam
│
├── 📋 Dashboard (Home)
│   ├── KPI Summary (linked database views)
│   ├── Phase Status (Phase 1 / 2 / 3 indicator)
│   └── Quick Links (GitHub PR, proposal page, footprint log)
│
├── 🏛️ Institution CRM
│   ├── All Institutions (full table)
│   ├── Tier 1 — Archives (filtered view)
│   ├── Tier 2 — Funders (filtered view)
│   ├── Tier 3 — Academic (filtered view)
│   ├── Tier 4 — Media (filtered view)
│   └── Kanban: By Status
│
├── 📬 Submission Log
│   ├── All Submissions (table)
│   ├── By Phase (grouped view)
│   ├── Footprint Confirmations (filtered: has accession ID)
│   └── Pending Follow-ups (filtered: >14 days, no response)
│
├── 💰 Grant Pipeline
│   ├── All Funders (table)
│   ├── Calendar: Deadlines
│   ├── Active Applications (filtered)
│   └── Grant Narrative Library
│
├── 🗂️ Case File Gallery
│   ├── MNV-01 through MNV-15 (gallery view)
│   ├── Verification Tier Filter
│   └── Chapter Cross-Reference Index
│
├── ✉️ Message Library
│   ├── Template A — Archive
│   ├── Template B — Grant Funder
│   ├── Template C — Policy/Academic
│   └── Approved Copy Blocks (by keyword)
│
├── 📅 Content Calendar
│   ├── Submission Schedule
│   ├── Grant Deadlines
│   ├── Follow-up Queue
│   └── Journal Submission Windows
│
└── 📊 Analytics
    ├── Acknowledgment Rate Tracker
    ├── Phase 1 KPI Review
    └── LITCENTRAL Score Summary
```

### 10.2 — Institution CRM Database Schema

| Property Name | Type | Notes |
|---------------|------|-------|
| Name | Title | Institution name |
| Institution ID | Text | INST-0001 format |
| Type | Select | Archive / University / Foundation / Federal / Media |
| Tier | Select | Tier 1 / Tier 2 / Tier 3 / Tier 4 |
| Focus Area | Multi-select | Veterans / Chicano / Policy / Literary / Data |
| Status | Select | Planned / Submitted / Under Review / Accepted / Declined / Archived |
| Contact Name | Text | Primary contact |
| Contact Role | Text | Title |
| Contact Email | Email | |
| Submission Portal | URL | |
| Website | URL | |
| Stress Test Claim | Text | Which FOIA/database claim this institution can verify |
| Verification Weight | Number | 0.0–1.0 |
| Submission Date | Date | |
| Submission ID | Text | Accession / portal confirmation ID |
| SHA-256 Hash | Text | Manuscript hash at time of submission |
| Last Contact | Date | |
| Response Due | Date | 30 days from submission |
| Phase | Select | Phase 1 / Phase 2 / Phase 3 |
| Notes | Text | |
| Footprint Log | Relation | → Submission Log database |

### 10.3 — Submission Log Database Schema

| Property Name | Type | Notes |
|---------------|------|-------|
| Submission Title | Title | "[INST ID] — [Institution Name] — [Date]" |
| Institution | Relation | → Institution CRM |
| Submission Date | Date | |
| Transmission Method | Select | Email / Portal / Physical / API |
| Packet Contents | Multi-select | Manuscript / DCAS Audit / PSID Registry / Case Files / Footprint Manifest |
| Accession ID | Text | Assigned by institution |
| SHA-256 Hash | Text | |
| Custodian Declaration | Checkbox | Signed and attached? |
| Email Headers Saved | Checkbox | PDF/A saved? |
| SIP Submitted | Checkbox | |
| AIP Confirmed | Checkbox | |
| DIP URL | URL | Public dissemination URL if assigned |
| DOI / Handle | Text | |
| Status | Select | Sent / Acknowledged / Accepted / Declined / Archived |
| Follow-up Due | Date | Auto: submission date + 30 days |
| Notes | Text | |

### 10.4 — Grant Pipeline Database Schema

| Property Name | Type | Notes |
|---------------|------|-------|
| Funder | Title | |
| Program Name | Text | |
| Type | Select | Federal / Foundation / State / Internal / Nonprofit |
| Status | Select | Planned / LOI Submitted / Full Proposal / Under Review / Awarded / Declined |
| Ask Amount | Number | USD |
| Deadline | Date | |
| Submission Portal | URL | |
| Program Officer | Text | |
| Contact Email | Email | |
| Narrative Version | Select | NEH / Ford / MacArthur / USC / NEA / Veterans |
| Emphasis | Text | Which funder-specific angle to lead with |
| Deliverables | Text | What this grant funds |
| Submitted Date | Date | |
| Submission ID | Text | |
| Decision Date | Date | |
| Notes | Text | |

### 10.5 — Recommended Notion Views to Configure

| Database | View Name | View Type | Filter / Group By |
|----------|-----------|-----------|-------------------|
| Institution CRM | All Institutions | Table | None |
| Institution CRM | Submission Kanban | Board | Group by Status |
| Institution CRM | Tier 1 Priority | Table | Filter: Tier = Tier 1 |
| Institution CRM | Phase 1 Queue | Table | Filter: Phase = Phase 1, Status = Planned |
| Submission Log | Active Submissions | Table | Filter: Status ≠ Archived |
| Submission Log | Footprint Confirmed | Table | Filter: Accession ID is not empty |
| Submission Log | Follow-up Queue | Table | Filter: Follow-up Due ≤ today, Status = Sent |
| Grant Pipeline | Calendar | Calendar | Date: Deadline |
| Grant Pipeline | Active | Board | Group by Status |
| Case File Gallery | By Tier | Gallery | Group by Verification Tier |
| Content Calendar | Timeline | Timeline | Date: Submission Date |

### 10.6 — Notion Automation Triggers (native or Zapier)

| Trigger | Action |
|---------|--------|
| Institution Status → Submitted | Set Follow-up Due = Today + 30 days |
| Institution Status → Accepted | Create Submission Log entry with accession field |
| Grant Deadline < 14 days | Send reminder notification |
| Submission Status = Sent for 30 days | Flag as "Pending Follow-up" |
| New Case File added | Add to Discovery Index cross-reference |

---

## SECTION 11: KPIs & SUCCESS METRICS

### Phase 1 Gate (must hit before Phase 2 launch)
- [ ] ≥3 Tier 1 institutions: submission confirmed
- [ ] ≥1 accession ID received
- [ ] ≥15% acknowledgment rate across all Phase 1 submissions
- [ ] ≥1 grant submission sent with full evidentiary packet
- [ ] PSID restricted data application submitted
- [ ] USC Sol Price meeting requested

### Phase 2 Gate (must hit before Phase 3 launch)
- [ ] ≥20 submissions logged with footprint entries
- [ ] ≥1 grant under active review
- [ ] Academic journal submission sent
- [ ] Python automation pipeline validated (generate + assemble + log)
- [ ] Elasticsearch institution-directory index live

### Overall Success Metrics (12-month horizon)
| Metric | Target |
|--------|--------|
| Institutional submissions | 50+ |
| Tier 1 accessions confirmed | 5+ |
| Grant applications submitted | 7 |
| Grant dollars awarded | $150K+ |
| Academic journal: under review | 1 |
| DOI/handle assigned | 1 |
| Media placements | 2+ |
| Policy briefings delivered | 1+ |

---

## SECTION 12: TEAM ROLES & RESPONSIBILITIES

| Role | Responsibility | Owner |
|------|---------------|-------|
| Principal Investigator | All content, sign-off on all submissions, legal framing | Gabriel Arce |
| Submission Coordinator | Packet assembly, portal accounts, footprint log | TBD |
| Data Analyst | PSID regression, DCAS audit updates, Elasticsearch | TBD |
| Grant Writer | LOI + full proposals, funder-specific narrative versions | TBD / Gabriel Arce |
| Archivist | SIP/AIP/DIP protocol, PREMIS metadata, custodian declarations | TBD |
| Legal Advisor | FOIA requests, evidentiary framing review | Consult |

---

## APPENDIX: QUICK REFERENCE

**84.9%** — DCAS Hispanic casualty classification failure (N=58,220)  
**349** — casualties coded Hispanic in DCAS  
**~2,309–3,000** — estimated actual Hispanic casualties (BISG methodology)  
**6** — PSID waves documenting benefits denied to non-citizen veterans  
**15** — veteran case files (MNV-01 through MNV-15, tiers T1–T4)  
**245,000** — manuscript word count  
**0.938** — Cronbach's α (LITCENTRAL pilot, N=11 chapters)  
**88.3** — AutoCrit overall score  
**R²=0.947** — LITCENTRAL Omega composite model fit  
**21** — chapters at Omega Elite tier  

**GitHub:** `gama0218-lgtm/claude`, branch `claude/charming-cerf-ADEWO`, PR #1  
**Local proposal page:** `/home/user/sgt-ramos-proposal.html`  
**Elasticsearch endpoint:** rotate credentials before use (see security note in project history)
