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

HEROKU = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddqattk5bvmbq0',
        'HOST': 'ec2-3-225-79-57.compute-1.amazonaws.com',
        'USER': 'vbdjpyqxrsktel',
        'PASSWORD': '--REPLACED_2--',
        'PORT': 5432,
    }
}
#Hola
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}