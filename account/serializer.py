from abc import ABC

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from account.models import User
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(serializers.Serializer):
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

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password,
            )
            if not user:
                message = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError({"message": message}, code="authorization")
        else:
            message = _('Please enter the "username" and "password"')
            raise serializers.ValidationError({"message": message}, code="authorization")

        data['user'] = user

        return data


class UserRegisterView(serializers.Serializer):
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

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:

            query = User.objects.filter(username=username)
            if query.exists():
                message = _('The user already has a username')
                raise serializers.ValidationError({"message": message}, code="authorization")

            password = make_password(password)
            user = User(
                username=username,
                password=password
            )

            user.save()

        else:
            message = _('Please enter the "username" and "password"')
            raise serializers.ValidationError({"message": message}, code="authorization")

        print(user)
        data['user'] = user

        return data
