# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django.contrib.auth
from pathlib import Path

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
django.contrib.auth.LOGIN_URL = '/'
#import dj_database_url  #obligatoria para RENDER

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-aq8)3gd8k^k-pz4b%98cf^_ktn6vg1&97@f*(s8$wkh+%9o)yh'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-aq8)3gd8k^k-pz4b%98cf^_ktn6vg1&97@f*(s8$wkh+%9o)yh')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appcastillocongosto',
    #'allauth',
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

ROOT_URLCONF = 'pcastillocongosto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        # este directorio no puede estar vacío es donde busca las plantillas hay que incluirlo
        # este concretamente utiliza el directorio templates del proyecto
        # 'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [  # procesadores de contexto
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pcastillocongosto.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

if DEBUG == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'dbcastillo'),
            'USER': os.getenv('DB_USER', 'postgres'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'Adivinala1.'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
SITE_ID = 1
SITE_NAME = "Castillo"
#SITE_URL = "http://127.0.0.1:8000/"
LANGUAGE_CODE = 'es-ES'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'djblets.siteconfig.context_processors.siteconfig',
    'djblets.util.context_processors.settingsVars',
    'djblets.util.context_processors.siteRoot',
    'djblets.util.context_processors.ajaxSerial',
    'djblets.util.context_processors.mediaSerial',
	'django.template.context_processors.request',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
#STATIC_URL = 'static/'
#la parte estática es obligatoria para Heroku y para nuestra máquina
STATIC_URL = '/static/'    #js, css3, ..
MEDIA_URL = '/media/'  #videos, imágenes

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') ??render
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# declara la ruta donde se enlazará el contenido estático
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
	('css', os.path.join(STATIC_ROOT, 'css')),
	('js', os.path.join(STATIC_ROOT, 'js')),
	('images', os.path.join(STATIC_ROOT, 'images')),
    ('img', os.path.join(STATIC_ROOT, 'img')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'infoclub3000@gmail.com'# emisor
EMAIL_HOST_PASSWORD = 'aaaaaaaaaa'
EMAIL_USE_TLS = True  #seguridad de gmail
#EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

