from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('careers', views.careers, name='careers'),
    path('error', views.page_not_found, name='error'),
    # registerion urls
    path('signupuser', views.signup_user, name='signup_user'),
    path('signupcustomer', views.signup_customer, name='signup_customer'),
    path('signupseller', views.signup_seller, name='signup_seller'),
    # login urls
    path('login', views.login, name='login'),
    # cart
    path('checkout', views.checkout, name='checkout'),

    # test page urls
    path('test', views.test_page, name='test'),
    path('privacy',views.privacy,name='privacy'),
]
