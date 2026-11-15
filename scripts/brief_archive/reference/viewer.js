
'use strict';
const $ = id => document.getElementById(id);
const models = Array.from($('left').options, option => option.value);
const requested = {};
let missingNotice = '';
const modelId = value => (value || '').split('/')[0];
function readSelection() {
  const p = new URLSearchParams(location.hash.slice(1));
  const missing = [];
  for (const side of ['left', 'right']) {
    const preferred = side === 'left' ? 'glm-5-3' : 'opus-5-5';
    const raw = p.get(side);
    // Accept both legacy full-path share links and stable model IDs.
    const match = models.find(value => value === raw || modelId(value) === modelId(raw));
    const fallback = models.find(value => modelId(value) === preferred) || models[side === 'left' ? 0 : 1] || models[0];
    $(side).value = match || fallback;
    requested[side] = raw ? modelId(raw) : modelId($(side).value);
    if (raw && !match) missing.push(requested[side]+' is unavailable on this day; showing '+modelId($(side).value)+' on the '+side+'.');
  }
  missingNotice = missing.join(' ');
  update(false);
}
function updateDayLinks() {
  const hash = '#'+new URLSearchParams(requested);
  document.querySelectorAll('nav a[data-day]').forEach(link => {
    link.href = link.dataset.day + hash;
  });
}
function update(save = true) {
  for (const side of ['left', 'right']) {
    const name = $(side).value;
    if (!models.includes(name)) return;
    if ($(side+'-frame').getAttribute('src') !== name) $(side+'-frame').src = name;
    $(side+'-frame').title = side+' model brief: '+modelId(name);
    $(side+'-original').href = name;
  }
  if (save) {
    for (const side of ['left','right']) requested[side] = modelId($(side).value);
    missingNotice = '';
    history.replaceState(null, '', '#'+new URLSearchParams(requested));
  }
  updateDayLinks();
  $('status').textContent = missingNotice || ($('left').value === $('right').value ? 'Both panes show the same model. Select another to compare.' : 'Each pane scrolls independently. Use Open original for a full-width report.');
}
for (const side of ['left','right']) $(side).addEventListener('change', () => update());
$('swap').addEventListener('click', () => {const old = $('left').value; $('left').value=$('right').value; $('right').value=old; update();});
$('wide').addEventListener('click', () => {const wide=document.body.classList.toggle('wide'); $('wide').setAttribute('aria-pressed',String(wide)); $('wide').textContent=wide?'Exit wide view':'Wide view';});
document.addEventListener('keydown', event => {if(event.key==='Escape' && document.body.classList.contains('wide')) $('wide').click();});
$('share').addEventListener('click', async () => {
  update();
  try {
    if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(location.href);
    else {
      const field=document.createElement('textarea');field.value=location.href;field.style.position='fixed';field.style.opacity='0';document.body.append(field);field.select();
      const copied=document.execCommand('copy');field.remove();$('share').focus();if(!copied) throw new Error('Copy unavailable');
    }
    $('status').textContent='Comparison link copied.';
  } catch (_) { $('status').textContent='Copy the address from your browser to share this comparison.'; }
});
window.addEventListener('hashchange', readSelection);
if(models.length){$('compare').hidden=false;readSelection();}
