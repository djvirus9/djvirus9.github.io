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
  var lightLink = document.getElementById('theme-light');
  var darkLink = document.getElementById('theme-dark');
  var toggleBtn = document.getElementById('theme-toggle');

  function applyTheme(mode) {
    if (!lightLink || !darkLink) return;
    if (mode === 'dark') {
      darkLink.disabled = false;
      lightLink.disabled = true;
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      darkLink.disabled = true;
      lightLink.disabled = false;
      document.documentElement.setAttribute('data-theme', 'light');
    }
    if (toggleBtn) {
      toggleBtn.setAttribute('aria-pressed', mode === 'dark' ? 'true' : 'false');
      toggleBtn.setAttribute('title', mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
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
      var next = darkLink && !darkLink.disabled ? 'light' : 'dark';
      try {
        localStorage.setItem('theme', next);
      } catch (e) {
        /* ignore storage errors */
      }
      applyTheme(next);
    });
  }
})();
