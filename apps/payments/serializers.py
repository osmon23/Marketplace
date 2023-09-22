from datetime import timedelta

from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .constants import PaymentTypeChoices
from .models import PaymentType, Payment, Wallet


class PaymentInlineSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = Payment
        exclude = ('product',)


class PaymentTypeSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=PaymentTypeChoices.choices)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for k, v in zip(PaymentTypeChoices.values, PaymentTypeChoices.labels):
            if k == data['type']:
                data['type'] = {'value': k, 'label': v}
        return data

    class Meta:
        model = PaymentType
        fields = '__all__'


class MembershipPaymentSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)

    def validate(self, data):
        _type = data.get('type')

        if not _type:
            raise serializers.ValidationError({
                'type': _('Payment type is required.')
            })

        if not data.get('amount'):
            data['amount'] = _type.price

        return data

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentTypeChoiceSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()

    def to_representation(self, obj):
        return {'value': str(obj[0]), 'label': str(obj[1])}


class WalletSerializer(serializers.Serializer):
    class Meta:
        model = Wallet
        fields = (
            'id',
            'amount',
        )
