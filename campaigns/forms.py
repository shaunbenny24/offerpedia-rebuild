from django import forms
from django.forms.widgets import TextInput, Textarea, HiddenInput, Select, NumberInput
from campaigns.models import Campaign, PromoCode, EmailTemplate, Booking, CampaignRegion, CampaignCashbackPromocode, CampaignType, CampaignContent,\
    CampaignGallery, CampaignPricing, Invoice, Receipt, CampaignAccessibleRegion, CampaignViewCashbackClaim, CampaignBillAmountCashbackClaim,\
    CampaignBillAmountCashbackCode, BillAmountCashbackPricing, CampaignEnquiry, InvoiceMail, CampaignVoucherPromocode,\
    CampaignViewVoucherClaim
from django.utils.translation import ugettext_lazy as _
from dal import autocomplete


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        exclude = [
            'creator',
            'updator',
            'auto_id',
            'is_deleted',
            'total_bookings',
            'is_published',
            'balance',
            'active_clicks',
            'dead_clicks',
            'balance',

            'cashback_amount_used',
            'cashback_amount_balance',
            'cashback_amount_refunded',

            'cashback_amount_voucher_used',
            'cashback_amount_voucher_refunded',
            'cashback_amount_voucher_balance',

            'bill_amount_used_amount',
            'bill_amount_balance_amount',
            'bill_amount_refunded_amount',
            'bill_amount_bonus_amount',
            'bill_amount_net_amount',
            'bill_amount_collected_amount',

            'need_promo_code',
            'number_of_promo_codes',
            'promocode_length',
            'expiry_date',
            'discount_percentage',
            'discount_description'
        ]

        widgets = {
            'client' : autocomplete.ModelSelect2(url='clients:clients_autocomplete',attrs={'data-placeholder': 'Client','data-minimum-input-length': 1}),
            'title': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Title'}),
            'from_date': TextInput(attrs={'class': 'required date-picker form-control', 'placeholder': 'From date'}),
            'to_date': TextInput(attrs={'class': 'required date-picker form-control', 'placeholder': 'To date'}),
            'description': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Description'}),
            'public_description': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Description'}),
            'campaign_type': Select(attrs={'class': 'required form-control selectpicker'}),

            'delivery_charge': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Delivery Charge'}),

            'number_of_cashback_promo': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Number of cashback promo'}),
            'cashback_highlights': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Cashback Highlights, Comma separated'}),
            'cashback_amount_from_client' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount from client'}),
            'cashback_amount_to_user' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount to user'}),
            'cashback_amount_to_referrer' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount to referrer'}),
            'cashback_amount_collected' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount collected'}),

            'bill_amount_highlights': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Cashback Highlights, Comma separated'}),
            'bill_amount_percentage' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Cashback Percentage Percentage'}),
            'bill_amount_percentage_to_user' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Percentage to user'}),
            'bill_amount_percentage_to_referrer' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Percentage to referrer'}),
            'bill_amount_cashback_pricing': Select(attrs={'class': 'form-control selectpicker'}),

            'pricing': Select(attrs={'class': 'form-control selectpicker'}),
            'status': Select(attrs={'class': 'required form-control selectpicker'}),
            'number_of_promo_codes': TextInput(attrs={'class': 'form-control', 'placeholder': 'No of promo codes'}),
            'position': TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'expiry_date': TextInput(attrs={'class': 'date-picker form-control', 'placeholder': 'Expiry Date'}),
            'discount_percentage': TextInput(attrs={'class': 'form-control number', 'placeholder': 'Discount Percentage'}),
            'discount_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount Description'}),
            'promocode_length' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Promocode Length'}),

            'user_click_limit' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'User Click Limit'}),

            'youtube_video_id': TextInput(attrs={'class': 'form-control', 'placeholder': 'Youtube video id'}),

            'number_of_cashback_voucher_promo': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Number of cashback promo'}),
            'cashback_voucher_highlights': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Cashback Highlights, Comma separated'}),
            'cashback_amount_voucher_from_client' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount from client'}),
            'cashback_amount_voucher_to_user' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount to user'}),
            'cashback_amount_voucher_to_referrer' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount to referrer'}),
            'cashback_amount_voucher_collected' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Amount collected'}),

            'latitude' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Latitude'}),
            'longitude' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Longitude'}),
            'contact_phone' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Phone'}),
            'contact_email' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Email'}),
            'contact_address' : TextInput(attrs={'class': 'form-control number', 'placeholder': 'Address'}),
            'contact_website' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'customizable_button_link' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Customizable Button Link'}),
            'customizable_button_text' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Customizable Button Text'}),

            'user_benifit': TextInput(attrs={'class': 'required form-control', 'placeholder': 'User Benifit'}),
            'referrer_benifit': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Referrer Benifit'}),

            'sharable_content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Sharable Content'}),
            'enquiry_button_text' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Enquiry Button Text'}),

        }
        error_messages = {
            'title': {
                'required': _("Title field is required."),
            },
            'from_date': {
                'required': _("From date field is required."),
            },
            'to_date': {
                'required': _("To date field is required."),
            },
            'description': {
                'required': _("Description field is required."),
            },
            'pricing': {
                'required': _("Pricing field is required."),
            },
            'status': {
                'required': _("Status field is required."),
            },
            'campaign_type' : {
                'required' : _("Campaign Type field is required."),
            },

        }
        labels = {
            "discount_percentage" : "Promocode Discount Percentage",
            "discount_description" : "Promocode Discount Description",
        }


