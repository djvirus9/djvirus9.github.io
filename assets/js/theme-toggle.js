(function () {
  var root = document.documentElement;
  var button = document.getElementById('theme-toggle');
  var preference = window.matchMedia('(prefers-color-scheme: dark)');
  function label() {
    if (!button) return;
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    button.setAttribute('aria-label', 'Switch to ' + next + ' mode');
    button.setAttribute('title', 'Switch to ' + next + ' mode');
  }
  if (button) {
    button.hidden = false;
    label();
    button.addEventListener('click', function () {
      var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (error) { /* Storage is optional. */ }
      label();
    });
  }
  preference.addEventListener('change', function (event) {
    var saved;
    try { saved = localStorage.getItem('theme'); } catch (error) { /* Storage is optional. */ }
    if (saved !== 'light' && saved !== 'dark') {
      root.dataset.theme = event.matches ? 'dark' : 'light';
      label();
    }
  });
  var menu = document.getElementById('mobile-nav');
  if (!menu) return;
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && menu.open) {
      menu.open = false;
      menu.querySelector('summary').focus();
    }
  });
  document.addEventListener('click', function (event) {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
  menu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () { menu.open = false; });
  });
  window.matchMedia('(min-width: 56rem)').addEventListener('change', function (event) {
    if (event.matches) menu.open = false;
  });
})();
