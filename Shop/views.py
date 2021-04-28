from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import datetime
from django.contrib.auth.models import User

from .models import Seller, Customer
from .forms import CustomerForm, SellerForm


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

def login(request):
    return render(request, 'login.html')


def signup_user(request):
    return HttpResponse("user")


def signup_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            customer = Customer(name=name, email=email,
                                phone=phone, address=address, password=password)
            customer.save()
            return redirect('home')

    return render(request, 'signup_customer.html', {'form': form})


def signup_seller(request):
    return HttpResponse("Sller")


def logout(request):
    pass


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



# Test Page for Front End Developer

def test_page(request):
    return render(request, 'about/careers.html')
 