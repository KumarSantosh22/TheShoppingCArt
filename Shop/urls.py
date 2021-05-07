from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('careers', views.careers, name='careers'),
    path('error', views.page_not_found, name='error'),

    # Seller urls
    path('seller', views.seller, name='seller'),
    path('signupseller', views.signupseller, name='signupseller'),
    path('sellerprofile', views.sellerprofile, name='sellerprofile'),
    path('updateseller', views.updateseller, name='updateseller'),

    # Customer urls
    path('signup', views.signup, name='signup'),
    path('Login', views.Login, name='userlogin'),
    path('Logout', views.Logout, name='Logout'),
    path('profile', views.profile, name='userprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),

    # Products
    path('checkout', views.checkout, name='checkout'),

    # Others
    path("privacy",views.privacy,name="privacy"),
    path('test', views.test, name='test'),
]
