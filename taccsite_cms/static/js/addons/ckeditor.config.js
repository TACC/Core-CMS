/* Register external plugins before CKEditor resolves extraPlugins */
/* https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_config.html#cfg-customConfig */

CKEDITOR.plugins.addExternal(
  'pastefromgdocs',
  'https://cdn.jsdelivr.net/gh/ckeditor/ckeditor4@4.21.0/plugins/pastefromgdocs/',
  'plugin.js'
);

/* Convert inline bold/italic styles to semantic tags on paste,
   because the site strips inline styles from saved content,
   yet `pastefromgdocs` bold/italic are as inline styles. */
CKEDITOR.on('instanceReady', function(ev) {
  ev.editor.on('paste', function(e) {
    var parser = new DOMParser();
    var doc = parser.parseFromString(e.data.dataValue, 'text/html');

    doc.querySelectorAll('span').forEach(function(span) {
      var fw = span.style.fontWeight;
      var fs = span.style.fontStyle;
      var replacement;

      if (fw === 'bold' || fw === '700') {
        replacement = doc.createElement('strong');
      } else if (fs === 'italic') {
        replacement = doc.createElement('em');
      }

      if (replacement) {
        while (span.firstChild) replacement.appendChild(span.firstChild);
        span.parentNode.replaceChild(replacement, span);
      }
    });

    e.data.dataValue = doc.body.innerHTML;
  /* Priority 4 runs after `pastetools` (priority 3); we must run after it
     because it re-reads original clipboard data and overwrites dataValue. */
  }, null, null, 4);
});
