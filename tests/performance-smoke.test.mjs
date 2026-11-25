import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync, statSync } from 'node:fs';
import { resolve } from 'node:path';
import vm from 'node:vm';

const root = process.cwd();
const html = readFileSync(resolve(root, 'index.html'), 'utf8');

test('HTML does not embed large base64 image payloads', () => {
  assert.doesNotMatch(html, /data:image\/[^;]+;base64,/i);
  assert.ok(Buffer.byteLength(html) < 200_000, 'index.html should stay below 200 KB');
});

test('all externalized local image assets exist', () => {
  const refs = [...html.matchAll(/\b(?:src|href|srcset)=["'](assets\/[^"']+)["']/g)].map(match => match[1]);
  assert.ok(refs.length >= 6, 'expected the six shared image assets to be referenced');
  for (const ref of new Set(refs)) {
    const path = resolve(root, ref);
    assert.ok(existsSync(path), 'Missing local asset: ' + ref);
    assert.ok(statSync(path).size > 0, 'Empty local asset: ' + ref);
  }
});

test('below-the-fold brand images use lazy loading and async decoding', () => {
  const ribbon = html.match(/<img\b(?=[^>]*class="[^"]*amash-brand-ribbon)[^>]*>/i)?.[0] ?? '';
  const footer = html.match(/<div class="footer-brand">([\s\S]*?)<\/div>/i)?.[1] ?? '';
  assert.match(ribbon, /loading="lazy"/);
  assert.match(ribbon, /decoding="async"/);
  assert.match(footer, /loading="lazy"/);
  assert.match(footer, /decoding="async"/);
});

test('core image workflow controls and processing functions remain', () => {
  for (const token of [
    'id="pick"', 'id="dl"', 'id="prev"', 'id="orig"', 'id="work"',
    'function base()', 'function fit(', 'async function squeeze(',
    'async function render(', 'function load(', 'function apply('
  ]) assert.ok(html.includes(token), 'Missing required workflow element: ' + token);
});

test('all executable inline JavaScript blocks parse', () => {
  const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(([, attrs]) => !/application\/ld\+json/i.test(attrs));
  assert.ok(scripts.length >= 3, 'expected application scripts');
  for (let i = 0; i < scripts.length; i++) {
    new vm.Script(scripts[i][2], { filename: 'index.html:inline-script-' + (i + 1) });
  }
});
