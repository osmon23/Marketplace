from django.contrib import admin

from apps.payments.models import PaymentType, Payment, TariffType, TariffPayment


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
    )
    list_display_links = ('name',)
    search_fields = (
        'name',
        'price',
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


@admin.register(TariffType)
class TariffTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'period',
        'product_limit',
        'range_weight',

    )
    list_display_links = ('name',)
    search_fields = (
        'name',
        'price',
    )


@admin.register(TariffPayment)
class TariffPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'store',
        'type',
        'amount',
        'period',
        'start_date',
        'end_date',
        'created_at',
        'is_active',
        'product_limit',
        'range_weight',
    )
    list_filter = (
        'is_active',
    )
    list_display_links = (
        'store',
    )