# -*- coding: utf-8 -*-
import random
import string
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    """ Manager para gestionar los aspectos característicos del modelo. """

    def create_user(self, email, password=None):
        """ Crea un usuario. """
        if not email:
            raise ValueError("Users must have an email address")
        if password is None:
            password = ''.join(random.choice(string.ascii_letters + \
                                             string.digits) for i in range(8))
        user = self.model(email=UserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Hereda de AbstractBaseUser y de PermissionsMixin. """
    email = models.EmailField(verbose_name=_("Email Address"),
                              max_length=255, unique=True,
                              db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Sobreescibimos el manager.
    objects = UserManager()
