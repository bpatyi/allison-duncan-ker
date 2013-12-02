from .base import *

DEBUG = True
DEBUG_TEMPLATE = True

ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'storages.backends.ftp.FTPStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.ftp.FTPStorage'

FTP_USER = os.environ.get('FTP_USER')
FTP_PASSWORD = os.environ.get('FTP_PASSWORD')
FTP_HOST = os.environ.get('FTP_HOST')
FTP_PORT = os.environ.get('FTP_PORT')

FTP_STORAGE_LOCATION = 'ftp://%s:%s@%s:%s/' % (FTP_USER, FTP_PASSWORD, FTP_HOST, FTP_PORT)

MEDIA_ROOT = 'http://static.alisonduncankerr.com/'
STATIC_ROOT = 'http://static.alisonduncankerr.com/'
STATIC_URL = 'http://static.alisonduncankerr.com/static/'
MEDIA_URL = 'http://static.alisonduncankerr.com/media/'

ADMIN_MEDIA_PREFIX = STATIC_ROOT + "grappelli/"