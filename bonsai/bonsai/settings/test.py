from settings.base import *  # NOQA

# TEST SETTINGS
DEBUG = False

# IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

# STORAGE
STATICFILES_STORAGE = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# END STORAGE

SECRET_KEY = '12345678954563rqewvsbeh245'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
