from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentTypeChoices(models.TextChoices):
    MEMBERSHIP = 'Name', _('Name')
