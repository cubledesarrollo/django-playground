# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Profile(models.Model):
    """ Datos de acceso al API de Google Plus relacionados con el user. """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='google')
    access_token = models.TextField()
