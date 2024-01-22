"""
Django settings for postgresTest project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y*rxe6-0%710fdy)#70qqilj3s0$5-xb_xy*h(bk!cr!&_^r+q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mpsn-iq.onrender.com', '127.0.0.1', 'www.mpsn-iq.org', 'mpsn-iq.org', 'mpsn-iq:10000']


# Application definition

INSTALLED_APPS = [
    'testdb',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'postgresTest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'postgresTest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mpsn_data_poc7',
        'USER': 'mpsn_data_poc7_user',
        'PASSWORD': 'lv94lwsO8qQ7AZy80YXAwWAgx8vq8TOx',
        'HOST': 'dpg-cigcoud9aq012ev1fn0g-a',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
            'sslrootcert': '/path/to/certificate.crt',

        },
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres', 
#         'USER': 'postgres', 
#         'PASSWORD': 'k8k8k8k8',
#         'HOST': 'localhost', 
#         'PORT': '5432',
#     }
# }

SECURE_SSL_CIPHERS = 'HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK'
SECURE_SSL_PROTOCOLS = ['TLSv1.2', 'TLSv1.3']


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# import dj_database_url


# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv('DATABASE_URL', "postgres://mpsn_data_poc7_user:lv94lwsO8qQ7AZy80YXAwWAgx8vq8TOx@dpg-cigcoud9aq012ev1fn0g-a.oregon-postgres.render.com/mpsn_data_poc7"), conn_max_age=60)
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AWS_STORAGE_BUCKET_NAME = 'mpsniq'
# AWS_ACCESS_KEY_ID = '22a34f8a6bd9'
# AWS_SECRET_ACCESS_KEY = '0056eb1268619cb1888b77de11a5c32b2fa8a06202'
AWS_URL='s3.us-east-005.backblazeb2.com'
# AWS_DEFAULT_ACL = None
# AWS_S3_REGION_NAME = 'us-east-005'
# AWS_S3_SIGNATURE_VERSION = 's3v4'


BACKBLAZEB2_ACCOUNT_ID = '22a34f8a6bd9'
BACKBLAZEB2_APP_KEY_ID = '22a34f8a6bd9'
BACKBLAZEB2_APP_KEY = '0056eb1268619cb1888b77de11a5c32b2fa8a06202'
BACKBLAZEB2_BUCKET_NAME = 'mpsniq'
BACKBLAZEB2_BUCKET_ID = 'd242fa3344ef589a867b0d19'

# test

# pylint: disable=unused-import
import django_backblaze_b2.storage

# BACKBLAZE_CONFIG = {
#     'bucket_name': 'mpsniq',
#     'account_id': '22a34f8a6bd9',
#     'application_key_id': '22a34f8a6bd9',
#     'application_key': '0056eb1268619cb1888b77de11a5c32b2fa8a06202',
#     'bucket_id': 'd242fa3344ef589a867b0d19',
#     'bucket_endpoint': 'https://s3.us-east-005.backblazeb2.com',
# }


# from django.conf import settings


# bucket_name = settings.BACKBLAZE_CONFIG['AWS_STORAGE_BUCKET_NAME']
# account_id = settings.BACKBLAZE_CONFIG['AWS_ACCESS_KEY_ID']
# application_key_id = settings.BACKBLAZE_CONFIG['AWS_ACCESS_KEY_ID']
# application_key = settings.BACKBLAZE_CONFIG['AWS_SECRET_ACCESS_KEY']
# bucket_endpoint = settings.BACKBLAZE_CONFIG['AWS_URL']




# DEFAULT_FILE_STORAGE = 'django_backblaze_b2.storage.B2Storage'
# STATICFILES_STORAGE = 'django_backblaze_b2.storage.B2Storage'

from b2_storage.storage import B2Storage


DEFAULT_FILE_STORAGE = 'b2_storage.storage.B2Storage'
STATICFILES_STORAGE = 'b2_storage.storage.B2Storage'



# DEFAULT_FILE_STORAGE = 'django_b2storage.storage.backends.B2Storage'
# STATICFILES_STORAGE = 'django_b2storage.storage.backends.B2Storage'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



STATIC_URL = AWS_URL + '/static/'
MEDIA_URL = AWS_URL + '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# USE_X_FORWARDED_HOST = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'testdb-home'

LOGIN_URL = 'login'

# import django_heroku
# django_heroku.settigns(locals(), staticfiles=False)
