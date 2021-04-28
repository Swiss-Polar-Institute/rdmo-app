import os

from rdmo.core.utils import sanitize_url

SITE_ID = 1

# set path-dependend settings
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

# import default settings from rdmo
from rdmo.core.settings import *

# import local settings from local.py
from .local import *

# update STATICFILES_DIRS for the vendor directory
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'vendor/')
]

# add static and templates from local.THEME_DIR to STATICFILES_DIRS and TEMPLATES
try:
    STATICFILES_DIRS.append(os.path.join(THEME_DIR, 'static/'))
    TEMPLATES[0]['DIRS'].append(os.path.join(THEME_DIR, 'templates/'))
except NameError:
    pass

# prepend the local.BASE_URL to the different URL settings
try:
    LOGIN_URL = sanitize_url(BASE_URL + LOGIN_URL)
    LOGIN_REDIRECT_URL = sanitize_url(BASE_URL + LOGIN_REDIRECT_URL)
    LOGOUT_URL = sanitize_url(BASE_URL + LOGOUT_URL)
    ACCOUNT_LOGOUT_REDIRECT_URL = sanitize_url(BASE_URL)
    MEDIA_URL = sanitize_url(BASE_URL + MEDIA_URL)
    STATIC_URL = sanitize_url(BASE_URL + STATIC_URL)

    CSRF_COOKIE_PATH = sanitize_url(BASE_URL + '/')
    LANGUAGE_COOKIE_PATH = sanitize_url(BASE_URL + '/')
    SESSION_COOKIE_PATH = sanitize_url(BASE_URL + '/')
except NameError:
    pass

# enable browsable API in DEBUG mode
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
