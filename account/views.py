from django.contrib.auth.models import update_last_login
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from account.models import User
from account.serializer import (
    UserSerializer,
    UserLoginSerializer,
    UserRegisterView,
)
from permissions import permissions as cp  # Custom Permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    """ list of active articles """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (cp.IsSuperuserOrStaffReadonly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ detail of active article """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (cp.IsSuperuserOrStaffReadonly,)
    authentication_classes = (JWTAuthentication,)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterView(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        context = {
            "refresh_token": refresh_token,
            "access_token": access_token,
            "user": {
                "pk": user.pk,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        }

        response = Response()
        response.set_cookie(key='refresh-token', value=refresh_token, httponly=True)
        response.set_cookie(key='access-token', value=access_token, httponly=True)
        response.set_cookie(key='isAuth', value=True, httponly=False)
        response.data = context
        response.status_code = 200

        return response


class LoginView(APIView):
    """
    User login View
    """

    def post(self, request):
        serializer = UserLoginSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        context = {
            "refresh_token": refresh_token,
            "access_token": access_token,
            "user": {
                "pk": user.pk,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        }

        response = Response()
        response.set_cookie(key='refresh-token', value=refresh_token, httponly=True)
        response.set_cookie(key='access-token', value=access_token, httponly=True)
        response.set_cookie(key='isAuth', value=True, httponly=False)
        response.data = context
        response.status_code = 200

        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('refresh-token')
        response.delete_cookie('access-token')
        response.data = {
            "message": "User logged out successfully"
        }
        return response
