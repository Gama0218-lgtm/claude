# Artifact Submission Package
## *SGT George Ramos: The Mathematics of Vietnam*
### Institutional Deposit, Stress-Test Protocol, and Electronic Footprint Roadmap

---

## I. What This Package Is

This is a standardized submission package for depositing *SGT George Ramos: The Mathematics of Vietnam* with institutions as a **documented cultural and scholarly artifact**. The deposit simultaneously:

1. Creates a timestamped, multi-source electronic footprint establishing the manuscript's provenance
2. Initiates the "manicule stress test" — presenting the manuscript's evidentiary claims to institutions that hold the underlying records, inviting independent verification
3. Positions the project for academic review, grant consideration, and archival preservation
4. Documents the author's methodology and transparency standards for institutional audiences

The goal is not simply to submit a manuscript for publication consideration. It is to place the manuscript **on record** — in the legal and archival sense — as a verifiable artifact tied to specific institutional data sources.

---

## II. The Electronic Footprint Protocol

Every institutional submission follows this six-step chain to create an auditable provenance record.

### Step 1 — Prepare Submission Files
- Finalize and date-stamp the manuscript version (e.g., `v97_UPDATED_FINAL_[DATE].pdf`)
- Generate SHA-256 hash of the final PDF: `sha256sum v97_UPDATED_FINAL_[DATE].pdf`
- Record hash, file size, and timestamp in `submission-manifest.json`
- Save a copy of the manifest alongside the manuscript

### Step 2 — Transmission
- Send submission email from a controlled, documented email account
- Include the SHA-256 hash and file version in the email body
- Preserve a copy of the sent email with full headers
- Record: sender, recipient, subject line, timestamp, and file attachments in the submission log

**Legal value:** Establishes intent, date, and first custody event. The preserved email header is the equivalent of a postmark.

### Step 3 — Portal Registration
- Create an account on the institutional submission portal (if applicable)
- Record: portal URL, account username, registration date, confirmation email
- Screenshot or PDF the account confirmation page

**Legal value:** Ties the depositor's identity to the institutional submission record.

### Step 4 — Upload Event
- Upload manuscript file(s), metadata form, and sidecar manifest
- Preserve: accession number, upload receipt, or confirmation ID issued by the portal
- Record upload timestamp
- Screenshot the upload confirmation page

**Legal value:** Creates the primary electronic footprint. The accession number is the institutional acknowledgment of receipt.

### Step 5 — Repository Ingest (for archival institutions)
- The institution converts the submission into preservation packages:
  - **SIP** (Submission Information Package) — what you send
  - **AIP** (Archival Information Package) — what they preserve
  - **DIP** (Dissemination Information Package) — what becomes publicly accessible
- Preservation metadata, fixity checks, and provenance records are attached at this stage

**Legal value:** The SIP→AIP conversion is the moment the institution takes custody. This is the archival equivalent of a deed of gift.

### Step 6 — Electronic Footprint Confirmation
- Compile the full record: email timestamp + hash + portal receipt + accession number
- Save to `electronic-footprint-log.json` with one entry per institution
- The log is the project's chain of custody document

---

## III. The Manicule Stress Test

The manicule (☞) is the historical pointing hand — the typographic gesture that says *look here*. The stress test uses the same gesture: it points institutional reviewers at their own data and invites them to verify or falsify the manuscript's claims.

### What the Stress Test Presents

1. **The manuscript** — or a representative sample (1–3 Omega Elite chapters, typically Chapter 8, Chapter 17, Chapter 29)
2. **The evidentiary layer** — a two-page summary of LITCENTRAL scoring, DCAS audit findings, and TruthEngine360 case documentation
3. **The specific claim** — directed at this institution's holdings (e.g., for NARA: "Your DCAS file coded 349 Hispanic casualties; our BISG audit finds 2,309–3,000")
4. **The invitation** — "We are not asking you to take our word. We are asking you to look at your own records."

### What the Stress Test Asks of Reviewers

- Verify a sample of the manuscript's historical claims against the institution's holdings
- Confirm or correct the BISG methodology as applied to DCAS
- Identify any records in their collection that would strengthen or complicate the case documentation (MNV-01–MNV-15)
- Provide a written response (for the record) or an acknowledgment of receipt

### Why This Is Legally and Academically Sound

A stress test against institutional records is standard scholarly practice. Presenting a historical claim to the institution that holds the underlying records — and preserving their response — creates a multi-party evidentiary chain. Even a non-response is meaningful: it documents that the institution was presented with the claim and did not correct it.

---

## IV. Submission Package Contents

Each institutional submission packet includes the following, customized by tier:

### Tier 1 — Archival Deposit (National Archives, Library of Congress, USC Libraries)
- Cover letter (archival framing)
- Manuscript PDF (full or sample chapters)
- LITCENTRAL dashboard export (one-page summary)
- TruthEngine360 case registry summary (MNV-01–MNV-15)
- DCAS audit findings brief (2 pages)
- Submission manifest with SHA-256 hash
- Electronic footprint log template

### Tier 2 — Academic Review (Universities, Research Centers)
- Cover letter (scholarly framing)
- Abstract and project overview (1 page)
- Methods summary: LITCENTRAL + TruthEngine360 (2 pages)
- Sample chapters: 1–2 Omega Elite chapters
- DCAS audit findings brief
- Bibliography of institutional sources

### Tier 3 — Grant Application (Foundations, Federal Programs)
- Cover letter (funding framing)
- Full grant proposal (from Grant Proposal Framework)
- Project overview with LITCENTRAL metrics
- Budget narrative
- Letters of support (when available)

