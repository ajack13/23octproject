import ast
import environ
from interview.base import *

env = environ.Env()
environ.Env.read_env('.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USERNAME'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': env.int('DB_PORT')
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'without_id': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'without_id',
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'without_id',
            'filename': os.path.join(BASE_DIR, 'logs', 'interview.log')
        },
    },
    'loggers': {
        'interview': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')
REDIS_DB = env.int('REDIS_DB')
REDIS_PASSWORD = env('REDIS_PASSWORD', default=False)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
REDIS_CONFIG = {'REDIS_URL': REDIS_URL}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ajaysrinivasan28@gmail.com'
EMAIL_HOST_PASSWORD = 'thedarkknight004.google'

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

SHARED_DRIVE_TYPE = env('SHARED_DRIVE_TYPE')
LINUX_SHARE_PATH = env('LINUX_SHARE_PATH')

CORS_ORIGIN_ALLOW_ALL = True

ARCHIVE_DIR = env('ARCHIVE_DIR', default=ARCHIVE_DIR)
TOTAL_DIRS = [ARCHIVE_DIR]

for DIRS in TOTAL_DIRS:
    if not os.path.exists(DIRS):
        os.makedirs(DIRS)
