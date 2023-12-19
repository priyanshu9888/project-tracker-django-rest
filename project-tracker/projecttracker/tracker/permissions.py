# tracker/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access for unauthenticated users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow full access for authenticated users
        return request.user and request.user.is_authenticated
