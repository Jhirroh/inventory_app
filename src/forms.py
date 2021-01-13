from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

from .models import Order, Product

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'status']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Enter Username...',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Enter Email...',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Enter Password...',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Confirm Password...',
    }))
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', ]

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-user', 
    'id':'exampleInputEmail', 
    'aria-describedby':'emailHelp', 
    'placeholder':'Enter Email Address...'}))

class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 
    'id':'exampleInputPassword', 
    'placeholder':'New Password...'}))
    new_password2 = forms.CharField(error_messages={'required':'The two password fields didn’t match.'}, widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 
    'id':'exampleInputPassword', 
    'placeholder':'Confirm Password...'}))