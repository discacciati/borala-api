from rest_framework import permissions
from rest_framework.views import Request, View

from .models import User


class IsSuperUserPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj:User):
        return request.method in permissions.SAFE_METHODS or obj.user == request.user.is_superuser
