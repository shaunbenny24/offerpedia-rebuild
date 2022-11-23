from dal import autocomplete
from django import forms
from django.forms.widgets import TextInput,Textarea,Select
from django.utils.translation import ugettext_lazy as _
from orders.models import Order, OrderItem


class OrderStatusForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['order_status']
        widgets = {
            'order_status': Select(attrs={'class': 'required form-control'}),
        }
        error_messages = {
            'order_status' : {
                'required' : _("Order status field is required."),
            },
        }


class OrderCancelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['cancel_reason']
        widgets = {
            'cancel_reason': TextInput(attrs={'class': 'required form-control','placeholder' : 'Reason'}),
        }
        error_messages = {
            'cancel_reason' : {
                'required' : _("Reason field is required."),
            },
        }


class CancelStatusForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['cancel_status']
        widgets = {
            'cancel_status': Select(attrs={'class': 'required form-control'}),
        }
        error_messages = {
            'cancel_status' : {
                'required' : _("Order status field is required."),
            },
        }


class DeliveragentForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['delivery_agent']
        widgets = {
            'delivery_agent': Select(attrs={'class': 'required form-control'}),
        }
        error_messages = {
            'delivery_agent' : {
                'required' : _("Delivery Agent status field is required."),
            },
        }


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['product','varient','qty','price']
        widgets = {
            'product': Select(attrs={'class': 'required form-control'}),
            'varient': TextInput(attrs={'class': 'form-control readonly','placeholder' : 'Variant'}),
            'qty': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Quantity'}),
            'price': TextInput(attrs={'class': 'number form-control','placeholder' : 'Price'}),
        }
