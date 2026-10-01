# AUMER Foundation — Full Integration Map

Every tool, how it connects, what it does, and what's needed to activate it.

---

## THE STACK

| Tool | Role | Connect via | Status | Action needed |
|------|------|-------------|--------|---------------|
| **Claude** | Brain / Chief of Staff | Direct (MCP) | ✅ Active | None |
| **Notion** | Command Center | MCP live | ✅ Active | None |
| **HubSpot** | Contact book (2,152 contacts) | MCP live | ✅ Active | Load 12 institutions |
| **GitHub** | Code vault / archive | MCP live | ✅ Active | None |
| **n8n** | Nervous system / automation hub | Cloud (just activated) | ✅ Active | Build 3 workflows |
| **Perplexity** | Researcher / citations | n8n → Sonar API | 🔑 Need API key | Get key from perplexity.ai/settings |
| **Gemini / Google Cloud** | Back office / Workspace | n8n → Google Cloud API | 🔑 Need API key | Get from console.cloud.google.com |
| **OpenAI** | Secondary reasoning / image gen | n8n → OpenAI API | 🔑 Need API key | Get from platform.openai.com |
| **Base44** | App builder / Superagents | n8n → Webhook | 🔗 Need webhook | Get from Base44 → Agent → Integrations |
| **Telegram** | Alert channel | n8n → Telegram Bot API | 🔑 Need bot token | BotFather on Telegram |
| **WhatsApp** | Alert channel | n8n → Twilio or WhatsApp Business API | 🔑 Need token | Twilio or Meta Business |
| **GoDaddy** | Domains + email | Manual (no API needed) | ⏳ Pending | Activate q2vengeance.org |
| **GA4** | Analytics | Manual embed | ⏳ Pending | Add Measurement ID to sites |

---

## THE 3 PRIORITY n8n WORKFLOWS

See `n8n-workflows.md` for full specs.

### Workflow 1 — Daily Brief (BUILD FIRST)
Reads Notion → calls Perplexity Sonar → formats → sends to Telegram + WhatsApp every morning at 7:30am Pacific.

### Workflow 2 — Submission Follow-up Monitor  
Checks Submission Directory every day at 9am for any institution where Stage = Sent and Date sent > 14 days ago. Sends Telegram alert with institution name and drafted follow-up note.

### Workflow 3 — Research Pipeline
Trigger: manual or scheduled. Calls Perplexity Sonar with a research query. Returns cited results to a new Notion page under a Research folder. Tags with source, date, confidence level.

---

## HOW THE TOOLS TALK TO EACH OTHER

```
Perplexity Sonar API ─────────────────────────────┐
Gemini / Google Cloud API ────────────────────────┤
OpenAI API ───────────────────────────────────────┤
Base44 Superagent webhooks ───────────────────────┼──► n8n (hub)
HubSpot API ──────────────────────────────────────┤         │
GitHub API ───────────────────────────────────────┘         │
                                                             ▼
                                              Notion (Command Center)
                                                             │
                                              ┌──────────────┤
                                              ▼              ▼
                                          Telegram       WhatsApp
                                        (alerts)        (alerts)
                                              │
                                              ▼
                                    Gabriel reviews + decides
```

---

## NOTION API CONNECTION SPEC (for Antigravity / Base44)

### Databases to wire into TruthEngine360:

| Database | URL | TruthEngine360 tab |
|----------|-----|--------------------|
| Submission Directory | https://www.notion.so/f8024ec76cab4541a2394db977a8d3c3 | Stakeholder Directory |
| Grant Pipeline | https://www.notion.so/0643034762764656b6960433b4e01f7f | Grants tab |
| Case File Registry | https://www.notion.so/6a1584093a4449be93d49084e82cb28c | Veterans / FOIA tab |
| Control Room | https://www.notion.so/12a40dc48e854bbb839838b69bf4fb5b | Dashboard / Control Room |

### Required Notion API scopes:
- `databases:read` — all four
- `databases:write` — Submission Directory, Case File Registry
- `pages:read` — all
- `pages:write` — Submission Directory (status updates)

### Steps:
1. Go to notion.so/my-integrations → Create new integration
2. Name: "TruthEngine360"
3. Grant access to the AUMER Command Center workspace
4. Copy the Internal Integration Token
5. In each database: Share → Invite → TruthEngine360 integration
6. Pass the token to Antigravity as `NOTION_API_KEY` env variable
