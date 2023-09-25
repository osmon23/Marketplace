from datetime import timedelta, time

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from utils.time import get_current_date
from .constants import PaymentTypeChoices
from apps.accounts.models import Seller
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


class SellerPayment(models.Model):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name=_('Seller')
    )


class Wallet(models.Model):
    seller = models.OneToOneField(
        Seller,
        on_delete=models.CASCADE,
        related_name='wallet',
        verbose_name=_('Seller')
    )
    amount = models.PositiveIntegerField(
        _('Amount'),
        default=0
    )

    def __str__(self):
        return f"{self.seller.email} - {self.amount}"

    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")