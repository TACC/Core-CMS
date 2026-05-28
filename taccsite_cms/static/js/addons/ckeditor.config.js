/* Register external plugins before CKEditor resolves extraPlugins */
/* https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_config.html#cfg-customConfig */

CKEDITOR.plugins.addExternal(
  'pastefromgdocs',
  'https://cdn.jsdelivr.net/gh/ckeditor/ckeditor4@4.21.0/plugins/pastefromgdocs/',
  'plugin.js'
);
