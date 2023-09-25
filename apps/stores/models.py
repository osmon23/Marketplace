from django.db import models
from django.utils.datetime_safe import date
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


from mptt.models import MPTTModel, TreeForeignKey

from apps.accounts.models import Seller
from utils.time import generate_dates


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


class Category(MPTTModel):
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        order_insertion_by = ['name']
        level_attr = 'mptt_level'


class FuelType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Fuel type')
        verbose_name_plural = _('Fuel types')


class Product(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Store'),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Category'),
        default=None,
    )
    fuel_type = models.ForeignKey(
        FuelType,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Fuel type'),
        null=True,
        blank=True,
    )
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    brand = models.CharField(
        _('Brand'),
        max_length=100,
    )
    country_of_origin = models.CharField(
        _('Country of origin'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )
    price = models.PositiveIntegerField(
        _('Price'),
        default=0
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0
    )

    def get_actual_payment(self):
        payments = self.payments.filter(
            start_date__lte=date.today(),
        )

        return payments.first()

    def get_payment_by_date(self, start_date: date, exclude: int = None):
        date_range = generate_dates(start_date,)

        payments = self.payments.filter(
            Q(start_date__in=date_range) | Q(end_date__in=date_range)
        ).exclude(pk=exclude)

        return payments.first()

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


class Review(models.Model):
    email = models.EmailField(
        blank=True,
        null=True
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
    )
    text = models.TextField(
        _("Text"),
        max_length=5000
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_("Parent"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children",
    )
    product = models.ForeignKey(
        Product,
        verbose_name="product",
        on_delete=models.CASCADE,
        related_name="reviews",
        default=None,
    )

    def __str__(self):
        return f"{self.product.name}"

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')


class ProductDiscount(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='discounts',
        verbose_name=_('product'),
    )
    discount = models.PositiveIntegerField(
        _('Discount'),
        default=0,
    )
    start_date = models.DateField(
        _('Start Date'),
    )
    end_date = models.DateField(
        _('End Date'),
    )

    def __str__(self):
        return f' Discount for {self.product.name}'

    class Meta:
        verbose_name = _('Product Discount')
        verbose_name_plural = _('Product Discounts')

    def calculate_discounted_price(self):
        return self.product.price * (100 - self.discount) / 100

