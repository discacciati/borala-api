from rest_framework import permissions
from rest_framework.views import Request, View
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Event


class IsOwnerOrReadyOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj:Event):
        return request.method in permissions.SAFE_METHODS or obj.user == request.user or request.user.is_superuser