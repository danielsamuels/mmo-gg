"""
Production settings for mmo project.

For an explanation of these settings, please see the Django documentation at:

<http://docs.djangoproject.com/en/dev/>

While many of these settings assume sensible defaults, you must provide values
for the site, database, media and email sections below.
"""

import os
from django.core.urlresolvers import reverse_lazy


# The name of this site.  Used for branding in the online admin area.

SITE_NAME = "Posix MMO"

SITE_DOMAIN = "posix.me"

PREPEND_WWW = True


# Database settings.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mmo",
        "USER": "mmo",
        "PASSWORD": "s82qwhg2",
        "HOST": "",
        "PORT": ""
    }
}


# Absolute path to the directory where all uploaded media files are stored.

MEDIA_ROOT = "/home/mmo/webapps/mmo_media"

MEDIA_URL = "/media/"

FILE_UPLOAD_PERMISSIONS = 0644


# Absolute path to the directory where static files will be collected.

STATIC_ROOT = "/home/mmo/webapps/mmo_static"

STATIC_URL = "/static/"


# Email settings.

EMAIL_HOST = "smtp.webfaction.com"

EMAIL_HOST_USER = "mmo"

EMAIL_HOST_PASSWORD = "c7c4738b"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

SERVER_EMAIL = u"{name} <notifications@{domain}>".format(
    name = SITE_NAME,
    domain = SITE_DOMAIN,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME


# Error reporting settings.  Use these to set up automatic error notifications.

ADMINS = (
    ("Onespacemedia Errors", "errors@onespacemedia.com"),
)

MANAGERS = ()

SEND_BROKEN_LINK_EMAILS = False


# Locale settings.

TIME_ZONE = "Europe/London"

LANGUAGE_CODE = "en-gb"

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Auto-discovery of project location.

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# A list of additional installed applications.

INSTALLED_APPS = (
    "django.contrib.sessions",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.sitemaps",
    "south",
    "mmo.apps.areas",
    "mmo.apps.characters",
    "mmo.apps.enemies",
    "mmo.apps.items",
    "mmo.apps.site",
    "mmo.apps.spells",
)


# Additional static file locations.

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

STATIC_ASSETS = {
    "default": {
        "js": {
            "include": (
                "js/*.js",
            ),
        },
        "css": {
            "include": (
                "css/*.css",
            ),
        },
    },
}


# Dispatch settings.

MIDDLEWARE_CLASSES = (
    "django.middleware.transaction.TransactionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "mmo.urls"

WSGI_APPLICATION = "mmo.wsgi.application"

PUBLICATION_MIDDLEWARE_EXCLUDE_URLS = (
    "^admin/.*",
)

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

SITE_ID = 1


# Absolute path to the directory where templates are stored.

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, "templates"),
)

TEMPLATE_LOADERS = (
    ("django.template.loaders.cached.Loader", (
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)


# Namespace for cache keys, if using a process-shared cache.

CACHE_MIDDLEWARE_KEY_PREFIX = "mmo"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # Used for efficient caching of static assets.
    "optimizations": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 60 * 24,
        "LOCATION": "optimizations",
    },
}


# A secret key used for cryptographic algorithms.

SECRET_KEY = 'o%xha0q1pbk8s4+^m5z(@@czj179f9lf+_wurftawo194+*8a!'


# TinyMCE settings.

RICHTEXT_SETTINGS = {
    "default": {
        "theme": "advanced",
        "plugins": "table, advimage, inlinepopups, paste",
        "paste_auto_cleanup_on_paste": True,
        "paste_remove_spans": True,
        "paste_remove_styles": True,
        "theme_advanced_buttons1": "code,|,formatselect,styleselect,|,bullist,numlist,table,hr,|,bold,italic,|,link,unlink,image",
        "theme_advanced_buttons2": "",
        "theme_advanced_buttons3": "",
        "theme_advanced_resizing": True,
        "theme_advanced_path": False,
        "theme_advanced_statusbar_location": "bottom",
        "width": "1000px",
        "height": "350px",
        "dialog_type": "modal",
        "theme_advanced_blockformats": "h2,h3,p",
        "content_css": "css/screen.content.css",
        "extended_valid_elements": "iframe[scrolling|frameborder|class|id|src|width|height|name|align],article[id|class],section[id|class],a[rel|rev|charset|hreflang|tabindex|accesskey|type|name|href|target|title|class|onfocus|onblur|id],embed[*]",
        "convert_urls": False,
        "accessibility_warnings": False,
    }
}


# Logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}


LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = reverse_lazy('character:listing')
