"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os 
from os import environ
import dotenv



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR_PARENT = Path(BASE_DIR).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vm&s^%hx08zk-it3ucpuvo_hyu$tcwvhbfq^5i#b_^+%j__2$b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "daphne",
    "rest_framework",
    "graphene_django",
    "channels",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 
    "home.apps.HomeConfig",
    "human.apps.HumanConfig",
    "info.apps.InfoConfig",
    # 
    "api.apps.ApiConfig",
    "shortener.apps.ShortenerConfig",
    # 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

GRAPHENE = {
    "SCHEMA": 'backend.schema.schema',
}

SITE_ID = 1

# Provider specifc settings 
# SOCIALACCOUNT_PROVIDERS = {

# }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR_PARENT, "frontend", "templates")
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

WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = "backend.asgi.application"



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

postgres_config = dotenv.dotenv_values(
    os.path.join(BASE_DIR, "config/.postgres.env")
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": postgres_config.get("DB"),
        "USER": postgres_config.get("USER"),
        "PASSWORD": postgres_config.get("PASSWORD"),
        "HOST": postgres_config.get("HOST"),
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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR_PARENT, "frontend",  "staticfiles")     # for collecting statcifiles
STATICFILES_DIRS = [
    os.path.join(BASE_DIR_PARENT, "frontend",  "static")
]

# MEDIA 
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR_PARENT, "frontend", "media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTHENTICATION BACKENDS
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of allauth 
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]