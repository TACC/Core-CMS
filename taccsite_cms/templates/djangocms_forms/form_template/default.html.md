# TACC CMS - Templates - Default Form

The [original template] could have been cloned and edited.

But, to avoid that[^1], the two changes have been performed other ways:

1. [Remove redundant load of `google.com/recaptcha/api.js`.][1]
2. [Add `c-button` class styles to form submit button via CSS not markup.][2]

[^1]: Avoid editing the template because it does not use `block`s (which means we need to clone the whole template; which means if the [original template] changes, and we update form plugin, ours will become out of date).

[original template]: https://github.com/avryhof/djangocms-forms/blob/ab38b22/djangocms_forms/templates/djangocms_forms/form_template/default.html
[1]: https://github.com/avryhof/djangocms-forms/pull/12
[2]: ../../../static/site_cms/css/src/_imports/components/django.cms.forms.css#L103
