"""
Django settings for blogging_platform project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import cloudinary
import environ



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



SESSION_COOKIE_AGE = 3600 * 24 * 30

env = environ.Env()
environ.Env.read_env()

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'


cloudinary.config( 
  cloud_name = "dy8cpoo0r", 
  api_key = "471922696947476", 
  api_secret = "SjrxSsA1s0SvCZjUJcapZN8Obeg" 
)




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--qndeaqr((v)9o)ruch%-^n9ic_$o*d@5_=p&*(pv!k7_jn=vu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
     'ckeditor',
     'cloudinary',
     'blog',
  ]

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
 

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dy8cpoo0r',
    'API_KEY': '471922696947476',
    'API_SECRET': 'SjrxSsA1s0SvCZjUJcapZN8Obeg',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#         'height': 300,
#         'width': 800,
#     },
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


AUTH_USER_MODEL = "blog.CustomBlogUser"

LOGIN_REDIRECT_URL  = "/"
LOGOUT_REDIRECT_URL  = "/"
LOGIN_URL = "/login"


SECRET_KEY = 'SS65UGJIT3UeC02mTjXpNL2meyfkr6UQ'

ROOT_URLCONF = 'blogging_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR /'static/templates'
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

WSGI_APPLICATION = 'blogging_platform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bloggingsite',  # Replace with your database name
        'USER': 'root',               # Default MySQL user in XAMPP
        'PASSWORD': '',               # Leave empty if no password set
        'HOST': 'localhost',          # MySQL server host (localhost)
        'PORT': '3306',               # Default MySQL port
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
STATICFILES_DIRS = [
    BASE_DIR/'static'
]

 
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'