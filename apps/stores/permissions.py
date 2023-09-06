from rest_framework import permissions

from apps.stores.models import Store, Product


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.role == 'Seller')

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            if request.user.is_staff or request.user.role == 'Seller':
                if isinstance(obj, Store):
                    return obj.seller == request.user
                elif isinstance(obj, Product):
                    return obj.store.seller == request.user
        return False
