"""Configure search plugins"""

PORTAL_ES_ENABLED = False

########################
# ELASTICSEARCH
########################

if PORTAL_ES_ENABLED:
    ES_AUTH = 'username:password'
    ES_HOSTS = 'http://elasticsearch:9200'
    ES_INDEX_PREFIX = 'cms-dev-{}'
    ES_DOMAIN = 'http://localhost:8000'

    # Elasticsearch Indexing
    HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter', ]
    HAYSTACK_SIGNAL_PROCESSOR = 'taccsite_cms.signal_processor.RealtimeSignalProcessor'
    ALDRYN_SEARCH_DEFAULT_LANGUAGE = 'en'
    ALDRYN_SEARCH_REGISTER_APPHOOK = True
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': ES_HOSTS,
            'INDEX_NAME': ES_INDEX_PREFIX.format('cms'),
            'KWARGS': {'http_auth': ES_AUTH}
        }
    }

########################
# DJANGO CMS
########################

if PORTAL_ES_ENABLED:
    _INSTALLED_APPS = [
        'haystack',                # search index
        'aldryn_apphooks_config',  # search index & django CMS Blog
    ]
else:
    _INSTALLED_APPS = []

########################
# TACC: SEARCH
########################

SEARCH_PATH = '/search'

if PORTAL_ES_ENABLED:
    # Elasticsearch
    SEARCH_QUERY_PARAM_NAME = 'query_string'
else:
    # Google
    SEARCH_QUERY_PARAM_NAME = 'q'
