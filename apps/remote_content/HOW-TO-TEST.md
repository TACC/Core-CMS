# Core-CMS#868 Test Setup

## 1. Set Up Sites in Django Admin

Visit: http://localhost:8000/admin/sites/site/

Configure two sites:
- Site 1: domain = localhost:8000
- Site 2: domain = 127.0.0.1:8000

## 2. Configure Local Settings

````python
# filepath: settings_local.py

# Enable multisite for blog
BLOG_MULTISITE = True

# Configure remote content settings
PORTAL_REMOTE_CONTENT_SOURCE_ROOT = 'http://localhost:8000/news/'
PORTAL_REMOTE_CONTENT_CLIENT_PATH = '/remote/markup/'

## 3. Create Test Articles

Visit: http://localhost:8000/admin/djangocms_blog/post/

1. Create two articles:

    1. "Site 1 Article":
    - Title: Site 1 Article 1
    - Publish date: 2025-05-09
    - Sites: Select only "localhost:8000"
    2. "Site 2 Article":
    - Title: Site 2 Article 1
    - Publish date: 2025-05-09
    - Sites: Select only "127.0.0.1:8000"

## 4. Test Setup

1. View articles on their respective sites:
    - http://localhost:8000/news/2025/05/09/site-1-article-1/
    - http://127.0.0.1:8000/news/2025/05/09/site-2-article-1/
2. Test remote content:
    - Visit Site 2 and try to view Site 1's article:\
      http://127.0.0.1:8000/remote/markup/2025/05/09/site-1-article-1/
