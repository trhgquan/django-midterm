from django.shortcuts import render
from django.http import HttpResponse

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

    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders,
    }

    return render(request, 'accounts/customer.html', context)