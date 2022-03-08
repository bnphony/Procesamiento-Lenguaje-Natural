import os

import dj_database_url
from decouple import config



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prueba_2',
        'USER': 'postgres',
        'PASSWORD': '--REPLACED_1--',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

HEROKU = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}