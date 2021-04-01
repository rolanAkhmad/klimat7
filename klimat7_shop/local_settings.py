from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '6c!7n$rihn07!f1fcx0j=d6@5&69l)whafat-0&m3)2ck%_d(q'

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATICFILES_DIRS = [
#    Path(BASE_DIR / 'static'),
#    Path(BASE_DIR / 'store/static'),
#    Path(BASE_DIR / 'core/static'),
#    Path(BASE_DIR / 'cart/static'),
#    Path(BASE_DIR / 'userprofiles/static'),
# ]