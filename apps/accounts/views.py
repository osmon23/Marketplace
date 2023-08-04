from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import CustomUserSerializer, SellerSerializer
from .models import CustomUser, Seller
from .constants import Role


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(role__in=[Role.ADMIN, Role.BUYER])
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]
