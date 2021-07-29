from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import datetime
import json
from django.core import serializers

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm

from .models import Seller, Customer, Product, Order, CartItem, OrderList
from .forms import SignUpForm, ProfileEditForm, SellerSignUpForm, SellerProfileEditForm, ProductForm

from .sendmail import send_registration_mail, send_login_mail, send_checkout_mail, send_payment_confirmation


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def aboutus(request):
    return render(request, 'about/about.html')


def contactus(request):
    return render(request, 'about/contact.html')


def careers(request):
    return render(request, 'about/careers.html')


def page_not_found(request):
    now = datetime.datetime.now()
    html = "<h1>%s</h1> <h1> Error in loading</h1><h1>Error 404... Page Not Found !</h1>" % now
    return HttpResponse(html)


# USER, SELLER, CUSTOMER AUTHENTICATION AND AUTHORIZATION MANAGEMENT

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            request.session['username'] = username
            print('*********USER DATA : ', user)
            customer = Customer(user=user)
            customer.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                print('*********USER DATA : ', user)
                send_login_mail(request.user.first_name, request.user.email)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        cust = Customer.objects.get(user=request.user)
        return render(request, 'profile.html', {'user': user, 'cust': cust})
    else:
        messages.info(request, 'Login to acess your profile.')
        return redirect('userlogin')


def updateprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = Customer.objects.get(user=request.user)
            fmd = ProfileEditForm(request.POST, request.FILES, instance=user)
            print(fmd.is_valid())
            if fmd.is_valid():
                fmd.save()
                for d in fmd.cleaned_data.values():
                    print(d)
                image = fmd.cleaned_data['image']
                first_name = fmd.cleaned_data['first_name']
                last_name = fmd.cleaned_data['last_name']
                email = fmd.cleaned_data['email']
                phone = fmd.cleaned_data['phone']
                dob = fmd.cleaned_data['dob']
                residential_address = fmd.cleaned_data['residential_address']
                permanent_address = fmd.cleaned_data['permanent_address']
                delievery_address = fmd.cleaned_data['delievery_address']

                User.objects.filter(username=request.user).update(
                    first_name=first_name, last_name=last_name, email=email)

                # Customer.objects.filter(user=request.user).update(image=image, phone=phone, residential_address=residential_address, permanent_address=permanent_address, delievery_address=delievery_address)

                messages.success(request, 'Profile Successfully Updated!')
                return redirect('userprofile')

        user = User.objects.get(username=request.user)
        cust = Customer.objects.get(user=request.user)
        form = ProfileEditForm()
        return render(request, 'update_profile.html', {'user': user, 'cust': cust, 'form': form})
    else:
        messages.info(request, 'Login to update your profile.')
        redirect('Login')


# Managing Seller

def seller(request):
    return render(request, 'about/seller.html')


