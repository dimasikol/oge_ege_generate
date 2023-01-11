"""
Django settings for apps project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#AUTH_USER_MODEL = 'users.UserNet'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','django-insecure-8re*dlr1bqadk$21irkyblpcod31#)!gqcne@j@35e5z*i9h_%')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  True #bool(os.environ.get('DJANGO_DEBUG', True))
ALLOWED_HOSTS = ['192.168.88.200','185.246.193.35','127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'nested_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'crispy_forms',
    'crispy_bootstrap5',

    'lk',
    'users',
    'apps',
    'quiz',
    'shop',
    'privatmessages',
    'news',

    'debug_toolbar',
    'channels',

]
##'chanelmessages',


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgiref.inmemory.ChannelLayer',
        'ROUTING': 'apps.channel_routing',
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [

        ],
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

WSGI_APPLICATION = 'apps.wsgi.application'
ASGI_APPLICATION = "apps.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('192.168.88.200', 6379),('127.0.0.1', 6379)],
        },
    },
}
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES_SQLite = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES_POSTGERS = {
		'default': {
      	'ENGINE': 'django.db.backends.postgresql',
      	'HOST' : os.environ.get('POSTGRES_HOST', 'localhost'),
      	'NAME': os.environ.get('POSTGRES_DB', 'db_name'),
      	'USER': os.environ.get('POSTGRES_USER', 'username'),
      	'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
      	'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}
DATABASES=DATABASES_SQLite #DATABASES_SQLite if DEBUG else DATABASES_POSTGERS


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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



#smtp
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "no_replay@sch1190.ru"
EMAIL_HOST_PASSWORD = "Dima9194!"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKEND':(
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION':True,


    'ALGORITHM':'HS256',
    'SIGNING_KEY':SECRET_KEY,
    'VERIFYING_KEY':None,
    'AUDIENCE':None,
    'ISSUER':None,

    'AUTH_HEADER_TYPES':('JWT',),
    'USER_ID_FIELD':'id',
    'USER_ID_CLAIM':'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM':'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

}

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'


# Internationalization
if not(DEBUG):
    INTERNAL_IPS =["192.168.88.200",]
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# if DEBUG:
#     import socket
#     hostname,_,ips = socket.gethostbyname_ex(socket.gethostname())
#     INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
CKEDITOR_UPLOAD_PATH = "uploads/"
MEDIA_URL = '/media/'

#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]
else:
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    MEDIA_ROOT = 'media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'