class CampaignRegionForm(forms.ModelForm):

    class Meta:
        model = CampaignRegion
        exclude = ['campaign']
        widgets = {
            'country' : autocomplete.ModelSelect2(url='cities:countries_autocomplete',attrs={'data-placeholder': 'Country','data-minimum-input-length': 1}),
            'state' : autocomplete.ModelSelect2(url='cities:states_autocomplete',forward=['country'],attrs={'data-placeholder': 'State','data-minimum-input-length': 1}),
            'city' : autocomplete.ModelSelect2(url='cities:cities_autocomplete',forward=['state'],attrs={'data-placeholder': 'City','data-minimum-input-length': 1}),
        }
        error_messages = {
            'country' : {
                'required' : _("Country field is required."),
            },
        }


class CampaignAccessibleRegionForm(forms.ModelForm):

    class Meta:
        model = CampaignAccessibleRegion
        exclude = ['campaign']
        widgets = {
            'country' : autocomplete.ModelSelect2(url='cities:countries_autocomplete',attrs={'data-placeholder': 'Country','data-minimum-input-length': 1}),
            'state' : autocomplete.ModelSelect2(url='cities:states_autocomplete',forward=['country'],attrs={'data-placeholder': 'State','data-minimum-input-length': 1}),
            'city' : autocomplete.ModelSelect2(url='cities:cities_autocomplete',forward=['state'],attrs={'data-placeholder': 'City','data-minimum-input-length': 1}),
        }
        error_messages = {
            'country' : {
                'required' : _("Country field is required."),
            },
        }


class CampaignVoucherPromocodeForm(forms.ModelForm):

    class Meta:
        model = CampaignVoucherPromocode
        exclude = ['creator','updator','auto_id','is_deleted','campaign']
        widgets = {
            'voucher_code': TextInput(attrs={'class': 'required form-control qty','placeholder' : 'Voucher Code'}),
        }


