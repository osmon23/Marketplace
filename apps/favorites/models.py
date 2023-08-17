from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import CustomUser
from apps.stores.models import Product


class Favorite(models.Model):
    customer = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name=_('CustomUser'),
    )
    items = models.ManyToManyField(
        Product,
        through='FavoriteItem',
    )

    def __str__(self):
        return f"Favorite for {self.customer.username}"

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        related_name='favorite_items',
        verbose_name=_('Favorite'),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('product'),
    )

    def __str__(self):
        return f"{self.product.name} in {self.favorite}"

    class Meta:
        verbose_name = _('Favorite Item')
        verbose_name_plural = _('Favorite Items')

