from rest_framework import permissions




class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем GET-запросы всем
        if request.method == 'GET':
            return True
        # Разрешаем POST, PUT, PATCH и DELETE только для аутентифицированных "Seller" и "is_staff"
        elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and (request.user.is_staff or request.user.role == 'Seller')
        return False

    def has_object_permission(self, request, view, obj):
        # Разрешаем доступ к объекту всем
        return True
#
# class IsStaffOrSellerOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         if request.user.is_authenticated:
#             if request.user.is_staff:
#                 return True
#             if request.user.role == 'seller':
#                 return True
#
#         return False
