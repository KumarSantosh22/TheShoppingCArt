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
    path('dashboard', views.dashboard, name='dashboard'),

    # Customer urls
    path('signup', views.signup, name='signup'),
    path('Login', views.Login, name='userlogin'),
    path('Logout', views.Logout, name='Logout'),
    path('profile', views.profile, name='userprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),

    # Products
    path('product/<int:id>', views.product, name='product'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('delproduct/<int:id>', views.delproduct, name='delproduct'),

    # Cart and Checkout
    path('updateitem', views.updateitem, name='updateitem'),
    path('cartitem', views.cartitem, name='cartitem'),
    path('checkout', views.checkout, name='checkout'),

    # Payment
    path('payment', views.payment, name='payment'),
    
    # Others
    path("privacy",views.privacy,name="privacy"),
    path('test', views.test, name='test'),
]
