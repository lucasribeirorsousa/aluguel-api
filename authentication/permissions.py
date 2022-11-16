from rest_framework import permissions


class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.method == "POST":
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
