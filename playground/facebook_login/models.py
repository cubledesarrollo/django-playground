from django.db import models
from django.conf import settings


class Profile(models.Model):
    """ Datos de acceso al API de Facebook relacionados con el user. """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='facebook')
    facebook_id = models.BigIntegerField(unique=True, db_index=True)
    access_token = models.TextField(db_index=True)
