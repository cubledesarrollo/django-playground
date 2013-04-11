'''
Created on 11/04/2013

Based on https://github.com/twoscoops/django-twoscoops-project

@author: Cuble
'''
from .base import *  # @UnusedWildImport


########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## END TEST SETTINGS


########## DATABASE CONFIGURATION
# In-memory configuration
DATABASES = {
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": ":memory:",
                    "USER": "",
                    "PASSWORD": "",
                    "HOST": "",
                    "PORT": "",
                },
             }
########## END DATABASE CONFIGURATION