def signupseller(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            gp = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            request.session['username'] = username
            print('*********USER DATA : ', user)
            seller = Seller(user=user)
            seller.save()

            group = Group.objects.get(name='GroupSeller')
            gp.groups.add(group)

            messages.success(
                request, 'You are now a member of TheShoppingCArt! Thank you! for chosing us.')

            return redirect('home')
    else:
        form = SellerSignUpForm()
    return render(request, 'signup_seller.html', {'form': form})


def sellerprofile(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = User.objects.get(username=request.user)
            seller = Seller.objects.get(user=request.user)
            return render(request, 'seller_profile.html', {'user': user, 'seller': seller})
        messages.warning(request, 'You are not not a seller!')
        return redirect('userlogin')
    else:
        messages.info(request, 'Login to acess your profile.')
        return redirect('userlogin')


def updateseller(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                user = Seller.objects.get(user=request.user)
                fmd = SellerProfileEditForm(
                    request.POST, request.FILES, instance=user)
                print(fmd.is_valid())
                if fmd.is_valid():
                    fmd.save()
                    for d in fmd.cleaned_data.values():
                        print(d)

                    first_name = fmd.cleaned_data['first_name']
                    last_name = fmd.cleaned_data['last_name']
                    email = fmd.cleaned_data['email']

                    User.objects.filter(username=request.user).update(
                        first_name=first_name, last_name=last_name, email=email)

                    messages.success(request, 'Profile Successfully Updated!')
                    return redirect('sellerprofile')

            user = User.objects.get(username=request.user)
            seller = Seller.objects.get(user=request.user)
            form = SellerProfileEditForm(instance=seller)
            return render(request, 'update_seller_profile.html', {'user': user, 'seller': seller, 'form': form})
    else:
        messages.info(request, 'Login to update your profile.')
        redirect('Login')


def dashboard(request):
    if request.user.is_authenticated and request.user.is_staff:
        seller = Seller.objects.get(user=request.user)
        product = Product.objects.all()
        messages.success(request, 'Welcome to Admin Dashboard')
        return render(request, 'dashboard.html', {'seller': seller, 'products': product})


def addproduct(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                Product.objects.create(seller=request.user, image=form.cleaned_data['image'], name=form.cleaned_data['name'], brand=form.cleaned_data['brand'], model=form.cleaned_data['model'], year=form.cleaned_data['year'], description=form.cleaned_data['description'], price=form.cleaned_data['price'], in_stock=form.cleaned_data['in_stock'], stock_qty=form.cleaned_data['stock_qty'],
                                       reorder_qty=form.cleaned_data['reorder_qty'], is_discount=form.cleaned_data['is_discount'], discount=form.cleaned_data['discount'], category=form.cleaned_data['category'], subcategory=form.cleaned_data['subcategory'], season=form.cleaned_data['season'], type_choice=form.cleaned_data['type_choice'], exp_date=form.cleaned_data['exp_date'], rating=form.cleaned_data['rating'])
                for f in form.cleaned_data.values():
                    print(f)
                messages.success(request, 'Product added successfully.')
        form = ProductForm()
        return render(request, 'product/add_products.html', {'form': form})


# PRODUCT MANAGEMENT FOR EACH CATEGORY

def product(request, id):
    # This function is for view details of product
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {'product': product})


def delproduct(request, id):
    prod = Product.objects.get(pk=id)
    prod.delete()
    messages.success(request, 'Product Successfully Deleted.')
    return redirect('dashboard')


def updateproduct(request, id):
    if id is not None:
        prod = Product.objects.get(pk=id)
    form = ProductForm(instance=prod)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully')
            return redirect('dashboard')
    return render(request, 'product/update_product.html', {'form': form})


# Different Product Pages

def products_electronics(request):
    return HttpResponse("")


def product_tv_appliances(request):
    pass


def products_men(request):
    pass


def products_women(request):
    pass


def products_kids(request):
    pass


def products_pc(request):
    pass


def products_phones(request):
    pass


def products_books(request):
    pass


def products_(accessories):
    pass


# Managing Cart

def updateitem(request):
    json_data = json.loads(request.body)
    productId = json_data['productId']
    action = json_data['action']
    print('Product ID: ', productId)
    print('Action: ', action)

    customer = Customer.objects.get(user=request.user)
    product = Product.objects.get(pk=productId)

    print(json_data)
    order, created = Order.objects.get_or_create(customer=customer)
    request.session['order'] = order.pk
    orderItem, created = CartItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        if orderItem.quantity:
            orderItem.quantity += 1
        else:
            orderItem.quantity = 1
    elif action == 'remove':
        if orderItem.quantity > 0:
            orderItem.quantity -= 1
        else:
            orderItem.quantity = 0

    orderItem.save()

    if request.session.get('total_price') and request.session.get('total_items_in_cart'):
        order.invoice = request.session.get('total_price')
        order.no_of_items = request.session.get('total_items_in_cart')
        order.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def cartitem(request):
    cart = CartItem.objects.filter(order=request.session.get('order'))
    print(cart.values())
    invoice = 0
    total_qty = 0
    for item in cart:
        item.total = item.product.price * item.quantity
        item.save()
        invoice += item.total
        total_qty += item.quantity
        print(invoice, total_qty)
        print(item.product.name)
    request.session['total_items_in_cart'] = total_qty
    request.session['total_price'] = int(invoice)

    return render(request, 'cart.html', {'cart': cart, 'invoice': invoice, 'total_qty': total_qty})


def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        addr4 = request.POST.get('addr4')
        addr5 = request.POST.get('addr5')
        addr6 = request.POST.get('addr6')
        address = f'{addr1}, {addr2}, {addr3}, {addr6},\n {addr4}, {addr5}'
        billed_amount = request.POST.get('billed_amount')
        request.session['billed_amount'] = billed_amount

        ordered_items = []
        cart_items = CartItem.objects.filter(
            order=request.session.get('order'))
        for item in cart_items.values():
            print(item)
            ordered_items.append(item)

        # qs_json = serializers.serialize('json', cart_items)
        # print(qs_json)

        print(str(ordered_items))

        order_list = OrderList(user=request.user, order=Order.objects.get(pk=request.session.get(
            'order')), list_of_order=ordered_items, billed_amount=billed_amount, shipping_address=address, phone=contact)

        order_list.save()
        ordr = Order.objects.get(pk=request.session.get('order'))
        ordr.order_date = datetime.datetime.now().date()
        ordr.save()
        cart_items.delete()
        del request.session['total_items_in_cart']
        del request.session['total_price']

        return redirect('payment')

    return render(request, 'product/checkout.html')


def payment(request):
    import num2word
    amt = num2word.word(int(float(request.session['billed_amount'])))
    return render(request, 'payment.html', {'amount_words': amt})


# Footer Items

def privacy(request):
    return render(request, "policy/privacy.html")


def payment_help(request):
    return render(request, "help/payments.html")


def ship_info(request):
    return render(request, "help/ship_info.html")


def return_help(request):
    return render(request, "help/cancellation&returns.html")


def return_policy(request):
    return render(request, "policy/return_policy.html")


def security(request):
    return render(request, "policy/security.html")


def tandc(request):
    return render(request, "policy/terms&use.html")


def faq(request):
    return render(request, "help/faq.html")


# Test Page for Front End Developer

def test(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES)
    else:
        user = User.objects.get(username=request.user)
        cust = Customer.objects.get(user=request.user)
        form = ProfileEditForm()
    return render(request, 'test.html', {'form': form, 'user': user, 'cust': cust})


# Order Tracking and Archives

def track_order(request):
    cust = Customer.objects.get(user=request.user)
    ordr = Order.objects.filter(customer=cust, is_complete=False)
    track_info = {}
    if ordr:
        # print('\n',ordr.values(),"\n")
        for val in ordr.values():
            track_info['order_id'] = val['orderid']
            track_info['shipped'] = val['is_shipped']
            track_info['delivered'] = val['is_delivered']
            track_info['complete'] = val['is_complete']
            track_info['transaction_id'] = val['transaction_id']
            track_info['customer_id'] = val['customer_id']
            track_info['invoice'] = val['invoice']
            track_info['no_of_items'] = val['no_of_items']
            track_info['order_date'] = val['order_date']
            track_info['shipping_date'] = val['shipping_date']
            track_info['deliever_date'] = val['deliever_date']
            track_info['status'] = val['status']

        print(track_info, '\n')

        if not track_info['complete']:
            return render(request, 'track/trackorder.html', {'track_info':track_info})
    else:
        return render(request, 'track/trackorder.html', {'no_track': True})


def shopping_archive(request):
    return render(request, 'track/prev_ordered_items.html')


