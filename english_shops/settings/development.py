from english_shops.settings.settings import *

DJANGO_SETTINGS_MODULE = 'english_shops.settings.development'

SECRET_KEY = 'q2oobdb4$ls)f(7pz(=0wp&@39#vxyi92z91#a_$6bjw^^35+*'

DEBUG = True
IS_PRODUCTION = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST', 'pgdb-english-shops'),
        'PORT': 5432,
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres')
    }
}

JSON_FILE = '/code/english-shops.json'
