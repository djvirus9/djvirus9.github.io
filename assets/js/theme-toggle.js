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

  // DEFAULT: light if no saved preference
  var saved = null;
  try { saved = localStorage.getItem('theme'); } catch (e) {}
  applyTheme(saved === 'dark' ? 'dark' : 'light');

  if (toggleBtn) {
    toggleBtn.addEventListener('click', function () {
      var current = html.getAttribute('data-theme') || 'light';
      var next = current === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('theme', next); } catch (e) {}
      applyTheme(next);
    });
  }
})();
