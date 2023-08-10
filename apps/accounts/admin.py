from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Seller


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
    )
    list_display_links = (
        'username',
    )
    search_fields = (
        'username',
        'email',
        'phone_number',
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "photo",
            "address",
            "birthday",
            "job",
            "specialization",
            "whatsapp",
            "telegram",
            "role",
            )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


@admin.register(Seller)
class SellerAdmin(CustomUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "photo",
            "address",
            "birthday",
            "job",
            "specialization",
            "whatsapp",
            "telegram",
            "role",
            "INN",
            "type",
            "certificate_number",
            "confirmation_code",
            )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
