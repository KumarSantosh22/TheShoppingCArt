import django.utils.timezone
from django.conf import settings
from django.core.mail import send_mail


def send_registration_mail(user_name, user_mail):
    subject = 'WELCOME TO TheShoppingCArt'
    message = f'Hi {user_name}, thank you for registering in TheShoppingCArt.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail,]
    send_mail(subject, message, email_from, recipient_list)

def send_login_mail(user_name, user_mail):
    subject = 'Login Review TheShoppingCArt'
    message = f'Hi {user_name}, You have successfully logged into TheShoppingCArt on {{django.utils.timezone.now}}. If this is not you then contact us immediately.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail,]
    send_mail(subject, message, email_from, recipient_list)
