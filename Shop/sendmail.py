import django.utils.timezone
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_registration_mail(user_name, user_mail):
    subject = 'TheShoppingCArt WELCOME'
    message = f'Hi {user_name}, Thank you for registering in TheShoppingCArt.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail, ]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)


def send_login_mail(user_name, user_mail):
    subject = 'TheShoppingCArt Login Review'
    message = f'Hi {user_name}, You have successfully logged into TheShoppingCArt on {django.utils.timezone.now()}. If this is not you then contact us immediately.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail, ]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)


def send_checkout_mail(user_name, user_mail, order_list, billed_amt):
    subject = 'TheShoppingCArt CheckoutInfo'
    message = f'Hi {user_name}, Thank you for shopping with us. Please continue to payment. You have shopped {order_list} and your billed amount is {billed_amt}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail, ]
    send_mail(subject, message, email_from,
              recipient_list, fail_silently=False)


def send_payment_confirmation(user_name, user_mail, transaction_id, billed_amt):
    subject = 'TheShoppingCArt Payment Confirmation'
    message = f'Hi {user_name}, Thank you for shopping with ust. You successfully made the payment of {billed_amt} with transaction id  {transaction_id} Please Keep it for future reference.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail, ]
    send_mail(subject, message, email_from,
              recipient_list, fail_silently=False)

def send_offers(email_list):
    subject = 'TheShoppingCArt Payment Confirmation'
    message = f'Hello TheShoppingCArt Users, We hope you all are doing well in this COVID time. We have great deals for you. Visit on TheShoppingCArt for more info. STAY HOME & SAFE & Shop With Us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = email_list
    send_mail(subject, message, email_from,
              recipient_list, fail_silently=False)

# template = render_to_string('templates/email_template.html', {'name': request.user.profile.first_name})
