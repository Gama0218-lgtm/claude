/** @OnlyCurrentDoc */

const OPENAI_API_URL = 'https://api.openai.com/v1/responses';
const DEFAULT_OPENAI_MODEL = 'gpt-4.1-mini';
const API_KEY_PROPERTY = 'OPENAI_API_KEY';
const MODEL_PROPERTY = 'OPENAI_MODEL';

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('OpenAI')
    .addItem('Set API key', 'setOpenAiApiKey')
    .addItem('Set model', 'setOpenAiModel')
    .addSeparator()
    .addItem('Remove API key', 'removeOpenAiApiKey')
    .addToUi();
}

function setOpenAiApiKey() {
  const ui = SpreadsheetApp.getUi();
  const response = ui.prompt(
    'Set OpenAI API key',
    'Paste your OpenAI API key. It will be stored in your Apps Script User Properties, not in a cell.',
    ui.ButtonSet.OK_CANCEL
  );

  if (response.getSelectedButton() !== ui.Button.OK) return;

  const apiKey = response.getResponseText().trim();
  if (!apiKey.startsWith('sk-')) {
    ui.alert('That does not look like an OpenAI API key. No value was saved.');
    return;
  }

  PropertiesService.getUserProperties().setProperty(API_KEY_PROPERTY, apiKey);
  ui.alert('OpenAI API key saved for your Google account.');
}

function setOpenAiModel() {
  const ui = SpreadsheetApp.getUi();
  const currentModel = getUserProperties_().getProperty(MODEL_PROPERTY) || DEFAULT_OPENAI_MODEL;
  const response = ui.prompt(
    'Set OpenAI model',
    `Enter a model available to your OpenAI API project (current: ${currentModel}).`,
    ui.ButtonSet.OK_CANCEL
  );

  if (response.getSelectedButton() !== ui.Button.OK) return;

  const model = response.getResponseText().trim();
  if (!model || !/^[A-Za-z0-9._:-]+$/.test(model)) {
    ui.alert('Enter a valid model name. No value was saved.');
    return;
  }

  getUserProperties_().setProperty(MODEL_PROPERTY, model);
  ui.alert(`OpenAI model saved as ${model}.`);
}

function removeOpenAiApiKey() {
  getUserProperties_().deleteProperty(API_KEY_PROPERTY);
  SpreadsheetApp.getUi().alert('The OpenAI API key was removed from your User Properties.');
}

/**
 * Sends an instruction and optional cell/range context to OpenAI.
 *
 * @param {string} instruction The task for the model.
 * @param {*=} context Optional cell or range containing source material.
 * @return {string} The model's text response.
 * @customfunction
 */
function OPENAI_AGENT(instruction, context) {
  const prompt = String(instruction || '').trim();
  if (!prompt) throw new Error('Provide an instruction as the first argument.');

  const properties = getUserProperties_();
  const apiKey = properties.getProperty(API_KEY_PROPERTY);
  if (!apiKey) {
    throw new Error('OpenAI API key is not configured. Reload the sheet, then use OpenAI → Set API key.');
  }

  const contextText = serializeContext_(context);
  const input = contextText ? `${prompt}\n\nSpreadsheet context:\n${contextText}` : prompt;
  const response = UrlFetchApp.fetch(OPENAI_API_URL, {
    method: 'post',
    contentType: 'application/json',
    headers: { Authorization: `Bearer ${apiKey}` },
    payload: JSON.stringify({
      model: properties.getProperty(MODEL_PROPERTY) || DEFAULT_OPENAI_MODEL,
      input: input
    }),
    muteHttpExceptions: true
  });

  const status = response.getResponseCode();
  const body = response.getContentText();
  let data;
  try {
    data = JSON.parse(body);
  } catch (error) {
    throw new Error(`OpenAI returned HTTP ${status} with an unreadable response.`);
  }

  if (status < 200 || status >= 300) {
    const message = data && data.error && data.error.message ? data.error.message : 'Request failed.';
    throw new Error(`OpenAI returned HTTP ${status}: ${message}`);
  }

  const output = extractOutputText_(data);
  if (!output) throw new Error('OpenAI returned no text output.');
  return output;
}

function getUserProperties_() {
  return PropertiesService.getUserProperties();
}

function serializeContext_(context) {
  if (context === undefined || context === null || context === '') return '';
  if (!Array.isArray(context)) return String(context);

  return context
    .map(row => (Array.isArray(row) ? row : [row]).map(value => String(value ?? '')).join('\t'))
    .join('\n');
}

function extractOutputText_(data) {
  if (typeof data.output_text === 'string' && data.output_text.trim()) {
    return data.output_text.trim();
  }

  const textParts = [];
  (data.output || []).forEach(item => {
    (item.content || []).forEach(content => {
      if (content.type === 'output_text' && typeof content.text === 'string') {
        textParts.push(content.text);
      }
    });
  });
  return textParts.join('\n').trim();
}
