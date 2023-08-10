import random
import string

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from config import settings
from .models import Seller


def generate_random_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(10))
    return code


@receiver(post_save, sender=Seller)
def send_seller_code(sender, instance, created, **kwargs):
    if created:
        subject = f'Marketplace PM Ordo.'
        random_code = generate_random_code()
        instance.confirmation_code = random_code
        instance.save()
        message = f'''Здравствуйте, {instance.username}.
Для того чтобы подтвердить свою учетную запись вставьте ниже сгенерированный код:\n\n
                {random_code}\n\n
Никому не передавайте код! 
Если вы не создавали нигде аккаунт или вошли через Gmail аккаунт, то проигнорируйте это письмо.
'''
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email if instance.email else settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [to_email])
