import django


DEBUG = True
USE_TZ = True

SECRET_KEY = "**************************************************"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "drf_related_object_field",
    "tests"
]

MIDDLEWARE = ()
