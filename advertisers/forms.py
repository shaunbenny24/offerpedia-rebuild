#Third Party
from dal import autocomplete
#Django
from django import forms
from django.forms.widgets import TextInput, Textarea, HiddenInput, Select
from django.utils.translation import ugettext_lazy as _
#Local libraries
from advertisers.models import Advertiser, DealerRequest, AppUserAddress, AppUser


class AdvertiserForm(forms.ModelForm):

    class Meta:
        model = Advertiser
        exclude = ['creator', 'updator', 'auto_id', 'is_deleted','user','email','earned','paid','balance']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'address': Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),

            'account_no': TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'branch_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Name'}),
            'ifsc_code': TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}),
            'iban_no': TextInput(attrs={'class': 'form-control', 'placeholder': 'IBAN No'}),
        }
        
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'phone': {
                'required': _("Phone field is required."),
            }
        }


class DealerRequestForm(forms.ModelForm):
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'required form-control', 'placeholder': 'Password'}),
    )

    class Meta:
        model = DealerRequest
        fields = ['name','password','phone','email']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'email': TextInput(attrs={'class': 'email form-control', 'placeholder': 'Email'}),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'password': {
                'required': _("Password field is required."),
            },
            'phone': {
                'required': _("Phone field is required."),
            }
        }


class AppUserAddressForm(forms.ModelForm):

    class Meta:
        model = AppUserAddress
        fields = ['road_number','block_number','building_number', 'additional_directions','name','villa_or_flat_no']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder' : 'Name'}),
            'road_number': TextInput(attrs={'class': 'required form-control','placeholder' : 'Road Number'}),
            'block_number': TextInput(attrs={'class': 'required form-control','placeholder' : 'Block Number'}),
            'building_number' : TextInput(attrs={'class': 'form-control','placeholder' : 'Building Number'}),
            'villa_or_flat_no' : TextInput(attrs={'class': 'form-control','placeholder' : 'Villa/Flat No:'}),
            'additional_directions' : TextInput(attrs={'class': 'form-control','placeholder' : 'Area/Additional Directions'}),
        }
        error_messages = {
            'road_number' : {
                'required' : _("Road Number field is required."),
            },
            'block_number' : {
                'required' : _("Block Number field is required."),
            }
        }


class AppUserForm(forms.ModelForm):
    
    class Meta:
        model = AppUser
        fields = ['earned','paid','cashbacks','balance','address']
        widgets = {
            'earned': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Earned'}),
            'paid': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Paid'}),
            'cashbacks': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Cashabcks'}),
            'balance': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Balance'}),
            'address': Textarea(attrs={'class': 'form-control','placeholder' : 'Address'}),
        }