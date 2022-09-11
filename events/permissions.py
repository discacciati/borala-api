from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Event


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request: Request, view: View, obj:Event):
        if request.method in permissions.SAFE_METHODS:
            return True

        return  obj.user.id == request.user.id or request.user.is_superuser

class IsPromoterOrReadOnly(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        user_can_post = request.user.is_authenticated and request.user.is_promoter

        return request.method in permissions.SAFE_METHODS or user_can_post
