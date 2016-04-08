from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False

class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsMasterAdminOfSite(permissions.BasePermission):
    def has_object_permission(self, request, view, masteradmin):
        if request.user:
            return masteradmin.user == request.user
        return False


class IsClientOfSite(permissions.BasePermission):
    def has_object_permission(self, request, view, masteradmin):
        if request.user:
            return masteradmin.user == request.user
        return False