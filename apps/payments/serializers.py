from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from .models import PaymentType, Payment, TariffType, TariffPayment


class PaymentSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentType
        fields = '__all__'


class TariffTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffType
        fields = '__all__'


class TariffPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffPayment
        fields = '__all__'

# class MembershipPaymentSerializer(serializers.ModelSerializer):
#     type_name = serializers.CharField(source='type.name', read_only=True)
#
#     def validate(self, data):
#         _type = data.get('type')
#
#         if not _type:
#             raise serializers.ValidationError({
#                 'type': _('Payment type is required.')
#             })
#
#         if not data.get('amount'):
#             data['amount'] = _type.price
#
#         return data
#
#     class Meta:
#         model = Payment
#         fields = '__all__'
