from pathlib import Path

import os
import environ
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

INSTALLED_APPS = [

    'account.apps.AccountConfig',
    'todo.apps.TodoConfig',
    'widget_tweaks',    #DOM 属性等の操作
    # 'drf_writable_nested',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'webpack-loader',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',                # CSRF検証機能
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    os.path.join(BASE_DIR, "account/templates"),     
                    os.path.join(BASE_DIR, "todo/templates"),
                                   
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

WSGI_APPLICATION = 'config.wsgi.application' 



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{"min_length":6},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'


# collectstaticコマンドの配置先
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "account/static"),
    os.path.join(BASE_DIR, "todo/static"),
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.CustomUser'
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/top'
LOGOUT_REDIRECT_URL = '/login'


# ローカル設定ファイル読込
try:
    from .local_settings import *
except ImportError:
    pass


# 本番環境
if not DEBUG:

    import dj_database_url

    # redirect http access to https
    SECURE_SSL_REDIRECT = True



    env = environ.Env()
    env.read_env(os.path.join(BASE_DIR, '.env'))

    DATABASES = {
        'default':env.db(),
    }

    SECRET_KEY = env('SECRET_KEY')
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

    # Activate Django-Heroku.
    # django-heroku​ : Automatically configure your Django application to work on Heroku.
    django_heroku.settings(locals())


    # Configure your Django 
    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    
