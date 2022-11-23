from django import forms
from django.forms.widgets import TextInput, Textarea, Select
from django.utils.translation import gettext_lazy as _
from main.models import Settings


class TextForm(forms.Form):
    name = forms.TextInput()


class SettingsForm(forms.ModelForm):

    class Meta:
        model = Settings
        fields = ['minimum_amount','commission_percentage','bank_transfer_minimum_amount','referal_bonus', 'invitation_code_length','invitation_usage_limit','total_invitation','referral_for_both']
        widgets = {
            'minimum_amount': TextInput(attrs={'class': 'form-control required number','placeholder' : 'Minimum Amount'}),
            'bank_transfer_minimum_amount': TextInput(attrs={'class': 'form-control required number','placeholder' : 'Bank Transfer Minimum Amount'}),
            'commission_percentage': TextInput(attrs={'class': 'form-control required number','placeholder' : 'Commission Percentage'}),
            'referal_bonus': TextInput(attrs={'class': 'form-control required number','placeholder' : 'Referal Bonus'}),
            'invitation_code_length': TextInput(attrs={'class': 'form-control required number','placeholder' : 'Invitation Code Length'}),
            'invitation_usage_limit': TextInput(attrs={'class': 'form-control required number','placeholder' : 'Invitation Usage Limit'}),
            'total_invitation': TextInput(attrs={'class': 'form-control required number','placeholder' : 'Total Invitation'}),
        }

        error_messages = {
            'minimum_amount' : {
                'required' : _("Minimum Amount field is required."),
            },
            'bank_transfer_minimum_amount' : {
                'required' : _("Bank Transfer Minimum Amount field is required."),
            },
            'commission_percentage' : {
                'required' : _("Commission Percentage field is required."),
            },
        }


class FileForm(forms.Form):
    file = forms.FileField()



    