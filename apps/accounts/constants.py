from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Role(TextChoices):
    ADMIN = "A", _("Admin")
    BUYER = "B", _("Buyer")
    SELLER = "S", _("Seller")
