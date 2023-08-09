from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import CustomUserSerializer, SellerSerializer, UserUpdateSerializer, SellerUpdateSerializer
from .models import CustomUser, Seller
from .constants import Role


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(role__in=[Role.ADMIN, Role.BUYER])
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        return self.serializer_class


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'update':
            return SellerUpdateSerializer
        return self.serializer_class
