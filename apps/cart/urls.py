from django.urls import path
from .views import AddToCartView, RemoveFromCartView, CartItemsListView

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart-items-list', CartItemsListView.as_view(), name='cart-items-list'),
]
