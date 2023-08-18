from datetime import timedelta, time

from django.db import models
from django.utils.datetime_safe import date
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from utils.time import get_current_date
from .constants import PaymentTypeChoices
# from utils.time import get_current_date

from ..stores.models import Product


class PaymentType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    type = models.CharField(
        _('Membership Type'),
        max_length=100,
        choices=PaymentTypeChoices.choices,
        default=PaymentTypeChoices.MEMBERSHIP
    )
    price = models.PositiveIntegerField(
        _('Price'),
        default=0
    )
    period = models.PositiveIntegerField(
        _('Period'),
        default=1
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
        verbose_name=_('Membership Type')
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
    is_active = models.BooleanField(
        _('Is active'),
        null=True,
        blank=True,
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

        if not self.period:
            self.period = self.type.period

        self.end_date = self.start_date + timedelta(days=self.period)

        payment = self.product.get_payment_by_date(
            self.start_date,
            self.end_date,
            exclude=self.pk if self.pk else None
        )

        if payment:
            raise ValidationError({
                'start_date': _('The specified payment period overlaps with an existing payment for this '
                                'payment.')})

        if not self.amount:
            self.amount = self.type.price
