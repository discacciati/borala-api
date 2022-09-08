from rest_framework import permissions
from rest_framework.views import Request, View

from .models import User


class IsSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.method in permissions.SAFE_METHODS or request.user.is_superuser


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        return request.user.id == obj.id


class IsSuperUserDeleteOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        if request.method == 'DELETE' and request.user.is_superuser:
            return True

        return request.user.id == obj.id