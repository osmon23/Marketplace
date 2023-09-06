from rest_framework import permissions


class IsStaffOrSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
            if request.user.role == 'seller':
                return True

        return False
