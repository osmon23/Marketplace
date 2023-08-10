from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import Seller


class Store(models.Model):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='stores',
        verbose_name=_('Seller'),
    )
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )
    logo = models.ImageField(
        _('Logo'),
        upload_to=f"stores/{name}/",
    )
    address = models.CharField(
        _('Address'),
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')


class Product(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Store'),
    )
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )
    price = models.PositiveIntegerField(
        _('Price'),
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Product'),
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f"products/{product.name}/",
    )

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')


class Specifications(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='specifications',
        verbose_name=_('Product'),
    )
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    value = models.TextField(
        _('Value'),
    )

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Specification')
        verbose_name_plural = _('Specifications')
