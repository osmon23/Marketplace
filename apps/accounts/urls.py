from django.urls import  path, include

from rest_framework import routers

from .views import CustomUserViewSet, SellerViewSet, WalletDetail

router = routers.DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'sellers', SellerViewSet, basename='sellers')

urlpatterns = [
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('wallet/<int:pk>', WalletDetail.as_view(), name='wallet-detail'),

]

urlpatterns += router.urls
