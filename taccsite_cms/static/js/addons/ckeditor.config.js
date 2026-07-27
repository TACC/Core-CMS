/* Register external plugins before CKEditor resolves extraPlugins */
/* https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_config.html#cfg-customConfig */

CKEDITOR.plugins.addExternal(
  'pastefromgdocs',
  'https://cdn.jsdelivr.net/gh/ckeditor/ckeditor4@4.21.0/plugins/pastefromgdocs/',
  'plugin.js'
);

CKEDITOR.on('instanceReady', function(ev) {
  var dtd = CKEDITOR.dtd;

  // To support what html5lib does not
  dtd.details = CKEDITOR.tools.extend({}, dtd.div, { summary: 1 });
  dtd.summary = CKEDITOR.tools.extend({}, dtd.div, { summary: 0 });
  dtd.$block['summary'] = 1;
  dtd.$intermediate['summary'] = 1;

  // To convert inline bold/italic styles to semantic tags on paste
  // FAQ: `pastefromgdocs` bold/italic are as inline styles,
  //      but the WYSIWYG strips inline styles from saved content
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
