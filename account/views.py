from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User
from account.serializer import UserSerializer
from permissions import permissions as cp  # Custom Permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth


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


class LoginView(APIView):
    """
    Login View
    """

    def get(self):
        pass

    def post(self, request):
        # user = request.user
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            context = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
            }
            return Response(context, status=200)
        return Response({"msg": "user does not exist"}, status=401)
