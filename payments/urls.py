from django.urls import path
from . import views

urlpatterns = [
    path('razorpay', views.razorpay, name='razorpay'),
    path('razorpay_handler', views.razorpay_handler, name='razorpay_handler'),
    path('testpay', views.testpay, name='testpay'),
]
