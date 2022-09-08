from rest_framework import permissions

from reviews.models import Review


class CustomProductPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Review):

        return request.method in permissions.SAFE_METHODS or (request.user == obj.user)
