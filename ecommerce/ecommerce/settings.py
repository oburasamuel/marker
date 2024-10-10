import os
from celery import Celery

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'ecommerce_db'),
        'USER': os.getenv('POSTGRES_USER', 'user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Redis caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Celery configuration
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
