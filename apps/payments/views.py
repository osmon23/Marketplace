from datetime import timedelta

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters import rest_framework as filters
from django.db.models import F
from django.utils import timezone

from utils.time import get_current_date
from .models import PaymentType, Payment, TariffPayment, TariffType
from .serializers import PaymentTypeSerializer, MembershipPaymentSerializer, TariffTypeSerializer, \
    TariffPaymentSerializer
from ..stores.models import Product


class PaymentTypeViewSet(ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    permission_classes = [AllowAny]


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = MembershipPaymentSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['product', 'type']


class TariffTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TariffType.objects.all()
    serializer_class = TariffTypeSerializer
    permission_classes = [AllowAny]


class TariffPaymentViewSet(viewsets.ModelViewSet):
    queryset = TariffPayment.objects.all()
    serializer_class = TariffPaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def purchase_tariff(self, request):
        tariff_type_id = request.data.get('type')

        try:
            tariff_payment = TariffType.objects.get(pk=tariff_type_id)
        except TariffType.DoesNotExist:
            return Response({'error': 'Выбранный тип тарифа не существует.'}, status=status.HTTP_404_NOT_FOUND)

        seller = request.user

        if not hasattr(seller, 'seller'):
            return Response({'error': 'Вы не являетесь продавцом.'}, status=status.HTTP_403_FORBIDDEN)

        if seller.seller.wallet.amount < tariff_payment.price:
            return Response({'error': 'Недостаточно средств на кошельке для оплаты тарифа.'},
                            status=status.HTTP_400_BAD_REQUEST)

        seller.seller.wallet.amount -= tariff_payment.price
        seller.seller.wallet.save()

        products_to_update = Product.objects.filter(store=seller.seller.stores)

        products_to_update.update(range_weight=F('range_weight') + tariff_payment.range_weight)

        seller.seller.stores.product_limit = tariff_payment.product_limit
        seller.seller.stores.save()

        end_date = timezone.now() + timedelta(days=tariff_payment.period)
        TariffPayment.objects.create(
            store=seller.seller.stores,
            type=tariff_payment,
            amount=tariff_payment.price,
            period=tariff_payment.period,
            start_date=timezone.now(),
            end_date=end_date,
            product_limit=tariff_payment.product_limit,
            range_weight=tariff_payment.range_weight,
            is_active=True,
        )

        return Response({'message': 'Тариф успешно оплачен и активирован.'}, status=status.HTTP_201_CREATED)
