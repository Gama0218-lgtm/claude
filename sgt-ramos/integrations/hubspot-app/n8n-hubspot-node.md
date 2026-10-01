# n8n HubSpot Node Configs — AUMER Foundation

All nodes use credential: **HubSpot API → AUMER Foundation Access Token**

---

## Node 1: Create/Update Contact (MNV Case)

```json
{
  "parameters": {
    "operation": "upsert",
    "resource": "contact",
    "additionalFields": {
      "email": "={{ $json.email }}",
      "firstName": "={{ $json.first_name }}",
      "lastName": "={{ $json.last_name }}"
    },
    "customPropertiesUi": {
      "customPropertiesValues": [
        { "property": "mnv_case_id", "value": "={{ $json.case_id }}" },
        { "property": "verification_tier", "value": "={{ $json.tier }}" },
        { "property": "project", "value": "SGT Ramos" }
      ]
    }
  },
  "type": "n8n-nodes-base.hubspot",
  "credentials": { "hubspotApi": { "name": "AUMER Foundation" } }
}
```

---

## Node 2: Create Deal (Grant Application)

```json
{
  "parameters": {
    "operation": "create",
    "resource": "deal",
    "additionalFields": {
      "dealName": "={{ $json.grant_name + ' — ' + $json.funder }}",
      "dealStage": "{{ $json.stage }}",
      "amount": "={{ $json.amount }}",
      "closeDate": "={{ $json.deadline }}"
    },
    "customPropertiesUi": {
      "customPropertiesValues": [
        { "property": "grant_type", "value": "={{ $json.grant_type }}" },
        { "property": "pi_name", "value": "Gabriel Arce" },
        { "property": "project", "value": "SGT Ramos" }
      ]
    }
  },
  "type": "n8n-nodes-base.hubspot",
  "credentials": { "hubspotApi": { "name": "AUMER Foundation" } }
}
```

---

## Node 3: Log FOIA Update (Note)

```json
{
  "parameters": {
    "operation": "create",
    "resource": "note",
    "body": "FOIA Update — {{ $json.agency }}\n\nStatus: {{ $json.status }}\nTracking: {{ $json.tracking_number }}\nDate: {{ $now.format('YYYY-MM-DD') }}\n\n{{ $json.details }}",
    "associations": {
      "contactIds": [],
      "dealIds": ["={{ $json.deal_id }}"]
    }
  },
  "type": "n8n-nodes-base.hubspot",
  "credentials": { "hubspotApi": { "name": "AUMER Foundation" } }
}
```

---

## Node 4: Timeline Event (Submission Sent)

Uses HTTP Request node (HubSpot node doesn't expose timeline API directly):

```json
{
  "parameters": {
    "method": "POST",
    "url": "https://api.hubapi.com/crm/v3/timeline/events",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "hubspotApi",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [
        { "name": "Content-Type", "value": "application/json" }
      ]
    },
    "sendBody": true,
    "bodyParameters": {
      "parameters": [
        { "name": "eventTemplateId", "value": "{{ $json.template_id }}" },
        { "name": "objectId", "value": "={{ $json.contact_id }}" },
        { "name": "tokens", "value": "={{ JSON.stringify({ submission_target: $json.institution, sent_date: $now.format('YYYY-MM-DD'), method: $json.method }) }}" }
      ]
    }
  },
  "type": "n8n-nodes-base.httpRequest",
  "credentials": { "hubspotApi": { "name": "AUMER Foundation" } }
}
```

---

## Custom Properties to Create in HubSpot

Go to HubSpot Settings → Properties → Create property for each:

### Contact Properties
| Property Name | Internal Name | Type | Used for |
|---|---|---|---|
| MNV Case ID | `mnv_case_id` | Single-line text | MNV-01 through MNV-15 |
| Verification Tier | `verification_tier` | Dropdown (T1/T2/T3/T4) | Evidence level |
| Project | `project` | Single-line text | SGT Ramos / First Responder |
| Branch of Service | `branch_of_service` | Dropdown | Army, Navy, USMC, etc. |
| Tour Dates | `tour_dates` | Single-line text | e.g. 1968-1969 |

### Deal Properties
| Property Name | Internal Name | Type | Used for |
|---|---|---|---|
| Grant Type | `grant_type` | Dropdown | NEH / Ford / Mellon / Other |
| PI Name | `pi_name` | Single-line text | Principal Investigator |
| Project | `project` | Single-line text | Links to manuscript |
| FOIA Tracking # | `foia_tracking_number` | Single-line text | VA/DHS request IDs |

---

## Pipeline Stage IDs (Deals)

Get your actual stage IDs from:
```
GET https://api.hubapi.com/crm/v3/pipelines/deals
Authorization: Bearer {HUBSPOT_ACCESS_TOKEN}
```

Then map them in your n8n workflow:
```
Prospect      → stage ID for "Identifying / Researching"
In Prep       → stage ID for "Writing Application"
Submitted     → stage ID for "Submitted — Awaiting Decision"
R&R           → stage ID for "Revise and Resubmit"
Funded        → stage ID for "Funded — Active"
Declined      → stage ID for "Declined"
```
