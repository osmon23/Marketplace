from rest_framework import routers

from django.urls import include, path

from apps.payments.views import PaymentTypeViewSet, PaymentViewSet, TariffTypeViewSet, TariffPaymentViewSet

router = routers.DefaultRouter()

router.register('types', PaymentTypeViewSet)
router.register('payment', PaymentViewSet)
router.register(r'tariff-types', TariffTypeViewSet, basename='tariff-type')
router.register(r'tariff-payments', TariffPaymentViewSet, basename='tariff-payment')

urlpatterns = [
    path('', include(router.urls)),
]