from events.models import Event
from rest_framework import permissions
from rest_framework.views import Request, View

from .models import LineUp


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj:LineUp):
        return request.method in permissions.SAFE_METHODS or obj.event.user.id == request.user.id


class IsEventOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj:Event):
        return request.method in permissions.SAFE_METHODS or obj.user.id == request.user.id
