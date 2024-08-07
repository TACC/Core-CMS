"""Configure deprecated search solution"""

########################
# SEARCH
########################

ES_AUTH = 'username:password'
ES_HOSTS = 'http://elasticsearch:9200'
ES_INDEX_PREFIX = 'cms-dev-{}'
ES_DOMAIN = 'http://localhost:8000'

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

_INSTALLED_APPS = [
    'haystack',                # search index
]
