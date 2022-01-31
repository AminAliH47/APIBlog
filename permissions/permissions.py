from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsSuperuserOrStaffReadonly(permissions.BasePermission):
    message = 'You do not have permission to access.'

    def has_permission(self, request, view):
        return bool(
            # just Readonly access for staff users
            request.method in SAFE_METHODS and request.user.is_staff or
            # Full access for superusers
            request.user.is_authenticated and request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            # just Readonly access for staff users
            request.method in SAFE_METHODS and request.user.is_staff or
            # Full access for superusers
            request.user.is_authenticated and request.user.is_superuser
        )
