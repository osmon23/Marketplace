from django.contrib import admin

from apps.payments.models import PaymentType, Payment, Wallet


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'price',
    )
    list_display_links = ('name',)
    list_filter = ('type',)
    search_fields = (
        'name',
        'price'
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'type',
        'amount',
        'created_at',
        'start_date',
    )
    list_filter = (
        'type',
    )


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'amount',
    )