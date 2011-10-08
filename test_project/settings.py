import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, os.path.dirname(PROJECT_ROOT))

DEBUG=True
TEMPLATE_DEBUG=True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/flatblocks.db'
SITE_ID = 1
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'flatblocks',
]
try:
    import south
    INSTALLED_APPS.append('south')
except ImportError, _:
    pass

LANGUAGE_CODE="en"
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
ROOT_URLCONF = 'test_project.urls'
