import os
from pathlib import Path

import environ

env = environ.Env()

# environ.Env.read_env(env_file=Path('./env/.env'))
environ.Env.read_env(env_file=Path('.env'))


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env('SECRET_KEY')


DEBUG = int(env('DEBUG', default=1))

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split()

CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS').split()


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',

    'users',
    'selections',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'kino.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
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

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.template.context_processors.debug",
    "django.template.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
)

WSGI_APPLICATION = 'kino.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('POSTGRES_HOST'),
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'PORT': env('POSTGRES_PORT'),
    }
}

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

# LOGGING = {
#     "version": 1,
#     "handlers": {
#         'console': {'class': 'logging.StreamHandler'}
#     },
#     "loggers": {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG'
#         }
#     }
# }


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"

CELERY_BROKER_URL = env('CELERY_BROKER_URL')

KINOPOISK_API_URL = 'https://api.kinopoisk.dev/v1.4/movie/random'

ADDITIONAL_REQUEST_PARAM = {
        'rating.kp': '6-10',
        'year': '2000-2023',
}