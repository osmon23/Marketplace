from rest_framework import permissions

from apps.stores.models import Store, Product


class IsAdminOrSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешение для GET-запросов (читать разрешено всем)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверка для остальных методов (POST, PUT, PATCH, DELETE)
        return request.user and (request.user.is_staff or hasattr(request.user, 'seller'))
