from django.urls import  path

from rest_framework import routers

from .views import CustomUserViewSet, SellerViewSet

router = routers.DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'sellers', SellerViewSet, basename='sellers')

urlpatterns = router.urls
