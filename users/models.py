from datetime import datetime

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class SevenVirtuesUsersManager(BaseUserManager):

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(
            self.model.USERNAME_FIELD)

        return self.get(**{case_insensitive_username_field: username})

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        now = datetime.utcnow()
        user = self.model(
            email=email,
            is_active=True,
            is_superuser=is_superuser,
            is_staff=is_staff,
            last_login=now,
            date_joined=now,
            **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class SevenVirtuesUsers(AbstractBaseUser, PermissionsMixin):
    is_account_owner = models.BooleanField(default=True)

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = SevenVirtuesUsersManager()

    USERNAME_FIELD = 'email'

    def __str__(self):

        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)

        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.__str__()
