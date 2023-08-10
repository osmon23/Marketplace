from rest_framework import routers

from .views import ProductViewSet, StoreViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'stores', StoreViewSet, basename='stores')

urlpatterns = router.urls
