"""
Django settings for radiopolka project.

Generated by 'django-admin startproject' using Django 2.0a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import conf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o1!%zvuy-dzn7q9(b$g&hix+0mnfo9el0!+&y40$(^5_*8d8+s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = conf.DEBUG

ALLOWED_HOSTS = conf.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'ckeditor',
    'core',
    'version',
    'linkzilla.django'
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

ROOT_URLCONF = 'radiopolka.urls'

TEMPLATES = [
    {
        'NAME': 'jinja2',
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'core.jinja2.environment',
            'context_processors': [
                'linkzilla.django.context_processors.linkzilla',
            ]
        },
    },
    {
        'NAME': 'django',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

IMAGE_URL = "images/"
BOOK_URL = "books/"

THEME_NAME = getattr(conf, 'THEME_NAME', 'default')

THEME_IMAGE_URL = "images/themes/{0}/".format(THEME_NAME)
THEME_STYLESHEET_URL = "stylesheet/themes/{0}/".format(THEME_NAME)
THEME_JAVASCRIPT_URL = "javascript/themes/{0}/".format(THEME_NAME)


WSGI_APPLICATION = 'radiopolka.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = conf.DATABASES


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = getattr(conf, 'STATIC_ROOT', os.path.join(BASE_DIR, os.pardir, 'static'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = '{0}{1}'.format(BASE_DIR, MEDIA_URL)

CKEDITOR_UPLOAD_PATH = 'media/ckeditor'

ADMIN_SITE_HEADER = "Администрирование сайта www.radiopolka.ru"

LINKZILLA_SERVICES = ['sape', ]
LINKZILLA_CONFIG = {
    'sape': {
        'name': 'sape',
        'user': 'c147e46648d8cbbe8d21a7bdd550415a',
        'host': 'radiopolka.ru',
        'storage': {
            'name': 'dbm',
            'database_path': os.path.join(BASE_DIR, os.pardir, 'sape/links.db'),
        }
    }
}
