from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from account.models import User
from account.serializer import UserSerializer
from permissions import permissions as cp  # Custom Permissions
from rest_framework.response import Response
from rest_framework.views import APIView


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


class RevokeToken(APIView):
    """ View for Revoke user token """

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def delete(self, request):
        request.auth.delete()
        return Response({"message": "token was revoked"}, status=204)
