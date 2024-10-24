"""Configure search solution"""

########################
# SEARCH
########################

# To support any search
PORTAL_SEARCH_PATH = '/search'

# To support Google search
# PORTAL_SEARCH_QUERY_PARAM_NAME = 'q'
# PORTAL_SEARCH_INDEX_IS_AUTOMATIC = False
GOOGLE_SEARCH_ENGINE_ID = ''

# (DEPRECATED) To support Elasticsearch
PORTAL_SEARCH_QUERY_PARAM_NAME = 'query_string'
PORTAL_SEARCH_INDEX_IS_AUTOMATIC = True

SEARCH_PAGE_AUTO_SETUP = True

ES_AUTH = 'username:password'
ES_HOSTS = 'http://elasticsearch:9200'
ES_INDEX_PREFIX = 'cms-dev-{}'
ES_DOMAIN = 'http://localhost:8000'

HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter', ]
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': ES_HOSTS,
        'INDEX_NAME': ES_INDEX_PREFIX.format('cms'),
        'KWARGS': {'http_auth': ES_AUTH}
    }
}

ALDRYN_SEARCH_DEFAULT_LANGUAGE = 'en'
ALDRYN_SEARCH_REGISTER_APPHOOK = True

_INSTALLED_APPS = [
    'haystack',                # ElasticSearch
#    'search_page'              # Google Search
]
