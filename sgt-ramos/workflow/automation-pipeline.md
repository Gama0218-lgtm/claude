# Submission Automation Pipeline
## SGT George Ramos — Institutional Outreach at Scale

---

## Overview

This pipeline converts the institution directory into an automated outreach and tracking system. The goal is 200–300 institutional submissions with individual provenance records (electronic footprints) for each, scalable from a single researcher.

Three phases: Manual (1–20), Template-automated (20–100), Full scale (100–300).

---

## Phase 1 — Manual First Wave (Institutions 1–20)

**Goal:** Validate the cover letter, test the stress-test framing, and confirm the electronic footprint protocol works before automating.

**Steps:**
1. Open `institution-directory.json` — sort by `tier` then `verification_weight` descending
2. For each institution (start with INST-0001 through INST-0010):
   a. Fill the cover letter template from `artifact-submission-package.md`
   b. Assemble the tier-appropriate packet (Tier 1/2/3/4 contents defined in that doc)
   c. Generate SHA-256 hash of the packet PDF: `sha256sum [filename].pdf`
   d. Send from the controlled email account
   e. Preserve sent email with headers
   f. Log the submission in `electronic-footprint-log.json`
3. Wait 5–7 business days for responses
4. Update `status` field in `institution-directory.json`
5. Analyze response patterns before scaling

**Validation criteria before Phase 2:**
- At least 3 institutional acknowledgments received
- At least 1 substantive response (even a no)
- Cover letter framing confirmed as professionally appropriate
- Electronic footprint log entries confirmed complete

---

## Phase 2 — Template Automation (Institutions 20–100)

**Tech stack:** Python 3.x, smtplib or Gmail API, PyPDF2 or reportlab, hashlib

### 2a. Cover Letter Generator

```python
# generate_cover_letter.py
import json
from string import Template

def generate_cover_letter(institution: dict, template_path: str) -> str:
    with open(template_path) as f:
        tmpl = Template(f.read())
    return tmpl.safe_substitute(
        institution_name=institution["name"],
        contact_name=institution.get("contact_name", "Director"),
        contact_role=institution.get("contact_role", ""),
        tier_specific_paragraph=get_tier_paragraph(institution),
        stress_test_claim=institution.get("stress_test_claim", ""),
        record_type_interest=institution.get("record_type_interest", ""),
        focus_area=", ".join(institution.get("focus_area", [])),
        date=date.today().strftime("%B %d, %Y")
    )

def get_tier_paragraph(institution: dict) -> str:
    tier_paragraphs = {
        1: "As an archival institution with holdings relevant to {record_type_interest}, "
           "{institution_name} is a logical site for this manuscript's formal deposit. "
           "The submission includes a SHA-256 verified file package and a complete "
           "electronic footprint record suitable for your preservation systems.",
        2: "As a research center focused on {focus_area}, {institution_name} is "
           "positioned to assess both the literary and methodological dimensions of "
           "this project. I am seeking scholarly feedback and, where appropriate, "
           "acknowledgment of receipt for manuscript under record.",
        3: "I am submitting this project for grant consideration. The attached "
           "proposal includes a full methods summary, deliverables timeline, and "
           "budget narrative tailored to your program priorities.",
        4: "I am reaching out to request a staff briefing or document review. "
           "The enclosed one-page summary presents the core findings in a form "
           "suitable for policy staff review."
    }
    t = institution.get("tier", 2)
    return tier_paragraphs.get(t, tier_paragraphs[2]).format(**institution)
```

### 2b. Packet Assembler

```python
# assemble_packet.py
import hashlib
import json
from datetime import datetime

def hash_file(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def assemble_packet(institution: dict, manuscript_pdf: str, output_dir: str) -> dict:
    """Assembles the submission packet and returns footprint metadata."""
    packet_hash = hash_file(manuscript_pdf)
    timestamp = datetime.utcnow().isoformat()
    submission_id = f"SUB-{institution['institution_id']}-{timestamp[:10]}"

    footprint = {
        "institution_id": institution["institution_id"],
        "institution_name": institution["name"],
        "submission_date": timestamp,
        "file_name": manuscript_pdf,
        "sha256_hash": packet_hash,
        "submission_id": submission_id,
        "status": "assembled",
        "upload_receipt_id": "",
        "accession_number": "",
        "response_received": False
    }
    return footprint
```

### 2c. Electronic Footprint Logger

```python
# footprint_log.py
import json
from pathlib import Path

FOOTPRINT_LOG = Path("electronic-footprint-log.json")

def append_footprint(entry: dict):
    log = []
    if FOOTPRINT_LOG.exists():
        with open(FOOTPRINT_LOG) as f:
            log = json.load(f)
    log.append(entry)
    with open(FOOTPRINT_LOG, "w") as f:
        json.dump(log, f, indent=2)

def update_footprint(submission_id: str, updates: dict):
    with open(FOOTPRINT_LOG) as f:
        log = json.load(f)
    for entry in log:
        if entry["submission_id"] == submission_id:
            entry.update(updates)
            break
    with open(FOOTPRINT_LOG, "w") as f:
        json.dump(log, f, indent=2)
```

### 2d. Run Script (Phase 2)

```bash
# run_phase2.sh
#!/bin/bash
python generate_cover_letter.py --institution-id $1 --template cover-letter-template.txt > /tmp/cover_letter.txt
python assemble_packet.py --institution-id $1 --manuscript manuscript_sample.pdf --output /tmp/packets/
python footprint_log.py --append /tmp/packets/$1_footprint.json
echo "Packet assembled for $1. Review /tmp/cover_letter.txt before sending."
```

**Human checkpoint:** All Phase 2 packets are reviewed by a human before sending. The script stages; the human sends.

---

## Phase 3 — Full Scale (100–300 Institutions)

**When to start Phase 3:** After Phase 2 response rate analysis confirms the cover letter and stress-test framing are working (target: >15% acknowledgment rate).

**Additions for Phase 3:**
- Email parsing for auto-updating `status` fields in the directory
- Response classification: acknowledged / substantive / declined / no-response
- Quarterly audit: pull all `status=submitted` entries older than 30 days, flag for follow-up
- Elasticsearch institution-directory index for search across all 300 entries
- Dashboard (Google Sheets or Kibana) showing submission status by tier and geography

---

## Electronic Footprint Log Schema

```json
[
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
    "submission_id": "",
    "response_received": false,
    "response_date": "",
    "response_summary": "",
    "notes": ""
  }
]
```

---

## Today's Checklist

- [ ] Fill contact details for INST-0001 through INST-0010 (USC, LOC, NARA, UCSB, Smithsonian, USC Price, UCLA, UCB, UT Austin, UNM)
- [ ] Draft cover letter for INST-0001 (USC Libraries) — use as template test
- [ ] Select 1–3 Omega Elite chapters for the evidence bundle PDF
- [ ] Run `sha256sum` on the manuscript PDF and record in footprint log
- [ ] Send INST-0001 submission manually — complete all 6 footprint steps
- [ ] Monitor for response (5–7 business days)
- [ ] Begin INST-0002 through INST-0005 after INST-0001 is confirmed sent
