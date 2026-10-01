# n8n Perplexity Node Configurations
## AUMER Project — HTTP Request node specs for all 3 workflows

All nodes use the `PERPLEXITY_API_KEY` environment variable.
Set it in n8n: **Settings → Variables → Add Variable**.

---

## WORKFLOW 1 — Daily Brief
### Node: Perplexity Agent API (pro-search)

**Node type:** HTTP Request  
**Method:** POST  
**URL:** `https://api.perplexity.ai/v1/agent`

**Headers:**
```json
{
  "Authorization": "Bearer {{ $env.PERPLEXITY_API_KEY }}",
  "Content-Type": "application/json"
}
```

**Body (JSON):**
```json
{
  "preset": "pro-search",
  "input": "Search today for developments in ALL of the following areas:\n1. VA policy changes affecting non-citizen veteran benefits\n2. DHS/ICE deportation of U.S. military veterans\n3. DCAS or Pentagon Vietnam casualty record updates\n4. NEH, Ford Foundation, MacArthur grant deadlines or announcements\n5. Congressional action on veteran citizenship legislation\nReturn only factual findings with source URLs. Omit topics with no new results."
}
```

**Response field to use downstream:** `output_text`

---

## WORKFLOW 1 — Daily Brief
### Node: Format Brief (Code node)

```javascript
const agentResult = $('Perplexity Agent API').first().json;
const signals = agentResult.output_text || 'No new signals today.';

const controlRoom = $('Read Notion Control Room').all();
const followUps = $('Read Submission Directory').all();
const grants = $('Read Grant Pipeline').all();

// Submissions overdue (sent > 14 days ago, no accession ID)
const today = new Date();
const overdueFollowUps = followUps
  .filter(r => {
    const sent = new Date(r.json.properties?.['Submission Date']?.date?.start);
    const hasAccession = r.json.properties?.['Accession ID']?.rich_text?.[0]?.text?.content;
    const daysSince = (today - sent) / (1000 * 60 * 60 * 24);
    return daysSince > 14 && !hasAccession;
  })
  .map(r => `- ${r.json.properties?.Name?.title?.[0]?.text?.content} (${Math.floor((today - new Date(r.json.properties?.['Submission Date']?.date?.start)) / (1000*60*60*24))} days)`)
  .join('\n') || 'None overdue.';

// Grants due in < 14 days
const urgentGrants = grants
  .filter(r => {
    const deadline = new Date(r.json.properties?.Deadline?.date?.start);
    const daysUntil = (deadline - today) / (1000 * 60 * 60 * 24);
    return daysUntil > 0 && daysUntil < 14;
  })
  .map(r => `- ${r.json.properties?.Funder?.title?.[0]?.text?.content}: ${r.json.properties?.Deadline?.date?.start}`)
  .join('\n') || 'None in the next 14 days.';

// Needs-me-today from Control Room
const needsMe = controlRoom
  .filter(r => r.json.properties?.Status?.select?.name === 'Needs You')
  .map(r => `- ${r.json.properties?.Thread?.title?.[0]?.text?.content}`)
  .join('\n') || 'Nothing flagged.';

const brief = `📋 AUMER DAILY BRIEF — ${today.toLocaleDateString('en-US', {weekday:'long', month:'long', day:'numeric'})}

🔴 NEEDS ME TODAY
${needsMe}

🟡 FOLLOW-UPS OVERDUE (14+ days, no accession)
${overdueFollowUps}

⏰ GRANT DEADLINES < 14 DAYS
${urgentGrants}

📡 NEW SIGNALS (Perplexity)
${signals}

✅ ONE THING
Check your top overdue follow-up. If 30 days have passed, send the escalation email.`;

return [{ json: { brief } }];
```

---

## WORKFLOW 2 — FOIA Watchdog
### Node: VA Policy Monitor (Sonar + domain filter)

**Node type:** HTTP Request  
**Method:** POST  
**URL:** `https://api.perplexity.ai/chat/completions`

**Headers:**
```json
{
  "Authorization": "Bearer {{ $env.PERPLEXITY_API_KEY }}",
  "Content-Type": "application/json"
}
```

**Body (JSON):**
```json
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "system",
      "content": "Only answer using the search results provided. If results do not contain new policy changes from the past 7 days, say so explicitly. State the source URL for each finding."
    },
    {
      "role": "user",
      "content": "What new guidance or policy changes has the VA issued about non-citizen veteran benefits, XC-files, or alien claims in the past 7 days?"
    }
  ],
  "search_domain_filter": ["va.gov", "benefits.va.gov", "publichealth.va.gov"],
  "search_recency_filter": "week"
}
```

**Response field:** `choices[0].message.content`  
**Citations field:** `citations[]`

---

### Node: DHS/ICE Monitor (Sonar + domain filter)

Same node type. Change body:

```json
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "system",
      "content": "Only answer using search results. State source URL for each finding. If nothing new, say so."
    },
    {
      "role": "user",
      "content": "What new ICE or DHS enforcement policies or guidance affect U.S. military veterans in removal proceedings in the past 7 days?"
    }
  ],
  "search_domain_filter": ["dhs.gov", "ice.gov", "uscis.gov", "eoir.justice.gov"],
  "search_recency_filter": "week"
}
```

---

## WORKFLOW 3 — Submission Concierge
### Node: Research Institution Before Drafting

**Node type:** HTTP Request  
**Method:** POST  
**URL:** `https://api.perplexity.ai/v1/agent`

**Body (JSON):**
```json
{
  "model": "anthropic/claude-sonnet-4-6",
  "input": "Look up current submission guidelines and contact information for {{ $json.institution_name }}'s special collections or archives program. Return: (1) current submission contact name and email, (2) submission format requirements, (3) whether they have a veterans, Chicano, or ethnic studies collection, (4) any current deadlines.",
  "tools": [{"type": "web_search"}],
  "instructions": "Search the institution's website first. Return only verified, current information. If contact info is not found, say so explicitly."
}
```

---

## ENVIRONMENT VARIABLES CHECKLIST

Set ALL of these in n8n before activating workflows:

| Variable | Where to get it | Used by |
|----------|-----------------|---------|
| `PERPLEXITY_API_KEY` | console.perplexity.ai | All Perplexity nodes |
| `NOTION_API_KEY` | notion.so/my-integrations | All Notion read nodes |
| `TELEGRAM_BOT_TOKEN` | Telegram → BotFather → /newbot | Daily Brief delivery |
| `TELEGRAM_CHAT_ID` | Message @userinfobot | Daily Brief delivery |
| `TWILIO_ACCOUNT_SID` | console.twilio.com | WhatsApp delivery (optional) |
| `TWILIO_AUTH_TOKEN` | console.twilio.com | WhatsApp delivery (optional) |

---

## COST ESTIMATES (Perplexity pay-as-you-go)

| Workflow | Frequency | Estimated cost |
|----------|-----------|----------------|
| Daily Brief (Agent API pro-search) | Daily | ~$0.01–0.05/run |
| FOIA Watchdog (Sonar Pro x2) | Weekly | ~$0.02–0.10/run |
| Submission Concierge (Agent API) | Per submission | ~$0.02–0.05/run |
| **Monthly total (est.)** | | **~$2–5/month** |

**Compare to:** OpenAI $20/mo subscription + Perplexity $20/mo subscription = $40/mo  
**With Agent API:** ~$5/mo actual usage. Cancel both subscriptions.
