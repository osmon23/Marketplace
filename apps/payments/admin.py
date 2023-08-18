from django.contrib import admin

from apps.payments.models import PaymentType, Payment


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'price',
        'period'
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
        'product',
        'type',
        'amount',
        'period',
        'created_at',
        'start_date',
        'end_date',
        'is_active',
    )
    readonly_fields = (
        'end_date',
    )
    list_filter = (
        'type',
        'is_active',
        'end_date',
    )
