from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddemo_localdb',
        'USER': 'ddemo_user',
        'PASSWORD': 'thebestpassword',
        'HOST': '',
        'PORT': '',
    }
}
