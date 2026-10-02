/* Toggle Alert plugin dismissable field when Appearance is Admonition (TACC). */
(function () {
  function getAppearanceSelect() {
    return document.getElementById('id_alert_presentation');
  }

  function getDismissableInput() {
    return document.getElementById('id_alert_dismissable');
  }

  function syncDismissableForAppearance() {
    var appearance = getAppearanceSelect();
    var dismissable = getDismissableInput();
    if (!appearance || !dismissable) {
      return;
    }

    var isAdmonition = appearance.value === 'admonition';
    dismissable.disabled = isAdmonition;
    if (isAdmonition) {
      dismissable.checked = false;
    }

    var row =
      dismissable.closest('.form-row') ||
      dismissable.closest('.field-alert_dismissable');
    if (row) {
      row.classList.toggle('disabled', isAdmonition);
      row.setAttribute('aria-disabled', isAdmonition ? 'true' : 'false');
    }
  }

  function bind() {
    var appearance = getAppearanceSelect();
    if (!appearance || appearance.dataset.alertAppearanceBound) {
      return;
    }
    appearance.dataset.alertAppearanceBound = '1';
    appearance.addEventListener('change', syncDismissableForAppearance);
    syncDismissableForAppearance();
  }

  if (typeof django !== 'undefined' && django.jQuery) {
    django.jQuery(document).on('ready formset:added', function () {
      bind();
    });
    django.jQuery(bind);
  } else {
    document.addEventListener('DOMContentLoaded', bind);
  }

  /* Plugin editor may inject the form after DOMContentLoaded. */
  var observer = new MutationObserver(function () {
    bind();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });
})();
