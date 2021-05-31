import os
from . import BASE_DIR

DEBUG = os.environ['DEBUG'] == '1'


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = []

i = 1
while f'ALLOWED_HOST_{i}' in os.environ:
    ALLOWED_HOSTS.append(os.environ[f'ALLOWED_HOST_{i}'])
    i += 1

'''
The root url of your application, only needed when its not '/'
'''

# BASE_URL = '/path'

'''
Language code and time zone
'''
LANGUAGE_CODE = 'en-CH'
TIME_ZONE = 'Europe/Berlin'

LANGUAGES = (
    ('en', 'English'),
)

'''
The database connection to be used, see also:
http://rdmo.readthedocs.io/en/latest/configuration/databases.html
'''

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

if os.environ.get('MYSQL_DATABASE_ENABLED', '0') == '1':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
        }
    }
elif os.environ.get('SQLITE3_DATABASE_ENABLED', '0') == '1':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.environ['SQLITE3_FILE_NAME'],
        }
    }
else:
    assert False

'''
E-Mail configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/email.html
'''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = SERVER_EMAIL = os.environ['FROM_EMAIL']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True

ADMINS = []
i = 1
while f'ADMIN_{i}' in os.environ:
    name_email = os.environ[f'ADMIN_{i}']
    ADMINS.append(name_email.split(','))
    i += 1

# When uploading our domain we have many attributes
DATA_UPLOAD_MAX_NUMBER_FIELDS=10000

'''
Allauth configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/allauth.html
'''

from rdmo.core.settings import INSTALLED_APPS, AUTHENTICATION_BACKENDS

ACCOUNT = True
ACCOUNT_SIGNUP = True
SOCIALACCOUNT = False

INSTALLED_APPS += [
    'allauth',
    'allauth.account',
    'spi_translations',
]

#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.facebook',
#     'allauth.socialaccount.providers.github',
#     'allauth.socialaccount.providers.google',
#     'allauth.socialaccount.providers.orcid',
#     'allauth.socialaccount.providers.twitter',
# ]
#
# AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')

'''
LDAP, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/ldap.html
'''

# import ldap
# from django_auth_ldap.config import LDAPSearch
# from rdmo.core.settings import AUTHENTICATION_BACKENDS
#
# PROFILE_UPDATE = False
#
# AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
# AUTH_LDAP_BIND_DN = "cn=admin,dc=ldap,dc=example,dc=com"
# AUTH_LDAP_BIND_PASSWORD = "admin"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=ldap,dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
#
# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     'email': 'mail'
# }
#
# AUTHENTICATION_BACKENDS.insert(
#     AUTHENTICATION_BACKENDS.index('django.contrib.auth.backends.ModelBackend'),
#     'django_auth_ldap.backend.LDAPBackend'
# )

'''
Shibboleth, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/shibboleth.html
'''

# from rdmo.core.settings import INSTALLED_APPS, AUTHENTICATION_BACKENDS, MIDDLEWARE
#
# SHIBBOLETH = True
# PROFILE_UPDATE = False
#
# INSTALLED_APPS += ['shibboleth']
#
# SHIBBOLETH_ATTRIBUTE_MAP = {
#     'uid': (True, 'username'),
#     'givenName': (True, 'first_name'),
#     'sn': (True, 'last_name'),
#     'mail': (True, 'email'),
# }
#
# AUTHENTICATION_BACKENDS.append('shibboleth.backends.ShibbolethRemoteUserBackend')
#
# MIDDLEWARE.insert(
#     MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
#     'shibboleth.middleware.ShibbolethRemoteUserMiddleware'
# )
#
# LOGIN_URL = '/Shibboleth.sso/Login?target=/projects'
# LOGOUT_URL = '/Shibboleth.sso/Logout'

'''
Theme, see also:
http://rdmo.readthedocs.io/en/latest/configuration/themes.html
'''

THEME_DIR = os.path.join(BASE_DIR, 'theme')

'''
Export Formats
'''

from django.utils.translation import ugettext_lazy as _
EXPORT_FORMATS = (
    ('pdf', 'PDF'),
    ('rtf', 'Rich Text Format'),
    ('odt', 'Libre Office'),
    ('docx', 'Microsoft Office'),
    ('html', 'HTML'),
    ('markdown', 'Markdown'),
    ('mediawiki', 'mediawiki'),
    ('tex', 'LaTeX')
)

'''
Cache, see also:
http://rdmo.readthedocs.io/en/latest/configuration/cache.html
'''

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#         'KEY_PREFIX': 'rdmo_default'
#     },
#     'api': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#         'KEY_PREFIX': 'rdmo_api'
#     },
# }

'''
Logging configuration
'''

# import os
# from . import BASE_DIR

# LOGGING_DIR = os.path.join(BASE_DIR, 'log')
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue'
#         }
#     },
#     'formatters': {
#         'default': {
#             'format': '[%(asctime)s] %(levelname)s: %(message)s'
#         },
#         'name': {
#             'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
#         },
#         'console': {
#             'format': '[%(asctime)s] %(message)s'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         },
#         'error_log': {
#             'level': 'ERROR',
#             'class':'logging.FileHandler',
#             'filename': os.path.join(LOGGING_DIR, 'error.log'),
#             'formatter': 'default'
#         },
#         'rdmo_log': {
#             'level': 'DEBUG',
#             'class':'logging.FileHandler',
#             'filename': os.path.join(LOGGING_DIR, 'rdmo.log'),
#             'formatter': 'name'
#         },
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#         },
#         'django.request': {
#             'handlers': ['mail_admins', 'error_log'],
#             'level': 'ERROR',
#             'propagate': True
#         },
#         'rdmo': {
#             'handlers': ['rdmo_log'],
#             'level': 'DEBUG',
#             'propagate': False
#         }
#     }
# }
