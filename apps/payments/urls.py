from django.urls import include, path
from rest_framework import routers

from apps.payments.views import PaymentTypeViewSet, PaymentViewSet, PaymentTypeChoicesView

router = routers.DefaultRouter()

router.register('types', PaymentTypeViewSet)
router.register('payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('type-choices/', PaymentTypeChoicesView.as_view()),
]