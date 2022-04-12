from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .decorators import admin_only, allowed_users, unauthenticated_user
from .forms import CustomerForm, LoginForm, OrderForm, CreateUserForm
from .filters import OrderFilter
from .models import *

# Create your views here.

@unauthenticated_user
def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            # Get cleaned data
            username = form.cleaned_data.get('username')

            # And create a flash message.
            messages.success(request, 'Account was created for ' + username)
    
            return redirect('login')
        else:
            error_messages = ''.join(message for message in form.error_messages.keys())
            messages.error(request, 'Failed to create new account: ' + error_messages)

    form = CreateUserForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/auth/register.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username or Password is incorrect')

    form = LoginForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/auth/login.html', context)

@login_required(login_url = 'login')
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['customer'])
def user_page(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered_orders = orders.filter(status = 'Delivered').count()
    pending_orders = orders.filter(status = 'Pending').count()

    context = {
        'total_orders' : total_orders,
        'orders' : orders,
        'delivered_orders' : delivered_orders,
        'pending_orders' : pending_orders,
    }

    return render(request, 'accounts/user/user.html', context)

@login_required(login_url = 'login')
def account_page(request):
    customer = request.user.customer    

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance = customer)

        if form.is_valid():
            form.save()

    form = CustomerForm(instance = customer)

    context = {
        'form' : form,
    }

    return render(request, 'accounts/user/account.html', context)

@login_required(login_url = 'login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered_orders = orders.filter(status = 'Delivered').count()
    pending_orders = orders.filter(status = 'Pending').count()

    context = {
        'customers' : customers,
        'orders' : orders,
        'total_customers' : total_customers,
        'total_orders' : total_orders,
        'delivered_orders' : delivered_orders,
        'pending_orders' : pending_orders,
    }

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def products(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'accounts/products.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def customer(request, customer_id):
    customer = Customer.objects.get(id = customer_id)
    orders = customer.order_set.all()
    total_orders = orders.count()

    orders_filter = OrderFilter(request.GET, queryset = orders)
    orders = orders_filter.qs

    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders,
        'orders_filter' : orders_filter,
    }

    return render(request, 'accounts/customer.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def create_order(request, customer_id):
    customer = Customer.objects.get(id = customer_id)

    # Extra = 10 means there are 10 rows each.
    OrderFormSet = inlineformset_factory(
        Customer, Order, 
        fields = (
            'product',
            'status'
        ),
        widgets = {
            'product' : forms.Select(attrs = {
                'class' : 'form-control',
            }),
            'status' : forms.Select(attrs = {
                'class' : 'form-control',
            }),
            'DELETE' : forms.CheckboxInput(attrs = {
                'class' : 'form-check-input',
                'type' : 'checkbox',
            })
        },
        extra = 10
    )

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance = customer)
        
        if formset.is_valid():
            formset.save()
            return redirect('/')

    # With queryset, currently existed items will not appears.
    formset = OrderFormSet(queryset = Order.objects.none(), instance = customer)

    context = {
        'formset' : formset
    }

    return render(request, 'accounts/order/create_order_form.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def update_order(request, order_id):
    order = Order.objects.get(id = order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)
        
        if form.is_valid():
            form.save()
            return redirect('/')

    form = OrderForm(instance = order)

    context = {
        'form' : form,
    }

    return render(request, 'accounts/order/update_order_form.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def delete_order(request, order_id):
    order = Order.objects.get(id = order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item' : order,
    }

    return render(request, 'accounts/order/delete_order_form.html', context)