from pathlib import Path
import os
import environ

env = environ.Env(
    DEBUG=(bool, True)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = [
    # env('HOST'),
    'http://127.0.0.1:8000',
    'https://a39b-82-215-113-148.ngrok-free.app'
]

# Application definition

INSTALLED_APPS = [
    # local apps
    'account', 'journal', 'dinamic', 'article',
    # external apps
    'ckeditor',
    'ckeditor_uploader',
    "corsheaders",
    'modeltranslation',
    "jazzmin",

    # 'tinymce', 'cuser', 'suit',
    # default django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'project.middleware.LanguageMiddleWare',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # "django.core.context_processors.i18n",
                # "django.core.context_processors.media",
                # "django.core.context_processors.static",
                # "django.core.context_processors.tz",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# custome admin panel

# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / env('DATABASE_NAME'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('DATABASE_NAME'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('DATABASE_PASSWORD'),
#         'HOST': env('DATABASE_HOST'),
#         'PORT': env('DATABASE_PORT'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static') 
STATICFILES_DIRS =  os.path.join(BASE_DIR, "static" ),
# STATICFILES_STORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage' # new


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'account.CustomUser'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

LOGIN_URL = 'login'

# Model translator
LANGUAGE_CODE = 'en'

gettext = lambda s: s

LANGUAGES = (
    ('uz', gettext('O`zbek')),
    ('ru', gettext('Русский')),
    ('en', gettext('English')),
)

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')
TRANSLATABLE_MODEL_MODULES = ["journal.models", "dinamic.models"]
IS_MONOLINGUAL=False


# CKEDITOR CONFIGURE

CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_BASEPATH = "uploads/ckeditor/"
CKEDITOR_CONFIGS = {
    'default': { 
        'toolbar': 'Custom',
        'width': '100%',
        'height': '300',
        'font_names': '"Raleway","HelveticaNeue","Helvetica Neue",Helvetica,Arial,sans-serif;',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'config.font_names': '"Raleway","HelveticaNeue","Helvetica Neue",Helvetica,Arial,sans-serif;',
    },
}


#  JAZZMIN SETTINGS

from project import jazzmin

JAZZMIN_SETTINGS = jazzmin.JAZZMIN_SETTINGS

JAZZMIN_UI_TWEAKS = jazzmin.JAZZMIN_UI_TWEAKS


