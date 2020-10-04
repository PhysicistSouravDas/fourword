from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from app.accounts.managers import UserManager
from app.base.models import BaseFourWordModel


class User(AbstractBaseUser, PermissionsMixin, BaseFourWordModel):
    """Django model class to represent User table.
    """
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=16)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128, blank=True, null=False)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ('first_name', 'last_name', )

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'
