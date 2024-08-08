########################
# DJANGO
########################

SECRET_KEY = 'CHANGE_ME'

# Specify allowed hosts or use an asterisk to allow any host.
# ALLOWED_HOSTS = ['hostname.tacc.utexas.edu', 'client.org'] # Dev/Prod/Etc
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']   # Local

########################
# TACC: PORTAL
########################

CEP_AUTH_VERIFICATION_ENDPOINT = 'http://django:6000'

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
        'KWARGS': {'http_auth': ES_AUTH }
    }
}
