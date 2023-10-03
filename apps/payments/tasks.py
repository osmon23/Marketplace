from datetime import date

from celery import shared_task

from apps.accounts.models import Seller
from apps.payments.models import TariffPayment, Payment
from apps.stores.models import Product
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
        Product.objects.filter(store=store).update(range_weight=0)
        tariff.save()


@shared_task
def start_daily_payment():
    today = date.today()

    active_payments = Payment.objects.filter(start_date=today, is_active=True)

    for payment in active_payments:
        seller = payment.product.store.seller
        wallet = seller.wallet
        current_balance = wallet.amount

        payment_type = payment.type
        payment_amount = payment_type.price

        if current_balance < payment_amount:
            payment.is_active = False
            payment.delete()
        else:
            wallet.amount -= payment_amount
            wallet.save()


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

