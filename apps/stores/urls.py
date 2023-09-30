from rest_framework import routers

from django.urls import path

from . import views

from .views import ProductViewSet, StoreViewSet, ProductDiscountViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'stores', StoreViewSet, basename='stores')
router.register(r'discounts', ProductDiscountViewSet, basename='diescounts')

urlpatterns = [
    path("review/", views.ReviewCreateView.as_view(), name="review-create"),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
] + router.urls
