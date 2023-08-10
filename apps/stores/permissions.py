from rest_framework import permissions

from .models import Product, Store


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_superuser or request.user.role == 'Seller')

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.role == 'Seller':
            if isinstance(obj, Store):
                return obj.seller == request.user
            elif isinstance(obj, Product):
                return obj.store.seller == request.user
        return False
