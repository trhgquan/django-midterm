from cgitb import lookup
from django import forms
import django_filters
from django_filters import DateFilter, CharFilter, ModelChoiceFilter, ChoiceFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    product = ModelChoiceFilter(
        queryset = Product.objects,
        widget = forms.Select(
            attrs = {
                'class' : 'form-control mb-2 mr-sm-2',
            }
        )
    )

    status = ChoiceFilter(
        choices = Order.STATUS,
        widget = forms.Select(
            attrs = {
                'class' : 'form-control mb-2 mr-sm-2',
            }
        )
    )

    start_date = DateFilter(
        field_name = 'date_created',
        lookup_expr = 'gte',
        widget = forms.DateInput(
            attrs = {
                'type' : 'date',
                'class' : 'form-control mb-2 mr-sm-2',
                'placeholder' : 'Select a date'
            }
        ),
        label = 'From date',
    )

    end_date = DateFilter(
        field_name = 'date_created',
        lookup_expr = 'lte',
        widget = forms.DateInput(
            attrs = {
                'type' : 'date',
                'class' : 'form-control mb-2 mr-sm-2',
                'placeholder' : 'Select a date',
            }
        ),
        label = 'To date',
    )

    note = CharFilter(
        field_name = 'note',
        lookup_expr = 'icontains',
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control mb-2 mr-sm-2',
                'placeholder' : 'Keyword for note'
            }
        )
    )

    class Meta:
        model = Order

        # Same as forms.py
        fields = '__all__'
        
        exclude = ['customer', 'date_created']