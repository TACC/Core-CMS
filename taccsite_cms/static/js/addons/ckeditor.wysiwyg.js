/* Alter ckeditor/styles.js to match our own wants */
/* https://github.com/django-cms/djangocms-text-ckeditor/blob/3.10.0/djangocms_text_ckeditor/static/djangocms_text_ckeditor/ckeditor/styles.js */

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
  }, null, null, 1);
});

CKEDITOR.stylesSet.add( 'default', [

	/* Block styles */

	{
		name: 'Island',
		element: 'aside',
		attributes: { 'class': 'island' }
	},

	/* Inline styles */

	{ name: 'Mark (Highlight)',			element: 'mark' },

	{ name: 'Big',				element: 'big' },
	{ name: 'Small',			element: 'small' },
	{ name: 'Typewriter',		element: 'tt' },

	{ name: 'Computer Code',	element: 'code' },
	{ name: 'Keyboard Phrase',	element: 'kbd' },
	{ name: 'Sample Text',		element: 'samp' },
	{ name: 'Variable',			element: 'var' },

	{ name: 'Deleted Text',		element: 'del' },
	{ name: 'Inserted Text',	element: 'ins' },

	{ name: 'Cited Work',		element: 'cite' },
	{ name: 'Inline Quotation',	element: 'q' },

	{ name: 'Time/Date', element: 'time' },

	{ name: 'Language: RTL',	element: 'span', attributes: { 'dir': 'rtl' } },
	{ name: 'Language: LTR',	element: 'span', attributes: { 'dir': 'ltr' } },

] );
