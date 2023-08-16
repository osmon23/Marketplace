from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, AddToCartView

router = DefaultRouter()
router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [
    path('api/add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),

]
urlpatterns += router.urls