(function () {
  'use strict';
  var root = document.querySelector('[data-secops-demo]');
  if (!root) return;
  var original;
  try { original = JSON.parse(root.querySelector('[data-demo-findings]').textContent); } catch (error) { return; }
  if (!Array.isArray(original) || !original.length) return;
  var findings;
  var selected;
  var list = root.querySelector('[data-findings-list]');
  var detail = root.querySelector('[data-finding-detail]');
  var form = root.querySelector('[data-triage-form]');
  var feedback = root.querySelector('[data-demo-feedback]');
  var filters = {};
  root.querySelectorAll('[data-filter]').forEach(function (control) { filters[control.dataset.filter] = control; });
  function label(value) { return value.charAt(0).toUpperCase() + value.slice(1); }
  function current() { return findings.find(function (finding) { return finding.id === selected; }); }
  function matches(finding) {
    var query = filters.search.value.trim().toLowerCase();
    var text = [finding.title, finding.asset, finding.tool, finding.project, finding.id].join(' ').toLowerCase();
    return (!query || text.includes(query)) &&
      (filters.severity.value === 'all' || finding.severity === filters.severity.value) &&
      (filters.status.value === 'all' || finding.status === filters.status.value);
  }
  function renderDetail() {
    var finding = current();
    detail.hidden = !finding;
    if (!finding) return;
    root.querySelectorAll('[data-detail]').forEach(function (element) {
      var key = element.dataset.detail;
      element.textContent = key === 'severity' ? label(finding[key]) : finding[key];
      if (key === 'severity') element.dataset.severity = finding.severity;
    });
    form.elements.status.value = finding.status;
    form.elements.assignee.value = finding.assignee;
  }
  function selectFinding(id) {
    selected = id;
    list.querySelectorAll('button').forEach(function (button) {
      button.setAttribute('aria-pressed', String(button.dataset.findingId === id));
    });
    renderDetail();
    var heading = root.querySelector('[data-detail="title"]');
    heading.focus({preventScroll: true});
    if (window.matchMedia('(max-width: 42rem)').matches) heading.scrollIntoView({block: 'start'});
    feedback.textContent = 'Viewing ' + current().id + '. Review the evidence, then choose a status and owner.';
  }
  function render() {
    var visible = findings.filter(matches);
    if (!visible.some(function (finding) { return finding.id === selected; })) selected = visible.length ? visible[0].id : null;
    list.replaceChildren();
    visible.forEach(function (finding) {
      var item = document.createElement('li');
      var button = document.createElement('button');
      button.type = 'button';
      button.dataset.findingId = finding.id;
      button.setAttribute('aria-pressed', String(finding.id === selected));
      button.setAttribute('aria-controls', 'sample-finding-title');
      var severity = document.createElement('span');
      severity.className = 'sd-severity';
      severity.dataset.severity = finding.severity;
      severity.textContent = label(finding.severity);
      var status = document.createElement('span');
      status.className = 'sd-row-status';
      status.textContent = label(finding.status);
      var meta = document.createElement('span');
      meta.className = 'sd-row-meta';
      meta.append(severity, status);
      var title = document.createElement('strong');
      title.textContent = finding.title;
      var source = document.createElement('span');
      source.className = 'sd-row-source';
      source.textContent = finding.tool + ' · ' + finding.project;
      button.append(meta, title, source);
      button.addEventListener('click', function () { selectFinding(finding.id); });
      item.append(button);
      list.append(item);
    });
    root.querySelector('[data-empty]').hidden = visible.length !== 0;
    root.querySelector('[data-result-count]').textContent = visible.length + ' of ' + findings.length + ' sample findings';
    root.querySelector('[data-count="total"]').textContent = findings.length;
    ['open', 'investigating', 'resolved'].forEach(function (status) {
      root.querySelector('[data-count="' + status + '"]').textContent = findings.filter(function (finding) {
        return finding.status === status || (status === 'resolved' && finding.status === 'closed');
      }).length;
    });
    renderDetail();
  }
  function reset() {
    findings = original.map(function (finding) { return Object.assign({}, finding); });
    selected = findings[0].id;
    filters.search.value = '';
    filters.severity.value = filters.status.value = 'all';
    render();
  }
  Object.keys(filters).forEach(function (key) {
    filters[key].addEventListener(key === 'search' ? 'input' : 'change', function () {
      render();
      feedback.textContent = 'Filters applied. Select a finding to inspect its evidence.';
    });
  });
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    var finding = current();
    if (!finding) return;
    var status = form.elements.status.value;
    var assignee = form.elements.assignee.value;
    if (!['open', 'investigating', 'resolved', 'closed'].includes(status) || !['Unassigned', 'Application team', 'Platform team'].includes(assignee)) return;
    finding.status = status;
    finding.assignee = assignee;
    var message = finding.id + ' updated to ' + label(status) + ' · ' + assignee + '. Sample changes last until reset or reload.';
    render();
    feedback.textContent = message;
    if (detail.hidden) root.querySelector('[data-reset-demo]').focus();
  });
  root.querySelector('[data-reset-demo]').addEventListener('click', function () {
    reset();
    feedback.textContent = 'Demo reset. All five original sample findings are restored.';
  });
  reset();
  root.querySelector('[data-demo-fallback]').hidden = true;
  root.querySelector('[data-demo-app]').hidden = false;
})();
