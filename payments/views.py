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
from .models import Transaction


billed_amt = ''
user_name = ''
user_email = ''
order = ''

def set_global(request):
    global billed_amt, user_name, user_email, order
    billed_amt = request.session.get('billed_amount')
    user_name = request.session.get('username')
    user_email = request.user.email
    order = request.session.get('order')
    return HttpResponse('')

razorpay_client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))


def razorpay(request):
    set_global(request)
    billed_amt = int(float(request.session.get('billed_amount'))) * 100
    print(f'************{billed_amt}***********')
    data = {
        'amount': billed_amt,
        "currency": "INR",
        "receipt": f"tsc_{django.utils.timezone.now()}",
        "notes": {
            "name": f"{request.user.username}",
            "Payment_for": 'Payment for Shopping',
        }
    }
    razor = razorpay_client.order.create(data=data)
    return render(request, 'payment/razorpay.html', {'razor': razor, 'KEY_ID': settings.KEY_ID})


@csrf_exempt
def razorpay_handler(request):
    data = None
    if request.method == 'POST':
        data = request.POST
        try:
            if data['error[code]']:
                datas = json.dumps(data)
                msg = f'Sorry! Payment is failed. Following are the details : \n {data}'
                return render(request, 'transaction_success.html', {'msg': msg})
        except:      
            verify_sign = razorpay_client.utility.verify_payment_signature(data)
            if verify_sign is None:
                razorpay_order_id = str(data['razorpay_order_id'])
                razorpay_payment_id = str(data['razorpay_payment_id'])
                razorpay_signature = str(data['razorpay_signature'])

                send_payment_confirmation(user_name, user_email, razorpay_payment_id, billed_amt)
                print("Payment Successfully Received")
                messages.success(request, 'Payment Successfully Received')
                
                ordr = Order.objects.get(pk=order)
                ordr.transaction_id = razorpay_payment_id
                ordr.save()

                tranz = Transaction(user=user_name, order_id=razorpay_order_id, payment_id=razorpay_payment_id, email=user_email, sign=razorpay_signature)
                tranz.save()
                html = f'<h1>Hurray! Payment is successful. Following are the details : </h1> {json.dumps(data)}'

            return render(request, 'transaction_success.html', {'data':data})

def testpay(request):
    set_global(request)
    html = f'{billed_amt} {user_name} {user_email}'
    return HttpResponse(html)
