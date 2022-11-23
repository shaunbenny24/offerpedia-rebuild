from django import forms
from django.forms.widgets import TextInput, Textarea, HiddenInput, Select
from contacts.models import Contact, Group
from django.utils.translation import ugettext_lazy as _
from dal import autocomplete


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ['creator', 'updator', 'auto_id', 'is_deleted','user','groups']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'required email form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            
            'country' : autocomplete.ModelSelect2(url='cities:countries_autocomplete',attrs={'data-placeholder': 'Country','data-minimum-input-length': 1}),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'email': {
                'required': _("Email field is required."),
            },
            'phone': {
                'required': _("Phone field is required."),
            },
            'country': {
                'required': _("Country field is required."),
            }
        }
        
        
class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        exclude = ['creator', 'updator', 'auto_id', 'is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            }
        }
        


