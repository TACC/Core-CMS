########################
# DJANGO
########################

SECRET_KEY = 'CHANGE_ME'

########################
# STORAGE
########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'PORT': '5432',
        'NAME': 'taccsite',
        'USER': 'postgresadmin',
        'PASSWORD': 'taccforever',
        'HOST': 'core_cms_postgres'
    }
}

########################
# SEARCH
########################

ES_AUTH = 'username:password'
ES_HOSTS = 'http://elasticsearch:9200'
ES_INDEX_PREFIX = 'cms-dev-{}'
ES_DOMAIN = 'http://localhost:8000'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': ES_HOSTS,
        'INDEX_NAME': ES_INDEX_PREFIX.format('cms'),
        'KWARGS': {'http_auth': ES_AUTH}
    }
}
