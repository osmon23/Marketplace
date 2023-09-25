from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import (
    CustomUserSerializer,
    SellerSerializer,
    UserUpdateSerializer,
    SellerUpdateSerializer,
)
from .models import CustomUser, Seller
from .constants import Role
from .permissions import IsOwnerOrReadOnly
from ..payments.models import Wallet


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
# aaa