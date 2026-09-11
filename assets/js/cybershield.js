(function () {
  'use strict';
  function loadVideo(video) {
    if (video.dataset.loaded) return;
    if (video.dataset.poster) video.poster = video.dataset.poster;
    video.querySelectorAll('[data-src]').forEach(function (element) {
      element.src = element.dataset.src;
    });
    video.dataset.loaded = 'true';
    video.load();
    // This silent tour uses captions as narration. Enable them on first load;
    // visitors can still change the setting through the native player controls.
    var captions = video.querySelector('track[default]');
    if (captions) captions.track.mode = 'showing';
  }
  function playVideo(video) {
    var playback = video.play();
    if (playback && playback.catch) playback.catch(function () { /* Native controls remain available if playback is restricted. */ });
  }
  var standalone = document.querySelector('[data-standalone-tour]');
  if (standalone) {
    var standaloneVideo = standalone.querySelector('video');
    var start = standalone.querySelector('[data-start-tour]');
    start.addEventListener('click', function () {
      standaloneVideo.controls = true;
      loadVideo(standaloneVideo);
      start.hidden = true;
      standaloneVideo.focus();
      playVideo(standaloneVideo);
    });
    standalone.hidden = false;
  }
  var showcase = document.querySelector('[data-showcase]');
  if (!showcase) return;
  var list = showcase.querySelector('[data-stage-list]');
  var tabs = Array.from(showcase.querySelectorAll('[data-stage-tab]'));
  var panels = Array.from(showcase.querySelectorAll('[data-stage-panel]'));
  if (!list || tabs.length !== panels.length || !tabs.length) return;

  list.setAttribute('role', 'tablist');
  tabs.forEach(function (tab, index) {
    tab.setAttribute('role', 'tab');
    tab.setAttribute('aria-controls', panels[index].id);
    panels[index].setAttribute('role', 'tabpanel');
    panels[index].setAttribute('aria-labelledby', tab.id);
    panels[index].setAttribute('tabindex', '0');
  });

  function select(index, focus, updateUrl) {
    tabs.forEach(function (tab, position) {
      var selected = position === index;
      tab.setAttribute('aria-selected', String(selected));
      tab.setAttribute('tabindex', selected ? '0' : '-1');
      panels[position].hidden = !selected;
    });
    if (focus) tabs[index].focus();
    if (updateUrl) {
      try { history.replaceState(null, '', '#' + panels[index].id); } catch (error) { /* The explorer also works without URL updates. */ }
    }
  }

  function indexFromHash() {
    return panels.findIndex(function (panel) { return '#' + panel.id === location.hash; });
  }
  var initial = indexFromHash();
  select(initial < 0 ? 0 : initial, false, false);
  showcase.classList.add('cs-showcase--interactive');

  tabs.forEach(function (tab, index) {
    tab.addEventListener('click', function (event) {
      event.preventDefault();
      select(index, false, true);
    });
    tab.addEventListener('keydown', function (event) {
      var next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (event.key === ' ') next = index;
      if (next !== undefined) {
        event.preventDefault();
        select(next, true, true);
      }
    });
  });
  window.addEventListener('hashchange', function () {
    var index = indexFromHash();
    if (index >= 0) select(index, false, false);
  });

  var dialog = document.querySelector('[data-tour-dialog]');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  var video = dialog.querySelector('[data-tour-video]');
  var trigger;
  document.querySelectorAll('[data-open-tour]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      trigger = link;
      loadVideo(video);
      dialog.showModal();
      document.documentElement.classList.add('cs-tour-open');
      dialog.querySelector('.cs-tour-close').focus();
      playVideo(video);
    });
  });
  dialog.addEventListener('close', function () {
    video.pause();
    document.documentElement.classList.remove('cs-tour-open');
    if (trigger) trigger.focus();
  });
  dialog.addEventListener('click', function (event) {
    if (event.target !== dialog) return;
    var bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
})();
