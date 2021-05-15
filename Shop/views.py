from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm

from .models import Seller, Customer, Product, Order
from .forms import SignUpForm, ProfileEditForm, SellerSignUpForm, SellerProfileEditForm, ProductForm


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about/about.html')


def contact(request):
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

                User.objects.filter(username=request.user).update(first_name=first_name, last_name=last_name, email=email)
                
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

            messages.success(request, 'You are now a member of TheShoppingCArt! Thank you! for chosing us.')

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
                fmd = SellerProfileEditForm(request.POST, request.FILES, instance=user)
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
            form = SellerProfileEditForm()
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
                Product.objects.create(seller=request.user, image=form.cleaned_data['image'],name=form.cleaned_data['name'],brand=form.cleaned_data['brand'],model=form.cleaned_data['model'],year=form.cleaned_data['year'],description=form.cleaned_data['description'],price=form.cleaned_data['price'],in_stock=form.cleaned_data['in_stock'],stock_qty=form.cleaned_data['stock_qty'],reorder_qty=form.cleaned_data['reorder_qty'],is_discount=form.cleaned_data['is_discount'],discount=form.cleaned_data['discount'],category=form.cleaned_data['category'],subcategory=form.cleaned_data['subcategory'],season=form.cleaned_data['season'],type_choice=form.cleaned_data['type_choice'],exp_date=form.cleaned_data['exp_date'], rating=form.cleaned_data['rating'])
                for f in form.cleaned_data.values():
                    print(f)
                messages.success(request, 'Product added successfully.')
        form = ProductForm()
        return render(request, 'product/add_products.html', {'form':form})


# PRODUCT MANAGEMENT FOR EACH CATEGORY

def product(request, id):
    # This function is for view details
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {'product':product})


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


# CART ITEMS
def checkout(request):
    return render(request, 'cart.html')


# Footer Items

def privacy(request):
    return render(request, "policy/privacy.html")



# Test Page for Front End Developer

def test(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES)
    else:
        user = User.objects.get(username=request.user)
        cust = Customer.objects.get(user=request.user)
        form = ProfileEditForm()
    return render(request, 'test.html', {'form': form, 'user': user, 'cust': cust})