class PromoCodeForm(forms.ModelForm):

    class Meta:
        model = PromoCode
        exclude = ['creator','updator','auto_id','is_deleted','campaign','total_used']
        widgets = {
            'code': TextInput(attrs={'class': 'required form-control qty','placeholder' : 'Code'}),
            'expiry_date': TextInput(attrs={'class': 'required datepickerold form-control','placeholder' : 'Expiry Date'}),
            'discount_percentage': TextInput(attrs={'class': 'required form-control number', 'placeholder': 'Discount Percentage'}),
            'discount_description': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Discount Description'}),
        }
        error_messages = {
            'code' : {
                'required' : _("Code field is required."),
            },
            'expiry_date' : {
                'required' : _("Expiry date field is required."),
            },
            'discount_percentage' : {
                'required' : _("Discount percentage field is required."),
            },
            'discount_description' : {
                'required' : _("Discount description field is required."),
            }
        }


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude = ['creator','updator','auto_id','is_deleted','campaign','amount','paid','balance','bill_amount','billing_percentage','invoice_no','billing_amount','payment_amount']
        widgets = {
            'invoice_date': TextInput(attrs={'class': 'required date-picker form-control','placeholder' : 'Invoice Date'}),
            'due_date': TextInput(attrs={'class': 'required date-picker form-control','placeholder' : 'Due Date'}),
            'from_date': TextInput(attrs={'class': 'required date-picker form-control', 'placeholder': 'From date'}),
            'to_date': TextInput(attrs={'class': 'required date-picker form-control','placeholder' : 'To Date'}),

        }
        error_messages = {
            'invoice_date' : {
                'required' : _("Invoice Date field is required."),
            },
            'due_date' : {
                'required' : _("Due Date field is required."),
            },
            'from_date' : {
                'required' : _("From Date field is required."),
            },
            'to_date' : {
                'required' : _("To Date field is required."),
            },
            'invoice_no' : {
                'required' : _("Invoice Number field is required."),
            },
        }


class ReceiptForm(forms.ModelForm):

    class Meta:
        model = Receipt
        exclude = ['creator','updator','auto_id','is_deleted','invoice','balance']
        widgets = {
            'date': TextInput(attrs={'class': 'required datepicker form-control','placeholder' : 'Date'}),
            'paid': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Amount paid'}),
        }
        error_messages = {
            'date' : {
                'required' : _("Date field is required."),
            },
            'paid' : {
                'required' : _("Paid field is required."),
            },
        }


class EmailSaleForm(forms.Form):
    email = forms.EmailField(widget=TextInput(attrs={'class': 'required form-control email','placeholder' : 'Email'}))
    name = forms.CharField(widget=TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}))
    content = forms.CharField(
        help_text="Link will be added automatically. You do not need to insert manually.",
        widget=Textarea(attrs={
             'class': 'form-control',
             'placeholder' : 'Content'
            }
        )
    )


class CampaignContentForm(forms.ModelForm):

    class Meta:
        model = CampaignContent
        exclude = ['is_deleted','campaign']
        widgets = {
            'title': TextInput(attrs={'class': 'required form-control qty','placeholder' : 'Title'}),
            'description': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Description'}),
        }
        error_messages = {
            'title' : {
                'required' : _("Title field is required."),
            },
            'description' : {
                'required' : _("Description field is required."),
            }
        }


class CampaignPricingForm(forms.ModelForm):

    class Meta:
        model = CampaignPricing
        exclude = ['creator','updator','auto_id','is_deleted','campaign']
        widgets = {
            'amount': TextInput(attrs={'class': 'required form-control number','placeholder' : 'Amount'}),
            'no_of_clicks': TextInput(attrs={'class': 'required form-control number', 'placeholder': 'Number of clicks'}),
            'campaign_type': Select(attrs={'class': 'required form-control selectpicker'}),
        }
        error_messages = {
            'amount' : {
                'required' : _("Amount field is required."),
            },
            'no_of_clicks' : {
                'required' : _("Number of clicks field is required."),
            },
            'campaign_type' : {
                'required' : _("Campaign type field is required."),
            }
        }


