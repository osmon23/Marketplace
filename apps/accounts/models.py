from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .constants import Role, Type
from .validators import validate_inn

class CustomUser(AbstractUser):
    email = models.EmailField(
        _('Email'),
        unique=True,
    )
    phone_number = PhoneNumberField(
        _('Phone number'),
        unique=True,
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to='users/',
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        _('Birthday'),
        null=True,
        blank=True,
    )
    job = models.CharField(
        _('Job'),
        max_length=255,
        null=True,
        blank=True,
    )
    specialization = models.CharField(
        _('Specialization'),
        max_length=255,
        null=True,
        blank=True,
    )
    address = models.CharField(
        _('Address'),
        max_length=255,
        null=True,
        blank=True,
    )
    whatsapp = models.URLField(
        _('WhatsApp'),
        null=True,
        blank=True,
    )
    telegram = models.URLField(
        _('Telegram'),
        null=True,
        blank=True,
    )
    role = models.CharField(
        _('Role'),
        max_length=1,
        choices=Role.choices,
        default=Role.BUYER,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.role == Role.ADMIN:
            self.is_staff = True
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Seller(CustomUser):
    INN = models.PositiveIntegerField(
        _('INN'),
        unique=True,
        validators=[validate_inn],
    )
    type = models.CharField(
        _('Type'),
        max_length=1,
        choices=Type.choices,
        default=Type.NATURAL,
        null=True,
        blank=True,
    )
    certificate_number = models.PositiveIntegerField(
        _('Certificate number'),
        null=True,
        blank=True,
    )
    confirmation_code = models.CharField(
        _('Confirmation Code'),
        max_length=10,
        null=True,
        blank=True,
    )

    REQUIRED_FIELDS = ['username', 'role', 'INN']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.role = Role.SELLER
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = _('Seller')
        verbose_name_plural = _('Sellers')
