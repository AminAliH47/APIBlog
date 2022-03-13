from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.models import User
from django.utils.translation import gettext_lazy as _

from common.validators import validate_phone_number


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=120,
        label=_("Username"),
    )
    password = serializers.CharField(
        max_length=120,
        label=_("Password"),
        style={"input_type": "password"},
        write_only=True,
        trim_whitespace=True,
    )

    def validate_username(self, value):
        if '@' in value.lower():
            try:
                validate_email(value)
            except ValidationError:
                raise serializers.ValidationError(_("Please enter a valid email address"))
        else:
            value = validate_phone_number(value)

        return value

    def validate_password(self, value):
        value = make_password(value)
        return value


class UserValidationSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=120,
        label=_("Phone number or Email"),
    )
    password = serializers.CharField(
        max_length=120,
        label=_("Password"),
        style={"input_type": "password"},
        write_only=True,
        trim_whitespace=True,
    )

    # def validate(self, data):
    #     username = data.get('username')
    #
    #     if username :
    #         if '@' in username:
    #
    #
    #     else:
    #         message = _('Please enter the "username" and "password"')
    #         raise serializers.ValidationError({"message": message}, code="authorization")

    # return data
