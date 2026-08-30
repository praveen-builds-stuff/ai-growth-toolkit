const { Resend } = require('resend');
const resend = new Resend(process.env.RESEND_API_KEY);

function buildHtml(results) {
  const rows = results.map(r => {
    const issues = [
      ...r.brokenLinks.map(l => `Broken link: ${l.href} (${l.status})`),
      ...r.brokenCTAs.map(c => `CTA with no destination: "${c}"`),
      r.embeddedForm.present && !r.embeddedForm.fieldsVisible ? 'Form embed present but fields not rendering' : null,
      r.modalForm.present && !r.modalForm.fieldsVisible ? 'Modal form present but fields not rendering' : null,
    ].filter(Boolean);
    const status = issues.length ? '❌' : '✅';
    return `<tr><td>${status}</td><td>${r.url}</td><td>${issues.join('<br>') || '—'}</td></tr>`;
  }).join('');

  return `<table border="1" cellpadding="8">
    <tr><th>Status</th><th>Page</th><th>Issues</th></tr>
    ${rows}
  </table>`;
}

async function sendReport(results) {
  const passed = results.filter(r => !r.brokenLinks.length && !r.brokenCTAs.length).length;
  await resend.emails.send({
    from: process.env.FROM_EMAIL,
    to: process.env.TO_EMAIL,
    subject: `Canary Daily Report — ${new Date().toDateString()} — ${passed}/${results.length} pages passed`,
    html: buildHtml(results),
  });
}

module.exports = { sendReport };
