from dal import autocomplete
from django import forms
from django.forms.widgets import TextInput,Textarea,Select, RadioSelect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from delivery_agents.models import DeliveryAgent


GENDER_CHOICES= (
    ("male", "Male"),
    ("female", "Female"),
)


class DeliveryAgentForm(forms.ModelForm):

    class Meta:
        model = DeliveryAgent
        fields = ['name','phone']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'phone': TextInput(attrs={'class': 'required form-control','placeholder' : 'Phone'}),
        }
        labels = {
            'name' : "Name",  
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required.")
            },
            'phone' : {
                'required' : _("Phone field is required."),
            },
        }