from django import forms
from .models import Customer, Seller
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(
        max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        labels = {'username': 'Username', 'first_name': 'First Name', 'last_name': 'Last Name',
                  'email': 'Email', 'password1': 'Password', 'password2': 'Confirm Password'}


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50, required=True,  label='First Name')
    last_name = forms.CharField(
        max_length=50, label='Last Name', required=False)
    email = forms.EmailField(
        max_length=50, help_text='characters not exceeding 50 chars')
    dob = forms.DateField(required=True, label='DoB',
                          widget=DateInput)
    class Meta:
        model = Customer
        fields = ['image', 'first_name', 'last_name', 'email', 'phone', 'dob', 'residential_address',
            'permanent_address', 'delievery_address']
        labels = {'residential_address': 'Residential Address',
                  'permanent_address': 'Permanent Address', 'delievery_address': 'Delievery Address'}
