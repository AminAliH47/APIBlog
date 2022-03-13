from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.validators import phone_number_validator


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=12,
        validators=[phone_number_validator],
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Phone number"),
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Email"),
    )
