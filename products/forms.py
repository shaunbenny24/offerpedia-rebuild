from django import forms
from django.forms.widgets import TextInput,Textarea,Select,DateInput, CheckboxInput
from django.contrib.auth.models import User
from products.models import Product, ProductCategory, ProductImage, ProductSubCategory, ProductVarient
from dal import autocomplete, forward
from django.utils.translation import ugettext_lazy as _
# from ckeditor.widgets import CKEditorWidget


class ProductCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        exclude = ['creator','updator','auto_id','is_deleted','a_id','client']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'description': Textarea(attrs={'class': 'form-control','placeholder' : 'Description'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            
        }


class ProductVarientForm(forms.ModelForm):

    class Meta:
        model = ProductVarient
        fields = ['varient_name']
        widgets = {
            'varient_name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Varient Name'}),
        }
        error_messages = {
            'varient_name' : {
                'required' : _("Varient Name field is required."),
            },
            
        }


class ProductSubCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductSubCategory
        exclude = ['auto_id','is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'category' : autocomplete.ModelSelect2(url='products:category_autocomplete',
                attrs={'data-placeholder': 'Category','data-minimum-input-length': 1}),

        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['creator','updator','auto_id','is_deleted','discount','a_id','first_time_stock','campaign','meta_keywords']
        widgets = {
            'name' : TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'description' : Textarea(attrs={'class': 'form-control','placeholder' : 'Description'}),
            'price': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Price'}),
            'mrp': TextInput(attrs={'class': 'number required form-control','placeholder' : 'MRP'}),
            'stock': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Stock'}),
            'cost': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Cost'}),
            'tax': TextInput(attrs={'class': 'number required form-control','placeholder' : 'Tax'}),
            'youtube_video' : TextInput(attrs={'class': 'form-control','placeholder' : 'Youtube Video Id'}),
            'varients' : autocomplete.ModelSelect2Multiple(
                    url='products:varient_autocomplete',
                    attrs={'class': 'form-control','data-placeholder': 'Varients','data-minimum-input-length': 1}
            ),
            'category' : autocomplete.ModelSelect2(url='products:category_autocomplete',
                attrs={'class': 'required form-control','data-placeholder': 'Category','data-minimum-input-length': 1}),
            'sub_category' : autocomplete.ModelSelect2(url='products:sub_category_autocomplete', forward= ["category"], 
                attrs={'class': 'form-control','data-placeholder': 'Sub Category','data-minimum-input-length': 1,'data-autocomplete-light-forward':'category'}),
            'meta_description': Textarea(attrs={'class': 'form-control','placeholder' : 'Meta Description'}), 
            'low_stock_limit':TextInput(attrs={'class': 'number required form-control','placeholder' : 'Stock limit'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            'mrp' : {
                'required' : _("MRP field is required."),
            },
            'stock' : {
                'required' : _("Stock field is required."),
            },
            'category' : {
                'required' : _("Category field is required."),
            },
            'tax' : {
                'required' : _("Tax field is required."),
            },
            'cost' : {
                'required' : _("Cost field is required."),
            },
            'price' : {
                'required' : _("Price field is required."),
            },


        }
        labels = {
            'featured_image' : "Featured image"
        }


class ProductImageForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        exclude = ['creator','updator','auto_id','is_deleted','product']
        error_messages = {
            'image' : {
                'required' : _("Image field is required."),
            },
        }


# class VarientForm(forms.ModelForm):
        # varients = ModelMultipleChoiceField(
    #     required=False,
    #     queryset=ProductVarient.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(
    #         url='products:varient_autocomplete',
    #         forward=("varients", ),
    #         attrs={'class': 'form-control','data-placeholder': 'Varients','data-minimum-input-length': 1}
    #     )
    # )
#     class Meta:
#         model = ProductVarient
#         fields = ['varient_name']
#         widgets = {
#             'varient_name' : autocomplete.ModelSelect2(url='products:varient_autocomplete',
#                 attrs={'class': 'form-control','data-placeholder': 'Varient','data-minimum-input-length': 1}),
#         }


    # varient = forms.ModelMultipleChoiceField(
    #     queryset=ProductVarient.objects.all(),
    #     widget=autocomplete.ModelSelect2(
    #         url='products:varient_autocomplete',
    #         forward=("varients", ),
    #         attrs={'class': 'form-control','data-placeholder': 'Varient','data-minimum-input-length': 1}
    #     )
    # )