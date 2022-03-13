from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import re

phone_number_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_("Please enter a valid phone number"),
)


def validate_phone_number(value):
    if not re.match(r"^\+?1?\d{9,15}$", value):
        raise ValidationError(_("Please enter a valid phone number"))
    return value
