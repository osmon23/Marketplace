from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from utils.time import get_current_date

from ..stores.models import Product, Store


class PaymentType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    price = models.PositiveIntegerField(
        _('Price'),
        default=0
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Payment Type")
        verbose_name_plural = _("Payment Types")


class Payment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='payments',
        verbose_name=_('Product')
    )
    type = models.ForeignKey(
        PaymentType,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name=_('Payment Type')
    )
    amount = models.PositiveIntegerField(
        _('Payment amount'),
        null=True, blank=True
    )
    start_date = models.DateField(
        _('Start date of the payment period'),
        default=get_current_date
    )
    created_at = models.DateTimeField(
        _('Date of creation'),
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product} - {self.type}"

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def clean(self):
        if not self.type:
            raise ValidationError({
                'type': _('Payment type is required.')
            })

        if not self.amount:
            self.amount = self.type.price


class TariffType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    price = models.PositiveIntegerField(
        _('Price'),
        default=0,
    )
    period = models.PositiveIntegerField(
        _('Period'),
        default=0,
    )
    product_limit = models.PositiveIntegerField(
        _('Product limit'),
        default=10,
    )
    range_weight = models.PositiveIntegerField(
        _('Range weight'),
        default=0,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Tariff Type")
        verbose_name_plural = _("Tariff Types")


class TariffPayment(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.PROTECT,
        related_name='payments',
        verbose_name=_('Store')
    )
    type = models.ForeignKey(
        TariffType,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name=_('Tariff Type')
    )
    amount = models.PositiveIntegerField(
        _('Payment amount'),
        null=True, blank=True
    )
    period = models.PositiveIntegerField(
        _('Period'),
        null=True, blank=True
    )
    start_date = models.DateField(
        _('Start date of the payment period'),
        default=get_current_date
    )
    end_date = models.DateField(
        _('End date of payment period'),
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        _('Date of creation'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Update date'),
        auto_now=True
    )
    product_limit = models.PositiveIntegerField(
        _('Product limit'),
        default=10,
    )
    range_weight = models.PositiveIntegerField(
        _('Range weight'),
        default=0,
    )
    is_active = models.BooleanField(
        _('Is active'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.store} - {self.type}"

    class Meta:
        verbose_name = _("Tariff Payment")
        verbose_name_plural = _("Tariff Payments")

    def clean(self):
        if not self.type:
            raise ValidationError({
                'type': _('Tariff type is required.')
            })

        if not self.period:
            self.period = self.type.period

        self.end_date = self.start_date + timedelta(days=self.period)

        payment = self.store.get_payment_by_date(
            self.start_date,
            self.end_date,
            exclude=self.pk if self.pk else None
        )

        if payment:
            raise ValidationError({
                'start_date': _('The specified payment period overlaps with an existing payment for this '
                                'membership.')})

        if not self.amount:
            self.amount = self.type.price

        if not self.product_limit:
            self.product_limit = self.type.product_limit

        if not self.range_weight:
            self.range_weight = self.type.range_weight