class BillAmountCashbackPricingForm(forms.ModelForm):

    class Meta:
        model = BillAmountCashbackPricing
        exclude = ['creator','updator','auto_id','is_deleted','campaign']
        widgets = {
            'amount': TextInput(attrs={'class': 'required form-control number','placeholder' : 'Amount'}),
            'percentage': TextInput(attrs={'class': 'required form-control number','placeholder' : 'Percentage'}),
            'percentage_to_user' : TextInput(attrs={'class': 'required form-control number','placeholder' : 'Percentage to user'}),
            'percentage_to_referrer': TextInput(attrs={'class': 'required form-control number','placeholder' : 'Percentage to referrer'}),
            'bonus_percentage': TextInput(attrs={'class': 'required form-control number','placeholder' : 'Bonus Percentage'})
        }
        error_messages = {
            'amount' : {
                'required' : _("Amount field is required."),
            },
            'percentage' : {
                'required' : _("Percentage field is required."),
            },
            'percentage_to_user' : {
                'required' : _("Percentage to user field is required."),
            },
            'percentage_to_referrer' : {
                'required' : _("Percentage to referrer field is required."),
            }
        }


class CampaignGalleryForm(forms.ModelForm):

    class Meta:
        model = CampaignGallery
        exclude = ['is_deleted','campaign']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control','placeholder' : 'Title'}),
        }
        error_messages = {
            'image' : {
                'required' : _("Image field is required."),
            }
        }


class RechargeForm(forms.ModelForm):

    class Meta:
        model = Campaign
        exclude = [
            'client',
            'creator',
            'updator',
            'auto_id',
            'is_deleted',
            'total_bookings',
            'is_published',
            'balance',
            'active_clicks',
            'dead_clicks',
            'balance',
            'title',
            'description',
            'public_description',
            'campaign',
            'from_date',
            'to_date',
            'pricing',
            'sharable_content',
            'campaign_type',
            'number_of_cashback_promo',
            'cashback_amount_to_user',
            'cashback_amount_from_client',
            'user_click_limit',
            'cashback_amount_to_referrer',
            'status',
            'cashback_amount_collected',

            'cashback_amount_used',
            'cashback_amount_balance',
            'cashback_amount_refunded',

            'bill_amount_used_amount',
            'bill_amount_balance_amount',
            'bill_amount_refunded_amount',
            'bill_amount_bonus_amount',
            'bill_amount_net_amount',
            'bill_amount_collected_amount',

            'need_promo_code',
            'number_of_promo_codes',
            'promocode_length',
            'expiry_date',
            'discount_percentage',
            'discount_description'
        ]

        widgets = {
            'bill_amount_cashback_pricing': Select(attrs={'class': 'form-control','placeholder' : 'Select cashback'}),
        }
        error_messages = {
            'bill_amount_cashback_pricing' : {
                'required' : _("Cashback price  field is required."),
            }
        }


class EmailTemplateForm(forms.ModelForm):

    class Meta:
        model = EmailTemplate
        exclude = ['creator','updator','auto_id','is_deleted','campaign','design']
        widgets = {
            'content1': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content2': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content3': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content4': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content5': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content6': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content7': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content8': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content9': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content10': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content11': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content12': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content13': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content14': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),
            'content15': Textarea(attrs={'class': 'form-control','placeholder' : 'Content'}),

        }


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        exclude = ['creator','updator','auto_id','is_deleted','campaign','email_template', 'contact','status','promo_code']
        widgets = {
            'from_date': TextInput(attrs={'class': 'required form-control date-picker','placeholder' : 'From date'}),
            'to_date': TextInput(attrs={'class': 'required date-picker form-control','placeholder' : 'To Date'}),
            'seats': TextInput(attrs={'class': 'required form-control number','placeholder' : 'Seats'}),
            'amount': TextInput(attrs={'class': 'required form-control number','placeholder' : 'Amount'}),

            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'email': TextInput(attrs={'class': 'required form-control email','placeholder' : 'Email'}),
            'phone': TextInput(attrs={'class': 'required form-control','placeholder' : 'Phone'}),
            'address': TextInput(attrs={'class': 'form-control','placeholder' : 'Address'}),
        }
        error_messages = {
            'from_date' : {
                'required' : _("From date field is required."),
            },
            'to_date' : {
                'required' : _("To date field is required."),
            },
            'seats' : {
                'required' : _("Seats field is required."),
            },
            'amount' : {
                'required' : _("Amount field is required."),
            },

        }


