/*
Visual sanity checklist:
- headings readable
- body text readable
- links visible
- code blocks readable
- nav readable
- cards/feature_row readable
*/
(function () {
  var html = document.documentElement;
  var toggleBtn = document.getElementById('theme-toggle');

  function applyTheme(mode) {
    if (!html) return;
    html.setAttribute('data-theme', mode);
    if (toggleBtn) {
      toggleBtn.setAttribute('aria-pressed', mode === 'dark' ? 'true' : 'false');
      toggleBtn.setAttribute('title', mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
      toggleBtn.textContent = mode === 'dark' ? '🌞' : '🌓';
    }
  }

  var stored = null;
  try {
    stored = localStorage.getItem('theme');
  } catch (e) {
    stored = null;
  }
  var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  var initial = stored === 'dark' || stored === 'light' ? stored : (prefersDark ? 'dark' : 'light');

  applyTheme(initial);

  if (toggleBtn) {
    toggleBtn.addEventListener('click', function () {
      var current = html.getAttribute('data-theme') || 'light';
      var next = current === 'dark' ? 'light' : 'dark';
      try {
        localStorage.setItem('theme', next);
      } catch (e) {
        /* ignore storage errors */
      }
      applyTheme(next);
    });
  }
})();
