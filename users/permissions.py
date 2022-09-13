from rest_framework import permissions
from rest_framework.views import Request, View

from .models import User


class IsSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_superuser


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        return request.user.id == obj.id


class IsSuperUserMethodOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        if request.method in view.admin_methods and request.user.is_superuser:
            return True

        return request.user.id == obj.id
