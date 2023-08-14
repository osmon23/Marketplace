import random
import string

from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from django.core.mail import send_mail

from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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
Если вы не создавали нигде аккаунт то, проигнорируйте это письмо.
'''
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email if instance.email else settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [to_email])


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    subject = 'Password Reset for PM Ordo Marketplace.'
    token = reset_password_token.key
    message = f'''Здравствуйте, {reset_password_token.user.username}!
Вставьте этот токен на сайте.\n
                {token}\n
Для сброса пароля и введите новый пароль.
'''
    from_email = settings.EMAIL_HOST_USER
    to_email = reset_password_token.user.email
    send_mail(subject, message, from_email, [to_email])
