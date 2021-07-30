from mailjet_rest import Client
import django.utils.timezone
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


api_key = ''
api_secret = ''


def send_registration_mail(user_name, to_mail):
    subject = 'TheShoppingCArt WELCOME'
    message = f'Hi {user_name}, Thank you for registering in TheShoppingCArt.'
    email_from = settings.EMAIL_HOST_USER

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": email_from,
                    "Name": "TheShoppingCArt"},
                "To": [
                    {
                        "Email": to_mail,
                        "Name": user_name,
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"{message} <br/><h3>Kindly visit on  <a href='https://www.google.com'>TheShoppingCArt's Team </a>!</h3><br />Have a nice day!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def send_login_mail(user_name, to_mail):
    subject = 'TheShoppingCArt Login Review'
    message = f'Hi {user_name}, You have successfully logged into TheShoppingCArt on {django.utils.timezone.now()}. If this is not you then contact us immediately.'
    email_from = settings.EMAIL_HOST_USER

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": email_from,
                    "Name": "TheShoppingCArt"},
                "To": [
                    {
                        "Email": to_mail,
                        "Name": user_name,
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"{message} <br/><h3>Kindly visit on  <a href='https://www.google.com'>TheShoppingCArt's Team </a>!</h3><br />Have a nice day!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def send_checkout_mail(user_name, to_mail, order_list, billed_amt):
    subject = 'TheShoppingCArt CheckoutInfo'
    message = f'Hi {user_name}, Thank you for shopping with us. Please continue to payment. You have shopped {order_list} and your billed amount is {billed_amt}'
    email_from = settings.EMAIL_HOST_USER

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": email_from,
                    "Name": "TheShoppingCArt"},
                "To": [
                    {
                        "Email": to_mail,
                        "Name": user_name,
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"{message} <br/><h3>Kindly visit on  <a href='https://www.google.com'>TheShoppingCArt's Team </a>!</h3><br />Have a nice day!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def send_payment_confirmation(user_name, to_mail, transaction_id, billed_amt):
    subject = 'TheShoppingCArt Payment Confirmation'
    message = f'Hi {user_name}, Thank you for shopping with ust. You successfully made the payment of {billed_amt} with transaction id  {transaction_id} Please Keep it for future reference.'
    email_from = settings.EMAIL_HOST_USER

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": email_from,
                    "Name": "TheShoppingCArt"},
                "To": [
                    {
                        "Email": to_mail,
                        "Name": user_name,
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"{message} <br/><h3>Kindly visit on  <a href='https://www.google.com'>TheShoppingCArt's Team </a>!</h3><br />Have a nice day!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def send_offers(email_list):
    subject = 'TheShoppingCArt Payment Confirmation'
    message = f'Hello TheShoppingCArt Users, We hope you all are doing well in this COVID time. We have great deals for you. Visit on TheShoppingCArt for more info. STAY HOME & SAFE & Shop With Us'
    email_from = settings.EMAIL_HOST_USER

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": email_from,
                    "Name": "TheShoppingCArt"},
                "To": [
                    {
                        "Email": to_mail,
                        "Name": user_name,
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"{message} <br/><h3>Kindly visit on  <a href='https://www.google.com'>TheShoppingCArt's Team </a>!</h3><br />Have a nice day!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def sendmail(subject, message, to_mail):

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "shkr2209@gmail.com",
                    "Name": "TheShoppingCArt"},
                "To": [
                    {
                        "Email": to_mail,
                        "Name": ""
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"{message} <br/><h3>Kindly visit on  <a href='https://www.google.com'>TheShoppingCArt's Team </a>!</h3><br />Have a nice day!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
