from celery import shared_task
from apps.payments.models import Payment
from utils.time import get_current_date


@shared_task
def clear_subscriptions():
    today = get_current_date()
    expired_payments = Payment.objects.filter(end_date__lt=today, is_active=True)

    for payment in expired_payments:
        payment = payment.product

        payment.is_active = False
        payment.end_date = today
        payment.save()


@shared_task
def activate_payment():
    today = get_current_date()
    payments = Payment.objects.filter(start_date=today, is_active=False)

    for payment in payments:
        payment.is_active = True
        payment.save()
