"""
Django settings for the_playstation_experiment project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from configurations import Configuration


class Base(Configuration):
    DEBUG = False

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "corsheaders",
        "rest_framework",
        "episodes",
        "games",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "the_playstation_experiment.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "the_playstation_experiment.wsgi.application"

    # Password validation
    # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

    PASSWORD_MINIMUM_LENGTH = 8

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
            "OPTIONS": {"min_length": PASSWORD_MINIMUM_LENGTH},
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Password hashing
    # https://docs.djangoproject.com/en/4.1/topics/auth/passwords/
    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
        "django.contrib.auth.hashers.ScryptPasswordHasher",
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/

    STATIC_URL = "static/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    # DRF
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": [
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ],
        "DEFAULT_PARSER_CLASSES": [
            "rest_framework.parsers.JSONParser",
            "rest_framework.parsers.FormParser",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework.authentication.SessionAuthentication",
        ],
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
        "PAGE_SIZE": 100,
    }

    # Storages
    STORAGES = {
        "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    AWS_STORAGE_BUCKET_NAME = "the-playstation-experiment-assets"
    AWS_QUERYSTRING_AUTH = False


class Local(Base):
    DEBUG = True

    SECRET_KEY = "django-insecure-78$76ac1&qq!w^(sygmcakxj!wh1(0++8o0r#nr=aj)bo!738@"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "psx",
            "USER": "psx",
            "PASSWORD": "xsp",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
    AWS_S3_REGION_NAME = "us-east-1"
    AWS_ACCESS_KEY_ID = "foo"
    AWS_SECRET_ACCESS_KEY = "bar"
    AWS_S3_ENDPOINT_URL = "http://localhost:4566"  # localstack endpoint
    IMAGES_BASE_URL = AWS_S3_ENDPOINT_URL


class Production(Base):
    DEBUG = False

    ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOST")]
    SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("POSTGRES_NAME", "playstation_experiment"),
            "USER": os.environ.get("POSTGRES_USER", "playstation_experiment"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        }
    }
    AWS_S3_REGION_NAME = "us-west-2"
    AWS_DEFAULT_ACL = "public-read"
    IMAGES_BASE_URL = "https://s3.{region}.amazonaws.com".format(
        region=AWS_S3_REGION_NAME
    )
