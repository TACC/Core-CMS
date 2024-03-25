/* Alter ckeditor/styles.js to match our own wants */
/* https://github.com/django-cms/djangocms-text-ckeditor/blob/3.10.0/djangocms_text_ckeditor/static/djangocms_text_ckeditor/ckeditor/styles.js */

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
