# Mailman Web configuration file.
# /etc/mailman3/settings.py

# Get the default settings.
from mailman_web.settings.base import *
from mailman_web.settings.mailman import *
import pymysql

# Settings below supplement or override the defaults.

#: Default list of admins who receive the emails from error logging.
ADMINS = (
    ('Mailman Suite Admin', 'postmaster@example.com'),
)

# Database setup.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mailmanweb',
        'USER': 'mailman',
        'PASSWORD': '[MYSQL-USER-PASSWORD]',
        'HOST': '[MYSQL-IP-ADDRESS]',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}
# Fake PyMySQL's version and install as MySQLdb
# https://adamj.eu/tech/2020/02/04/how-to-use-pymysql-with-django/
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

# 'collectstatic' command will copy all the static files here.
# Alias this location from your webserver to `/static`
STATIC_ROOT = '/opt/app-root/src/mailman/web/static'

# enable the 'compress' command.
COMPRESS_ENABLED = True

# Make sure that this directory is created or Django will fail on start.
LOGGING['handlers']['file']['filename'] = '/opt/app-root/src/mailman/web/logs/mailmanweb.log'

#: See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",  # Archiving API from Mailman, keep it.
    "127.0.0.1",
    "lists.example.com",
]

#: See https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins
#: For Django <4.0 these are of the form 'lists.example.com' or
#: '.example.com' to include subdomains and for Django >=4.0 they include
#: the scheme as in 'https://lists.example.com' or 'https://*.example.com'.
CSRF_TRUSTED_ORIGINS = [
    "https://lists.example.com",
]

#: Current Django Site being served. This is used to customize the web host
#: being used to serve the current website. For more details about Django
#: site, see: https://docs.djangoproject.com/en/dev/ref/contrib/sites/
SITE_ID = 0

# Set this to a new secret value.
SECRET_KEY = '[SECRET-KEY]'

# Set this to match the api_key setting in
# /opt/mailman/mm/mailman-hyperkitty.cfg (quoted here, not there).
MAILMAN_ARCHIVER_KEY = '[MAILMAN-ARCHIVER-KEY]'

# The sender of emails from Django such as address confirmation requests.
# Set this to a valid email address.
DEFAULT_FROM_EMAIL = 'mailman@example.com'

# The sender of error messages from Django. Set this to a valid email
# address.
SERVER_EMAIL = 'mailman@example.com'

# Outgoing mail to our relay
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'relay.int.example.com'
EMAIL_PORT = 25

# Use Xapian for full-text indexing
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': "/opt/app-root/src/mailman/fulltext_index",
    },
#    'default': {
#        'ENGINE': 'xapian_backend.XapianEngine',
#        'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index')
#    },
}

# Sort multiple domains
FILTER_VHOST = 1

# Default to something more likely
TIME_ZONE = 'America/New_York'
USE_TZ = True

# Social logins
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_UNIQUE_EMAIL = True
INSTALLED_APPS = [
    'hyperkitty',
    'postorius',
    'django_mailman3',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_gravatar',
    'compressor',
    'haystack',
    'django_extensions',
    'django_q',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.yahoo',
]
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    },
    'facebook': {
       'METHOD': 'oauth2',
       'SCOPE': ['email', 'public_profile'],
       'FIELDS': [
           'email',
           'name',
           'first_name',
           'last_name',
           'locale',
           'timezone',
           ],
    },
}

# Fix for updated django-allauth
MIDDLEWARE += ('allauth.account.middleware.AccountMiddleware',)
