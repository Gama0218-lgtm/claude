# OpenAI agent for Google Sheets

This repository contains a small Google Apps Script integration that adds an
`OPENAI_AGENT` function to Google Sheets. It is intended for people who call a
Google Sheet an “Excel on Google” and need a safe place to configure their own
OpenAI API key.

> [!IMPORTANT]
> This project does **not** contain or grant access to an OpenAI key. Create a
> key in the [OpenAI API key dashboard](https://platform.openai.com/api-keys).
> API billing is separate from a ChatGPT subscription. Never paste a key into a
> spreadsheet cell, source file, commit, chat, or screenshot.

## Install in a Google Sheet

1. Open the target Google Sheet and select **Extensions → Apps Script**.
2. Replace the editor contents with [`Code.gs`](Code.gs).
3. In **Project Settings**, enable **Show `appsscript.json` manifest file in
   editor**, then replace that file with [`appsscript.json`](appsscript.json).
4. Save the project and reload the spreadsheet.
5. Select **OpenAI → Set API key**, paste a key beginning with `sk-`, and
   approve the Google authorization prompt. The script stores it in Apps
   Script **User Properties**, not in the workbook.
6. Optionally select **OpenAI → Set model**. If no model is configured, the
   sample uses `gpt-4.1-mini`.
7. Enter a formula such as:

   ```text
   =OPENAI_AGENT("Summarize this cell in one sentence", A2)
   ```

The second parameter is optional. A two-dimensional cell range is serialized
as tab-separated rows so that its table structure remains visible to the
model.

## AutoSheet is a separate credential

The [AutoSheet API documentation](https://autosheet.com/docs/api#description/get-started)
describes AutoSheet's service. An AutoSheet API token and an OpenAI API key are
different credentials and are not interchangeable:

- If AutoSheet asks for an **OpenAI API key**, create your own key in the
  OpenAI dashboard and enter it only in AutoSheet's protected settings UI.
- If its endpoint asks for an **AutoSheet API key/token**, obtain that from
  your AutoSheet account or workspace.
- Do not send either secret as a worksheet formula argument. Formula values,
  revision history, and shared-sheet access can expose it.

The script in this repository calls OpenAI directly, so an AutoSheet account
is not required.

## Usage

```text
=OPENAI_AGENT("Classify the sentiment as positive, neutral, or negative", B2)
=OPENAI_AGENT("Extract three action items", A2:A20)
=OPENAI_AGENT("Rewrite this title for clarity")
```

Custom functions may execute more than once when a sheet recalculates. Avoid
copying the formula across a large range until you understand API usage and
costs. For sensitive or regulated data, confirm that sending the data to an
external API complies with your organization's policies.

## Configuration and security

The spreadsheet menu stores these per-user script properties:

| Property | Purpose |
| --- | --- |
| `OPENAI_API_KEY` | Secret OpenAI API key |
| `OPENAI_MODEL` | Optional model override |

To revoke local access, select **OpenAI → Remove API key**. If a key was ever
placed in a cell, source code, Git history, or a public message, delete it from
the OpenAI dashboard immediately and issue a new one; merely removing the text
does not make the old key safe.

The Apps Script manifest allowlists only the OpenAI API origin and requests the
minimum scopes needed for external requests, per-user properties, and the
spreadsheet menu.

## Troubleshooting

- **“OpenAI API key is not configured”** — reload the sheet and use **OpenAI →
  Set API key** while signed in as the user who will run the formula.
- **401 / invalid API key** — remove the stored value, create a new OpenAI key,
  and save it again without quotes or surrounding spaces.
- **429** — the account has hit a rate, usage, or billing limit. Check the
  OpenAI platform usage and billing pages, then retry later.
- **Model not found / access denied** — use **OpenAI → Set model** and enter a
  model available to the API project associated with the key.
- **Permission error** — run a menu command once to trigger Apps Script's
  authorization flow. Workspace administrators can restrict external calls.
- **AutoSheet authentication error** — verify that the credential belongs to
  the service named by the error; an OpenAI key cannot replace an AutoSheet
  token.

## Development check

`Code.gs` is plain JavaScript compatible with the Apps Script V8 runtime. A
lightweight syntax check can be run locally:

```bash
cp Code.gs /tmp/Code.js && node --check /tmp/Code.js
```
