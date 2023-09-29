from datetime import date

from celery import shared_task
from apps.payments.models import TariffPayment
from utils.time import get_current_date


@shared_task
def clear_tariffs():
    today = get_current_date()
    expired_tariffs = TariffPayment.objects.filter(end_date__lt=today, is_active=True)

    for tariff in expired_tariffs:
        store = tariff.store
        store.product_limit = 10
        store.save()
        tariff.is_active = False
        tariff.save()

# @shared_task
# def activate_payment():
#     today = get_current_date()
#     payments = Payment.objects.filter(start_date=today, is_active=False)
#
#     for payment in payments:
#         payment.is_active = True
#         payment.save()


# @shared_task
# def deduct_funds_daily():
#     payments = SellerPayment.objects.filter(start_date__lte=date.today())
#
#     for payment in payments:
#         amount_to_deduct = payment.type.price
#
#         wallet = Wallet.objects.get(seller=payment.seller)
#
#         if wallet.amount >= amount_to_deduct:
#             wallet.amount -= amount_to_deduct
#             wallet.save()

