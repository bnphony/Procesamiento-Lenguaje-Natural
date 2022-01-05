import os

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