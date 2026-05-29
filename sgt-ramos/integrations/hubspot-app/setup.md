# HubSpot Integration Setup — AUMER Foundation

Hub ID: **46948033**  
App file: `sgt-ramos/integrations/hubspot-app/app-hsmeta.json`

---

## Two paths — you need BOTH

| Path | What it fixes | Time |
|---|---|---|
| **A — Floor OAuth** | Floor reads/writes HubSpot inside Notion AI | 60 seconds |
| **B — Private App token** | n8n, Python scripts, any automation | 5 minutes |

They don't overlap. Path A is for Floor's browser session. Path B is for everything headless.

---

## Path A — Floor OAuth (do this first)

1. Open Notion AI (Floor / ~Flowriter)
2. Settings → Tools and access → HubSpot → **Connect**
3. Sign in with the account tied to hub **46948033**
4. Done — Floor can now read contacts, deals, and companies

---

## Path B — Private App Access Token (for n8n + scripts)

### Option 1: HubSpot UI (recommended — no CLI needed)

1. Go to **HubSpot Settings → Integrations → Private Apps**
2. Click **Create a private app**
3. Name: `AUMER Foundation`
4. Scopes tab — add all scopes listed in `app-hsmeta.json` → requiredScopes
5. Click **Create app**
6. Copy the **Access Token** (shown once — paste immediately)
7. Add to n8n: **Credentials → HubSpot API → Access Token**

### Option 2: CLI + app-hsmeta.json (developer path)

Use this if you want version-controlled app config or plan to add CRM extensions.

```bash
# Run on your LOCAL Windows machine (not cloud)
npm install -g @hubspot/cli@latest
hs init                          # authenticates to hub 46948033

# Create app project
hs create app aumer-foundation
cd aumer-foundation

# Replace generated app-hsmeta.json with the one in this repo
# Then deploy:
hs upload
```

After `hs upload`, go to the app in your HubSpot developer portal → **Auth** tab → copy the **Access Token**.

---

## n8n Credential Setup

Once you have the Access Token:

1. n8n → **Credentials** → New → **HubSpot API**
2. Paste the Access Token
3. Test — should return your hub info
4. All HubSpot nodes in n8n will use this credential

---

## Scope Map — What Each Scope Covers

| Scope | Used by |
|---|---|
| `crm.objects.contacts.read/write` | MNV case contacts, researchers, veterans |
| `crm.objects.companies.read/write` | USC, LOC, grant funders, archives |
| `crm.objects.deals.read/write` | Grant applications, submissions pipeline |
| `crm.objects.notes.read/write` | Research log, FOIA updates, outreach log |
| `crm.schemas.*.read` | Custom property access for above objects |
| `crm.objects.owners` | Assign records to Gabriel |
| `files` | Attach PDFs, FOIA docs, manuscript excerpts |
| `timeline` | Log events: submission sent, FOIA escalated, etc. |

---

## CRM Object Map for AUMER

```
Contacts
  └── MNV Veterans (MNV-01 through MNV-15)
  └── Researchers (Dr. Romley, González, etc.)
  └── Archive contacts (USC, LOC, NARA)

Companies
  └── USC Sol Price School
  └── LOC Veterans History Project
  └── NARA (National Archives)
  └── Grant Funders (NEH, Ford, etc.)

Deals
  └── Grant Applications (pipeline)
  └── Manuscript Submissions
  └── FOIA Requests (VA BIRLS, DHS ENFORCE)

Notes
  └── FOIA tracking updates
  └── Submission confirmations
  └── Research session logs

Timeline Events
  └── FOIA escalation sent (June 2, 2026)
  └── USC Libraries submission sent
  └── LOC VHP submission sent
```

---

## Environment Variable

Once you have the token, add to n8n:

```
Variable name:  HUBSPOT_ACCESS_TOKEN
Value:          pat-na1-xxxx...  (your actual token)
```

And to your local `.env` for the Python client:

```bash
setx HUBSPOT_ACCESS_TOKEN "pat-na1-xxxx..."
```
