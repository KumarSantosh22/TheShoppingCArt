from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from Shop.models import Customer, Product, Order, CartItem, OrderList
from Shop.sendmail import send_payment_confirmation
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import django.utils.timezone
import razorpay
import json

razorpay_client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))


def razorpay(request):
    billed_amt = request.session.get('billed_amount')
    print(billed_amt)
    data = {
        'amount': 100*100,
        "currency": "INR",
        "receipt": f"tsc_{django.utils.timezone.now()}",
        "notes": {
            "name": "{request.user.username}",
            "Payment_for": 'Payment for Shopping',
        }
    }
    razor = razorpay_client.order.create(data=data)
    print(razor)
    if request.method == 'POST':
        return redirect('razorpay_handler')
    return render(request, 'payment/razorpay.html', {'razor': razor, 'KEY_ID': settings.KEY_ID})


@csrf_exempt
def razorpay_handler(request):
    print('**********',request.user, '********')
    data = None
    if request.method == 'POST':
        data = request.POST
        razorpay_order_id = str(data['razorpay_order_id'])
        razorpay_payment_id = str(data['razorpay_payment_id'])
        razorpay_signature = str(data['razorpay_signature'])
        verify_sign = razorpay_client.utility.verify_payment_signature(data)
        if verify_sign is None:
            # send_payment_confirmation(
            #     request.user.first_name, request.user.email, razorpay_payment_id, request.session.get('billed_amount'))
            print("Payment Successfully Received")
            messages.success(request, 'Payment Successfully Received')
    return HttpResponse(json.dumps(data))

