from django import forms
from .models import Seller, Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'password']
        labels = {'name': 'Name', 'email': 'Email'}
        help_text = {'name': 'Enter Your Full Name'}
        error_messages = {'name': {'required': 'Please Enter Your Full Name'},
                          'password': {'required': 'Please Enter Your Password'}}
        widgets = {'password': forms.PasswordInput,
                    'name': forms.TextInput(attrs={'class':'form-field', 'placeholder':'Enter Your Full Name'})}

class SellerForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    class Meta:
        model = Seller
        fields = ['name', 'email', 'phone', 'description', 'address', 'password', 'category', 'subcategory']
        labels = {'name': 'Name', 'email': 'Email'}
