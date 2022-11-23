from dal import autocomplete
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import TextInput, Textarea, HiddenInput, Select
from clients.models import Client, BusinessType, BusinessCategory


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ['creator', 'updator', 'auto_id', 'is_deleted','user','password_reset_otp','earned','paid','balance']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'required email form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'address': Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            
            'business_type': Select(attrs={'class': 'required selectpicker form-control'}),
            'business_category': Select(attrs={'class': 'required selectpicker form-control'}),
            'business_entity_name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Business Entity Name'}),
            'commission_percentage': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Commission Percentage'}),
            
            'contact_person_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact person name'}),
            'contact_person_email': TextInput(attrs={'class': 'form-control email', 'placeholder': 'Contact person email'}),
            'contact_person_phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact person phone'}),

            'account_no': TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'branch_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Name'}),
            'ifsc_code': TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}),
            'iban_no': TextInput(attrs={'class': 'form-control', 'placeholder': 'IBAN No'}),

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
            }
        }


class BusinessTypeForm(forms.ModelForm):

    class Meta:
        model = BusinessType
        exclude = ['creator', 'updator', 'auto_id', 'is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
        }


class BusinessCategoryForm(forms.ModelForm):

    class Meta:
        model = BusinessCategory
        exclude = ['creator', 'updator', 'auto_id', 'is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
        }