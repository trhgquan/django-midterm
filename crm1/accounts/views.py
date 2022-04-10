from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .forms import OrderForm
from .filters import OrderFilter
from .models import *

# Create your views here.
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

def products(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'accounts/products.html', context)

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

def create_order(request, customer_id):
    customer = Customer.objects.get(id = customer_id)

    # Extra = 10 means there are 10 rows each.
    OrderFormSet = inlineformset_factory(Customer, Order, fields = (
        'product',
        'status'
    ), extra = 10)

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

    return render(request, 'accounts/order_form.html', context)

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

    return render(request, 'accounts/update_order_form.html', context)

def delete_order(request, order_id):
    order = Order.objects.get(id = order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item' : order,
    }

    return render(request, 'accounts/delete.html', context)