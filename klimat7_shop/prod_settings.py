from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '6c!7n$rihvvn07!f1fcxssd0j=d6@5&6922l)whafa44sdfgt-0&m3)2ck%_d(q'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '78.40.109.163', 'klimat7-shop.kz', '*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'klimat7',
#         'USER': 'z00sharp',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATICFILES_DIRS = [
    Path(BASE_DIR / 'static'),
    Path(BASE_DIR / 'store/static'),
    Path(BASE_DIR / 'core/static'),
    Path(BASE_DIR / 'cart/static'),
    Path(BASE_DIR / 'userprofiles/static'),
]