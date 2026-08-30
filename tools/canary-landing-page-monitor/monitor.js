const { chromium } = require('playwright');
const { pages } = require('./config');

const STEALTH_USER_AGENT =
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36';

async function launchStealthBrowser() {
  const browser = await chromium.launch({
    headless: true,
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const context = await browser.newContext({
    userAgent: STEALTH_USER_AGENT,
    viewport: { width: 1280, height: 800 },
  });
  return { browser, context };
}

async function checkLinks(page) {
  const hrefs = await page.$$eval('a[href]', els => els.map(e => e.href));
  const results = [];
  for (const href of hrefs) {
    try {
      const res = await fetch(href, { method: 'HEAD' });
      if (res.status >= 400) results.push({ href, status: res.status });
    } catch {
      results.push({ href, status: 'ERROR' });
    }
  }
  return results;
}

async function checkCTAButtons(page) {
  const ctas = await page.$$('.btn, [class*="cta"], button');
  const broken = [];
  for (const cta of ctas) {
    const hasHref = await cta.evaluate(el => !!(el.href || el.onclick));
    if (!hasHref) broken.push(await cta.textContent());
  }
  return broken;
}

async function checkEmbeddedForm(page, selector = 'iframe[src*="form"]', timeoutMs = 8000) {
  const iframeEl = await page.$(selector);
  if (!iframeEl) return { present: false, fieldsVisible: false };
  const frame = await iframeEl.contentFrame();
  try {
    await frame.waitForSelector('input, textarea', { timeout: timeoutMs });
    return { present: true, fieldsVisible: true };
  } catch {
    return { present: true, fieldsVisible: false }; // script loaded, form didn't render — the real failure mode
  }
}

async function checkModalForm(page, triggerSelector = '[data-toggle="modal"]', timeoutMs = 5000) {
  const trigger = await page.$(triggerSelector);
  if (!trigger) return { present: false };
  await trigger.click();
  try {
    await page.waitForSelector('.modal input, .modal textarea', { timeout: timeoutMs });
    return { present: true, fieldsVisible: true };
  } catch {
    return { present: true, fieldsVisible: false };
  }
}

async function checkOnePage(context, url) {
  const page = await context.newPage();
  await page.goto(url, { waitUntil: 'networkidle' });
  const report = {
    url,
    brokenLinks: await checkLinks(page),
    brokenCTAs: await checkCTAButtons(page),
    embeddedForm: await checkEmbeddedForm(page),
    modalForm: await checkModalForm(page),
  };
  await page.close();
  return report;
}

async function run() {
  const { browser, context } = await launchStealthBrowser();
  const results = [];
  for (const url of pages) {
    results.push(await checkOnePage(context, url));
  }
  await browser.close();
  return results;
}

module.exports = { run };
if (require.main === module) run().then(r => console.log(JSON.stringify(r, null, 2)));
