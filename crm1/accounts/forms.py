from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        
        fields = '__all__'
        # Replace this with required fields, i.e
        # fields = [
        #   'customer', 'id', ..etc
        # ]