### Tier 4 — Policy Outreach (Congressional Offices, Veterans' Organizations)
- One-page executive summary
- DCAS audit findings (headline numbers only)
- Case summaries for 3–5 named cases (MNV-01, MNV-04, MNV-05 recommended)
- Request: committee testimony, staff briefing, or document review

---

## V. Cover Letter Template

```
[Date]

[Recipient Name]
[Title]
[Institution]
[Address]

Dear [Recipient],

I am writing to submit *SGT George Ramos: The Mathematics of Vietnam* — 
a 245,000-word literary-historical novel documenting the service, displacement, 
and deportation of Chicano and non-citizen U.S. Vietnam veterans — for 
[archival consideration / scholarly review / grant consideration].

[Institution-specific paragraph: why this institution, what their holdings 
contribute, what the stress test asks of them.]

This project is unusual in one respect: the manuscript's historical claims have 
been stress-tested against federal databases — the Pentagon Defense Casualty 
Analysis System (DCAS), the Panel Study of Income Dynamics (PSID), NARA records, 
and FOIA-disclosed VA documents — using the same methodologies employed in 
federal program evaluation and fair-lending enforcement. Applying Bayesian 
Improved Surname Geocoding (BISG) to DCAS, the project documents an estimated 
84.9% Hispanic casualty misclassification rate across 58,220 Vietnam-era records.

I am not asking [Institution] to take my word. I am presenting the government's 
own data — audited by the government's own preferred methodology — and inviting 
your institution to verify, correct, or extend these findings against your own 
holdings.

[Brief paragraph on deliverables: what you're depositing, what you're requesting, 
timeline.]

Enclosed: [list of package contents by tier]

I am available at [contact] to discuss the project or answer questions about 
the methodology.

Respectfully,

Gabriel Arce
[Affiliation, if applicable]
[Email]
[Phone]
```

---

## VI. Institution Directory Schema

The directory of target institutions is tracked as a structured log. One row per institution.

```json
{
  "institution_id": "INST-0001",
  "name": "",
  "type": "university | foundation | archive | gov_agency | think_tank | veterans_org",
  "focus_area": "military | chicano_studies | humanities | public_policy | immigration | veterans",
  "tier": "1 | 2 | 3 | 4",
  "contact_name": "",
  "contact_role": "",
  "contact_email": "",
  "submission_portal_url": "",
  "record_type_interest": "",
  "stress_test_claim": "",
  "last_contact_date": "",
  "submission_id": "",
  "footprint_log_entry": "",
  "status": "planned | submitted | under_review | accepted | declined | archived",
  "notes": ""
}
```

---

## VII. Electronic Footprint Log Schema

```json
{
  "institution_id": "INST-0001",
  "institution_name": "",
  "submission_date": "",
  "sender_email": "",
  "recipient_email": "",
  "subject_line": "",
  "file_name": "",
  "sha256_hash": "",
  "file_size_bytes": 0,
  "portal_url": "",
  "portal_account": "",
  "upload_receipt_id": "",
  "upload_timestamp": "",
  "accession_number": "",
  "response_received": false,
  "response_date": "",
  "response_summary": "",
  "notes": ""
}
```

---

## VIII. Priority Institution List (First Wave)

These 20 institutions represent the highest-value first-wave targets across all four tiers.

### Archival (Tier 1)
1. USC Libraries Special Collections — Chicano Studies Research Center
2. Library of Congress — American Folklife Center
3. National Archives and Records Administration (NARA) — Military Records
4. UC Santa Barbara — Chicano Studies Institute
5. Smithsonian National Museum of American History — Armed Forces collections

### Academic (Tier 2)
6. USC Sol Price School of Public Policy
7. UCLA Chicano Studies Research Center
8. UC Berkeley Institute for the Study of Societal Issues
9. UT Austin Center for Mexican American Studies
10. University of New Mexico Latin American & Iberian Institute

### Grant (Tier 3)
11. National Endowment for the Humanities — Scholarly Editions program
12. Ford Foundation — Civic Engagement and Government program
13. MacArthur Foundation — Criminal Justice program
14. California Humanities (NEH affiliate)
15. Mellon Foundation — Humanities for All program

### Policy/Veterans (Tier 4)
16. Congressional Hispanic Caucus — research staff
17. Senate Veterans' Affairs Committee — minority staff
18. Vietnam Veterans of America — national office
19. Swords to Plowshares (deported veterans legal services)
20. MALDEF — national office

---

## IX. Automation Roadmap

The submission workflow is designed for semi-automation at scale (200–300 institutions).

**Phase 1 (Manual, 10–20 institutions):**
- Hand-build first 20 directory entries
- Send first batch manually, monitor for responses
- Refine cover letter based on response patterns
- Validate footprint log format against real submission receipts

**Phase 2 (Template automation, 20–100 institutions):**
- Script generates cover letters from directory entries + template
- Script pre-fills submission forms where portals allow
- All outputs staged for human review before send
- Footprint log auto-populated from sent email metadata

**Phase 3 (Scale, 100–300 institutions):**
- Full pipeline with human spot-check on 10% of submissions
- Response tracking automated via email parsing
- Directory updated weekly with status changes
- Quarterly audit of footprint log against submitted files

**Tech stack:** Python (email generation, PDF manipulation, SHA-256 hashing), Elasticsearch (institution directory index), Google Sheets (human-readable status dashboard), Gmail API or SMTP (controlled sending account).
