// The privacy policy lives inside index.html (#privacy), behind the Turnstile
// gate, generated from eas-launcher/privacy/policy.html. No new static files.
import fs from 'node:fs';
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
const html = fs.readFileSync('index.html', 'utf8');
const a = html.indexOf('<!-- EAS-PRIVACY:START'), b = html.indexOf('<!-- EAS-PRIVACY:END -->');
const section = a >= 0 && b > a ? html.slice(a, b) : '';
ok(section.includes('id="privacy"'), 'index.html has the #privacy section between markers');
ok(section.includes('Effective date: 24/11/2026'), 'effective date DD/MM/YYYY');
ok(section.includes('mailto:colt98045@gmail.com'), 'contact email');
for (const w of ['30 days', 'full IP address', 'Turnstile', 'Cloudflare Access', 'PIPEDA', 'GDPR', 'California', 'not legal advice']) ok(section.includes(w), `mentions ${w}`);
ok(!/<script/i.test(section), 'no scripts in the policy section');
ok(/href="#privacy"/.test(html.slice(html.indexOf('<footer class="site-footer">'))), 'footer links to #privacy');
ok(/\.eas-privacy:target\s*\{\s*display:block/.test(html), 'opens with CSS :target (no JS)');
const ignore = fs.readFileSync('.assetsignore', 'utf8');
ok(!/privacy/.test(ignore), '.assetsignore allowlist unchanged (no privacy file published)');
if (!process.exitCode) console.log('US privacy tests passed');
