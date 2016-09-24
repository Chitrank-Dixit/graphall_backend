from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_secret('DATABASE_NAME'),
        'USER': get_secret('DATABASE_USER'),
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# stopped rds due to more money wasted in maintaining this
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': get_secret('DATABASE_NAME'),
#         'USER': get_secret('DATABASE_USER'),
#         'PASSWORD': get_secret('DATABASE_PASSWORD'),
#         'HOST': 'graphall-dev.c15tdklda9nm.us-west-2.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }
