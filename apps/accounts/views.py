from django.shortcuts import render

from rest_framework import viewsets, status, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from .serializers import (
    CustomUserSerializer,
    SellerSerializer,
    UserUpdateSerializer,
    SellerUpdateSerializer, StoreSerializer, ProductSerializer, WalletSerializer,
)
from .models import CustomUser, Seller, Wallet
from .constants import Role
from .permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(role__in=[Role.ADMIN, Role.BUYER])
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        return self.serializer_class


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.is_active = False
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if not hasattr(self, 'wallet'):
            Wallet.objects.create(seller=instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == 'update':
            return SellerUpdateSerializer
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        store_data = StoreSerializer(instance.stores).data
        product_data = ProductSerializer(instance.stores.products.all(), many=True).data
        wallet_data = WalletSerializer(instance.wallet).data

        data['store'] = store_data
        data['products'] = product_data
        data['wallet'] = wallet_data

        return Response(data, status=status.HTTP_200_OK)


class WalletDetail(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    # def get_object(self):
    #     return self.request.user.wallet


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    if user:
        data = {
            'id': user.id,
            'role': user.role,
            'email': user.email,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Пользователь не найден'}, status=404)

