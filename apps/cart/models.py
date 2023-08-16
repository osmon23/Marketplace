from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import Seller, CustomUser
from apps.stores.models import Product


class Cart(models.Model):
    customer = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name=_('CustomUser'),
    )
    items = models.ManyToManyField(
        Product,
        through='CartItem'
    )

    def __str__(self):
        return f"Cart for {self.customer.username}"

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name=_('Cart'),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('product'),
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0
    )

    def __str__(self):
        return f"{self.product.name} in {self.cart}"

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')

