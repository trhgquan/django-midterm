from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    '''Customer model
    '''

    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default = 'quan.jpg', null = True, blank = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        if self.name is not None:
            return self.name
        return self.user.username

class Tag(models.Model):
    '''Tag model
    '''

    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    '''Product model
    '''

    CATEGORIES = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )

    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200, choices = CATEGORIES, null = True)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name

class Order(models.Model):
    '''Order model
    '''

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
    status = models.CharField(max_length = 200, choices = STATUS, null = True)
    note = models.CharField(max_length = 1000, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.product.name