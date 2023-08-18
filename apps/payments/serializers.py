from datetime import timedelta

from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .constants import PaymentTypeChoices
from .models import PaymentType, Payment


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

        if not data.get('period'):
            data['period'] = _type.period

        data['end_date'] = data.get('start_date') + timedelta(days=data.get('period'))

        payment = data.get('membership').get_payment_by_date(
            data.get('start_date'),
            data.get('end_date'),
            exclude=data.get('pk') if data.get('pk') else None
        )

        if payment:
            raise serializers.ValidationError({
                'payment': _('The specified payment period overlaps with an existing payment')
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
