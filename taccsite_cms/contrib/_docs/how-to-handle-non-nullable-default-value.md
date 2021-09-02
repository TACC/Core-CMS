# How to Handle "Non-Nullable" "Default Value"

## Sample Error

```text
You are trying to add a non-nullable field '...'
to choice without a default; we can't do that
(the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option:
```

## Explanations

- (blog post) [What do you do when 'makemigrations' is telling you About your Lack of Default Value](https://chrisbartos.com/articles/what-do-you-do-when-makemigrations-is-telling-you-about-your-lack-of-default-value/)
- (video) [You are trying to add a non-nullable field ' ' to ' ' without a default; we can't do that](https://www.youtube.com/watch?v=NgaTUEijQSQ)

## Solutions

### For `cmsplugin_ptr`

1. ☑ Select option 1), then see:
    - [Follow-Up Error](#follow-up-error)
    - [Notes ▸ `cmsplugin_ptr`](#cmsplugin_ptr)

### For Other Fields

1. ⚠ Select option 1) and hope for the best.
2. ☑ Select option 2) and provide a sensible default (_not_ `None` a.k.a. null).
3. ⚠ (blog post) (hack) [Add A Migration For A Non-Null Foreignkey Field In Django](https://jaketrent.com/post/add-migration-nonnull-foreignkey-field-django)

## Follow-Up Error

If you allowed Null to be set as default, then you may have this new error:

```text
django.db.utils.IntegrityError: column "..." contains null values
```

Solutions:

1. [delete _relevant_ migration files and rebuild migrations](https://stackoverflow.com/a/37244199/11817077)
2. [delete _all_ migration files and rebuild migrations](https://stackoverflow.com/a/37242930/11817077)

## Notes

### `cmsplugin_ptr`

  If the field is `cmsplugin_ptr` then know that

  - [it is a database relationship field managed automatically by Django](https://github.com/nephila/djangocms-blog/issues/316#issuecomment-242292787),
  - you may see it in workarounds for other plugins ([source a](https://github.com/django-cms/djangocms-link/blob/3.0.0/djangocms_link/models.py#L125), [source b](https://github.com/django-cms/djangocms-picture/blob/3.0.0/djangocms_picture/models.py#L208)),
  - you should __not__ add or overwrite it unless you know what you are doing.

  _W. Bomar learned everything in the intitial version of this document after trying to overwrite `cmsplugin_ptr` while extending its model from [source a](https://github.com/django-cms/djangocms-link/blob/3.0.0/djangocms_link/models.py#L125). His solution was [delete _all_ migration files and rebuild migrations](https://stackoverflow.com/a/37242930/11817077)._

## Appendix

- [Django CMS ▸ How to create Plugins ▸ Handling Relations](https://docs.django-cms.org/en/release-3.7.x/how_to/custom_plugins.html#handling-relations)
- [[BUG] Plugins with models that don't directly inherit from CMSPlugin or an abstract model cannot be copied](https://github.com/django-cms/django-cms/issues/6987)
