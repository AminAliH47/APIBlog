from rest_framework import generics
from account.models import User
from account.serializer import UserSerializer
from permissions import permissions as cp  # Custom Permissions


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
