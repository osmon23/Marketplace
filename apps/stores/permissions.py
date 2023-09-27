from rest_framework import permissions

from apps.stores.models import Store, Product


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and (request.user.is_staff or request.user.role == 'Seller')
        return True

    def has_object_permission(self, request, view, obj):
        return True