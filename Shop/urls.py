from django.urls import path
from . import views

urlpatterns = [
    # Home urls
    path('', views.home, name='home'),

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
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('careers', views.careers, name='careers'),
    path('payment_help', views.payment_help, name='payment_help'),
    path('ship_info', views.ship_info, name='ship_info'),
    path('return_help', views.return_help, name='return_help'),
    path('return_policy', views.return_policy, name='return_policy'),
    path('faq', views.faq, name='faq'),
    path('tandc', views.tandc, name='tandc'),
    path('security', views.security, name='security'),
    path('error', views.page_not_found, name='error'),

    # Track Order
    path('trackorder', views.track_order, name='trackorder'),
    path('shopping_archive', views.shopping_archive, name='shopping_archive'),

    path('test', views.test, name='test'),
]
