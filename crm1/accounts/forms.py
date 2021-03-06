from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import Customer, Order

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = [
            'user',
        ]

        widgets = {
            'name' : forms.TextInput(attrs = {
                'class' : 'form-control'
            }),
            'phone' : forms.TextInput(attrs = {
                'class' : 'form-control',
            }),
            'email' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'type' : 'email',
            }),
        }

class OrderForm(ModelForm):
    '''Form to create orders
    '''
    class Meta:
        model = Order
        
        fields = '__all__'
        # Replace this with required fields, i.e
        # fields = [
        #   'customer', 'id', ..etc
        # ]

        widgets = {
            'customer' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                },
            ),
            'product' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                },
            ),
            'status' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                },
            ),
            'note' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'rows' : '3',
                },
            )
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your username'
        }
    ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your password'
        }
    ))

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

class CreateUserForm(UserCreationForm):
    '''Form to create Users
    '''

    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your username goes here'
        }
    ))

    email = forms.CharField(widget = forms.EmailInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your email goes here'
        }
    ))

    password1 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your password goes here'
        }
    ), label = 'Your password')

    password2 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Confirm your password again'
        }
    ), label = 'Confirm your password')

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]