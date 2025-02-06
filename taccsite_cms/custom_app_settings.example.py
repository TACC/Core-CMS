CUSTOM_APPS = [

    # CUSTOM APP
    'apps.custom_example',

    # DJANGOCMS_BLOG
    'parler',
    'taggit',
    'taggit_autosuggest',
    'sortedm2m',
    'djangocms_blog',

]
CUSTOM_MIDDLEWARE = ['taccsite_cms.middleware.cms_template.CMSTemplateOverrideMiddleware']
STATICFILES_DIRS = ()
