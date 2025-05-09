# Core-CMS#868 Test Setup

## 1. Set Up Sites in Django Admin

Visit: http://localhost:8000/admin/sites/site/

Configure two sites:
- Site 1: domain = localhost:8000
- Site 2: domain = 127.0.0.1:8000

## 2. Configure Settings

1. (Optional) Verify you have a working Blog/News e.g.\
    `cp taccsite_cms/settings_custom.example.py taccsite_cms/settings_custom.py`

    > [!NOTE]
    > This is not required — you could test regular pages — but this allows you to test using Blog/News (the kind of remote content we build this feature for).

2. (Optional) Allow your local server to load two Sites at unique URLs i.e.\
    `cp taccsite_cms/custom_app_settings.example.py taccsite_cms/custom_app_settings.py`

    > [!NOTE]
    > This is not required — you could test an actual remote production server — but this allows fully local testing.

3. Add these settings to `local_settings.py`:

    ```python
    # Enable multisite for blog
    BLOG_MULTISITE = True

    # Configure remote content settings
    PORTAL_REMOTE_CONTENT_SOURCE_ROOT = 'http://localhost:8000/'
    PORTAL_REMOTE_CONTENT_CLIENT_PATH = '/remote/markup/'
    ```

    > [!NOTE]
    > If you are **not** testing multisite **or** Blog/News content, then set `PORTAL_REMOTE_CONTENT…` values appropriately.
    >
    > If you are **not** testing multisite **nor** Blog/News content, then no need to set `BLOG_MULTISITE` at all.

## 3. Create Test Articles

If you test Blog/News, [create two **articles**](http://localhost:8000/admin/djangocms_blog/post/):

1. Via Blog/News (either site):

  - Title: **Site 1 Article 1**
  - Sites: _select only_ **`localhost:8000`**

2. Via Blog/News (either site):

  - Title: **Site 2 Article 1**
  - Sites: _select only_ **`127.0.0.1:8000`**

If you do **not** test Blog/News, [create two **pages**](http://localhost:8000/admin/cms/page/):

1. Via localhost:8000:

    1. Create "Site 1 Page".
    2. Add text "Site 1 Page" to the page.

2. Via 127.0.0.1:8000:

    1. Create "Site 2 Page".
    2. Add text "Site 2 Page" to the page.

## 4. Test Setup

1. View articles or pages on their respective sites:

  - articles:
    1. http://localhost:8000/news/2025/05/09/site-1-article-1/
    2. http://127.0.0.1:8000/news/2025/05/09/site-2-article-1/

  - pages:
    1. http://localhost:8000/site-1-page/
    2. http://127.0.0.1:8000/site-2-page/

2. Test article or pages as remote content:

  - (article) Visit Site 2 and try to view Site 1's article:\
      http://127.0.0.1:8000/remote/markup?path=/news/2025/05/09/site-1-article-1/

  - (page) Visit Site 2 and try to view Site 1's page:\
      http://127.0.0.1:8000/remote/markup?path=/site-1-page/
