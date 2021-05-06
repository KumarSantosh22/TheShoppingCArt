from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Seller, Customer
from .forms import SignUpForm, ProfileEditForm, SellerSignUpForm


def home(request):
    return render(request, 'index.html')


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
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            request.session['username'] = username
            print('*********USER DATA : ', user)
            seller = Seller(user=user)
            seller.save()
            return redirect('home')
    else:
        form = SellerSignUpForm()
    return render(request, 'signup_seller.html', {'form': form})


# PRODUCT MANAGEMENT FOR EACH CATEGORY

def products(request):
    return HttpResponse("products")


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


# Anish tiwari

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