class CampaignTypeForm(forms.ModelForm):

    class Meta:
        model = CampaignType
        exclude = ['creator','updator','auto_id','is_deleted','date_added','date_updated','theme','a_id']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'description': Textarea(attrs={'class': 'required form-control','placeholder' : 'Description'}),
            'amount_to_user': TextInput(attrs={'class': 'required  number form-control'}),
            'amount_from_client': TextInput(attrs={'class': 'required number form-control'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            'description' : {
                'required' : _("Description field is required."),
            },
            'amount_to_user' : {
                'required' : _("Amount To User field is required."),
            },
            'amount_from_client' : {
                'required' : _("Amount From Client field is required."),
            },
        }


class CampaignViewCashbackClaimForm(forms.ModelForm):

    class Meta:
        model = CampaignViewCashbackClaim
        exclude = ['campaign_view','is_deleted','country']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Enter your name'}),
            'phone': NumberInput(attrs={'class': 'required datepickerold form-control','placeholder' : 'Enter your 8 digit phone number','maxlength':'10'}),
            'cashback_code': NumberInput(attrs={'class': 'required form-control number', 'placeholder': 'Avail cashback code at the retail outlet','maxlength':'6'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            'phone' : {
                'required' : _("Phone field is required."),
            },
            'cashback_code' : {
                'required' : _("Cashback code field is required."),
            }
        }


class CampaignCashbackPromocodeForm(forms.ModelForm):

    class Meta:
        model = CampaignCashbackPromocode
        exclude = ['campaign','is_deleted','cashback_code','campaign_view']
        widgets = {
            'promocode': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Enter promocode','maxlength':'6'}),
        }
        error_messages = {
            'promocode' : {
                'required' : _("Promocode field is required."),
            }
        }


class CampaignBillAmountCashbackClaimForm(forms.ModelForm):

    class Meta:
        model = CampaignBillAmountCashbackClaim
        exclude = ['campaign_view','is_deleted','country','cashback_code']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Enter your name'}),
            'phone': NumberInput(attrs={'class': 'required datepickerold form-control','placeholder' : 'Enter your 8 digit phone number','maxlength':'10'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            'phone' : {
                'required' : _("Phone field is required."),
            }
        }


class CampaignVoucherClaimForm(forms.ModelForm):

    class Meta:
        model = CampaignViewVoucherClaim
        exclude = ['campaign_view','is_deleted','country']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Enter your name'}),
            'phone': NumberInput(attrs={'class': 'required datepickerold form-control','placeholder' : 'Enter your 8 digit phone number','maxlength':'10'}),
            'voucher_code': NumberInput(attrs={'class': 'required form-control number', 'placeholder': 'Avail cashback code at the retail outlet','maxlength':'6'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            'phone' : {
                'required' : _("Phone field is required."),
            },
            'voucher_code' : {
                'required' : _("Voucher code field is required."),
            }
        }



class CampaignBillAmountCashbackCodeForm(forms.ModelForm):

    class Meta:
        model = CampaignBillAmountCashbackCode
        exclude = ['campaign','is_deleted']
        widgets = {
            'bill_amount': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Enter Bill Amount'}),
            'receipt_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Receipt Number'}),
            'cashback_code': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Customer Code'}),
        }
        error_messages = {
            'bill_amount' : {
                'required' : _("Bill Amount field is required."),
            },
            'cashback_code' : {
                'required' : _("Customer Code field is required."),
            }
        }
        labels = {
            "receipt_number" : "Receipt Number(Optional)",
            "cashback_code" : "Customer Code",
        }


class CampaignEnquiryForm(forms.ModelForm):

    class Meta:
        model = CampaignEnquiry
        fields = ['name', 'phone', 'email']
        widgets = {
            'name':  TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'phone':  TextInput(attrs={'class': 'required form-control','placeholder' : 'Phone'}),
            'email':  TextInput(attrs={'class': 'required form-control','placeholder' : 'Email'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            'phone' : {
                'required' : _("Phone field is required."),
            }
        }
