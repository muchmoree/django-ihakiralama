import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ipmap@5ll$g0z7du(*1-whv5f%5^8qg#g^hk1ft%7at@mxoy4-'

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
    'ihas',# Uygulama Tanıtma
    'user',# Uygulama Tanıtma
    'crispy_forms',# Django Kendi Formu
    'django_cleanup.apps.CleanupConfig',# Eğer user silinirse, user'a bağlı oluşan herşeyin(video-image-audio) silinmesi için
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

ROOT_URLCONF = 'iharent.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # Ürüne resim eklemek için
            ],
        },
    },
]

WSGI_APPLICATION = 'iharent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Database ayarlarını buradan yap. User, postgresql 'i ilk defa kuruyorsan
# default olarak postgres gelir ve şifreyi indirirken sorar. Port numarası default olarak 5432 dir.
# dc ile djangonun ilişki kurabilmesi için "pip install psycopg2" kurmalısın

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iha_db',
        'USER':'postgres',
        'PASSWORD':'12345',
        'HOST':'127.0.0.1',
        'PORT':'5433',
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

LANGUAGE_CODE = 'tr' # Program dilini buradan değiştir

TIME_ZONE = 'Europe/Istanbul' # Program saat formatını buradan ayarla

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/' # Programda kullanılacak temalar bu klasöre gider

# Programda kullanılacak tema dosyalarını tek elde toplamayı sağlar 
# (CSS, JavaScript, Images)(Uygulama içinde değil genel klasör olarak tanımlanır
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# Projeyi gerçek bir sunucuya yüklersen 
# bütün static dosyalarını toplayıp STATIC_ROOT youlunu tanımlamalısın
# Daha sonra bu kodu çalıştırmayı unutma "python manage.py collectstatic"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy formu için gereken paketi tanımla
CRISPY_TEMPLATE_PACK = 'bootstrap'

# Ürüne ekleyeceğin media dosyalarını yolunu ve ROOT 'u tanımla
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')