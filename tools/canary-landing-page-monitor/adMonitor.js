const { pages } = require('./config');

async function checkPage(url) {
  try {
    const res = await fetch(url, { method: 'GET', redirect: 'follow' });
    return { url, status: res.status, ok: res.status === 200 };
  } catch (err) {
    return { url, status: 'ERROR', ok: false, error: err.message };
  }
}

async function run() {
  const results = await Promise.all(pages.map(checkPage));
  const failures = results.filter(r => !r.ok);
  console.log(`Checked ${results.length} pages, ${failures.length} failed`);
  return results;
}

module.exports = { run };
if (require.main === module) run();
