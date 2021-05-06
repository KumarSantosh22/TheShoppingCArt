from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('careers', views.careers, name='careers'),
    path('error', views.page_not_found, name='error'),
    # registerion urls
    path('signup', views.signup, name='signup'),
    path('signupseller', views.signup_seller, name='signup_seller'),
    # login urls
    path('Login', views.Login, name='userlogin'),
    path('Logout', views.Logout, name='Logout'),
    # profile
    path('profile', views.profile, name='userprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    # cart
    path('checkout', views.checkout, name='checkout'),

    # test page urls
    path('test', views.test, name='test'),
    path("privacy",views.privacy,name="privacy"),
]
