(function () {
  var root = document.documentElement;
  var saved;
  try { saved = localStorage.getItem('theme'); } catch (error) { /* Storage is optional. */ }
  var preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  root.dataset.theme = saved === 'light' || saved === 'dark' ? saved : preferred;
  root.classList.replace('no-js', 'js');
})();
