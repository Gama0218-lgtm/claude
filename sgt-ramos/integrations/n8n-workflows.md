# AUMER Foundation — n8n Workflow Specs

Import or build these in your n8n Cloud account (app.n8n.cloud).
Build Workflow 1 first. Prove it sends. Then add 2 and 3.

---

## WORKFLOW 1: Daily Brief
**Trigger:** Schedule — every day at 7:30am Pacific  
**Purpose:** Morning status report to Gabriel via Telegram + WhatsApp

### Nodes (in order):

**Node 1 — Schedule Trigger**
- Type: Schedule Trigger
- Interval: Daily at 7:30am (America/Los_Angeles)

**Node 2 — Read Notion Control Room**
- Type: Notion (official node)
- Operation: Get Many Pages
- Database: Control Room (ID: 12a40dc48e854bbb839838b69bf4fb5b)
- Filter: Status = "Blocked" OR Status = "Check" OR Due Date <= today

**Node 3 — Read Submission Directory**
- Type: Notion
- Operation: Get Many Pages
- Database: Submission Directory (ID: f8024ec76cab4541a2394db977a8d3c3)
- Filter: Stage = "Sent" AND Date sent <= 14 days ago

**Node 4 — Read Grant Pipeline**
- Type: Notion
- Operation: Get Many Pages
- Database: Grant Pipeline (ID: 0643034762764656b6960433b4e01f7f)
- Filter: Deadline <= today + 14 days AND Status = "Planned"

**Node 5 — Perplexity Sonar (new signals)**
- Type: HTTP Request
- Method: POST
- URL: https://api.perplexity.ai/chat/completions
- Headers: Authorization: Bearer {{$env.PERPLEXITY_API_KEY}}
- Body:
```json
{
  "model": "sonar",
  "messages": [
    {
      "role": "system",
      "content": "You are a research monitor for a veterans advocacy organization. Search for: (1) news about deported US veterans in the last 24 hours, (2) any updates on Vietnam-era casualty record audits, (3) any FOIA policy changes affecting veteran records. Return a brief summary with source URLs. Label all findings as unverified."
    },
    {
      "role": "user",
      "content": "What are the latest developments on deported veterans, Vietnam casualty records, and veteran FOIA requests in the past 24 hours?"
    }
  ]
}
```

**Node 6 — Format Brief**
- Type: Code (JavaScript)
- Purpose: Combine all inputs into the brief format
```javascript
const controlRoom = $('Read Notion Control Room').all();
const followUps = $('Read Submission Directory').all();
const grants = $('Read Grant Pipeline').all();
const signals = $('Perplexity Sonar').first().json.choices[0].message.content;

let brief = `*AUMER DAILY BRIEF — ${new Date().toLocaleDateString('en-US', {weekday:'long', month:'long', day:'numeric'})}*\n\n`;

// Section 1
brief += `*NEEDS ME TODAY*\n`;
if (controlRoom.length === 0) brief += `clear.\n`;
else controlRoom.forEach(item => {
  brief += `• ${item.json.properties['Task']?.title?.[0]?.plain_text || 'Item'} — ${item.json.properties['Status']?.select?.name || ''}\n`;
});

// Section 2
brief += `\n*FOLLOW-UPS DUE*\n`;
if (followUps.length === 0) brief += `clear.\n`;
else followUps.forEach(item => {
  brief += `• ${item.json.properties['Institution']?.title?.[0]?.plain_text} — sent ${item.json.properties['Date sent']?.date?.start}\n`;
});

// Section 3
brief += `\n*GRANT DEADLINES (next 14 days)*\n`;
if (grants.length === 0) brief += `clear.\n`;
else grants.forEach(item => {
  brief += `• ${item.json.properties['Funder']?.title?.[0]?.plain_text} — due ${item.json.properties['Deadline']?.date?.start}\n`;
});

// Section 4
brief += `\n*NEW SIGNALS (unverified — needs review)*\n`;
brief += signals.substring(0, 500) + '...\n';

brief += `\n_One thing to look at today: check Needs Me Today above._`;

return [{ json: { message: brief } }];
```

**Node 7 — Send Telegram**
- Type: Telegram
- Operation: Send Message
- Chat ID: {{$env.TELEGRAM_CHAT_ID}}
- Text: {{$json.message}}
- Parse Mode: Markdown

**Node 8 — Send WhatsApp** (via Twilio)
- Type: HTTP Request or Twilio node
- To: {{$env.WHATSAPP_NUMBER}}
- From: {{$env.TWILIO_WHATSAPP_FROM}}
- Body: {{$json.message}}

---

## WORKFLOW 2: Submission Follow-up Monitor
**Trigger:** Schedule — every day at 9:00am Pacific  
**Purpose:** Alert when an institution hasn't responded in 14+ days

### Nodes:

**Node 1 — Schedule Trigger**
- Daily at 9:00am Pacific

**Node 2 — Read Submission Directory**
- Notion → Get Many Pages
- Database: Submission Directory
- Filter: Stage = "Sent"

**Node 3 — Filter Overdue**
- Type: Code
```javascript
const items = $input.all();
const today = new Date();
const overdue = items.filter(item => {
  const sent = new Date(item.json.properties['Date sent']?.date?.start);
  const daysSince = (today - sent) / (1000 * 60 * 60 * 24);
  return daysSince >= 14;
});
return overdue;
```

**Node 4 — Send Telegram Alert** (only if overdue.length > 0)
- Message: `*FOLLOW-UP DUE* — {{institution name}} was sent {{X}} days ago. No response logged. Draft follow-up?`

---

## WORKFLOW 3: Research Pipeline
**Trigger:** Manual (webhook) or scheduled weekly  
**Purpose:** Pull cited research from Perplexity → save to Notion

### Nodes:

**Node 1 — Webhook Trigger** (or Schedule)
- Accepts: `{ "query": "research question here" }`

**Node 2 — Perplexity Deep Research**
- HTTP Request → Perplexity API
- Model: `sonar-deep-research`
- System prompt: "You are a forensic research assistant for a veterans advocacy project. Return a structured report with: key findings, source URLs, confidence level (High/Medium/Low), and what further verification is needed."
- User message: `{{$json.query}}`

**Node 3 — Save to Notion**
- Notion → Create Page
- Parent: Research folder under Command Center
- Title: `Research: {{$json.query}} — {{date}}`
- Content: Full Perplexity response
- Tags: Source = Perplexity, Status = Unverified, Date = today

**Node 4 — Telegram Alert**
- `*NEW RESEARCH SAVED* — "{{query}}" — unverified, needs Gabriel review. Check Notion.`

---

## ENVIRONMENT VARIABLES (set in n8n → Settings → Variables)

| Variable | Value source |
|----------|--------------|
| `NOTION_API_KEY` | notion.so/my-integrations |
| `PERPLEXITY_API_KEY` | perplexity.ai → Settings → API |
| `OPENAI_API_KEY` | platform.openai.com → API keys |
| `GEMINI_API_KEY` | console.cloud.google.com |
| `TELEGRAM_BOT_TOKEN` | BotFather on Telegram |
| `TELEGRAM_CHAT_ID` | Your Telegram user/group ID |
| `WHATSAPP_NUMBER` | Your WhatsApp number (E.164) |
| `TWILIO_ACCOUNT_SID` | twilio.com/console |
| `TWILIO_AUTH_TOKEN` | twilio.com/console |
| `TWILIO_WHATSAPP_FROM` | whatsapp:+14155238886 (Twilio sandbox) |
| `HUBSPOT_API_KEY` | hubspot.com → Settings → Integrations → API |
