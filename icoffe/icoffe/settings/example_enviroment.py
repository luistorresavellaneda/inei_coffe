from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h2@82xat0gwa&i*qjnzx*z()6r5o5n&%6s+=nczpm0uwqe-@6v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'db1': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_1.sqlite3'),
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_2.sqlite3'),
    }
}

DATABASE_ROUTERS = ['core.dbrouters.DeliveryRouter', 'core.dbrouters.ComprasRouter']

CORS_ORIGIN_ALLOW_ALL = True