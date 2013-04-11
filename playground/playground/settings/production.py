'''
Created on 11/04/2013

Based on https://github.com/twoscoops/django-twoscoops-project

@author: Cuble
'''
from .base import *  # @UnusedWildImport

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_setting('MYSQL_DB_NAME'),
        'USER': get_env_setting('MYSQL_DB_USER'),
        'PASSWORD': get_env_setting('MYSQL_DB_PASSWORD'),
        'HOST': get_env_setting('MYSQL_DB_HOST'),
        'PORT': get_env_setting('MYSQL_DB_PORT'),
    }
}
########## END DATABASE CONFIGURATION
