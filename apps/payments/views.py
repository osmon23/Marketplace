from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .constants import PaymentTypeChoices
from .models import PaymentType, Payment
from .serializers import PaymentTypeSerializer, PaymentTypeChoiceSerializer, MembershipPaymentSerializer


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


class PaymentTypeChoicesView(APIView):
    queryset = PaymentTypeChoices.choices
    serializer_class = PaymentTypeChoiceSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)

#
#