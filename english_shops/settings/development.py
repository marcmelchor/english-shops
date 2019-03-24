from english_shops.settings.settings import *

DJANGO_SETTINGS_MODULE = 'eng_shops.settings.development'

SECRET_KEY = 'q2oobdb4$ls)f(7pz(=0wp&@39#vxyi92z91#a_$6bjw^^35+*'

DEBUG = True
IS_PRODUCTION = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'shop-api',
        'USER': 'postgres',
        'PASSWORD': 'marc'
    }
}

JSON_FILE = 'C:\\Code\\english_shops.json'
