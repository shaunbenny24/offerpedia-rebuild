from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField
from main.models import BaseModel
from decimal import Decimal


class Client(BaseModel):
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField(blank=True,null=True)
    image = VersatileImageField('Image',upload_to='clients',blank=True,null=True)

    business_entity_name = models.CharField(max_length=128)
    business_type = models.ForeignKey("clients.BusinessType", on_delete=models.CASCADE,blank=True,null=True,limit_choices_to={'is_deleted': False})
    business_category = models.ForeignKey("clients.BusinessCategory", on_delete=models.CASCADE,blank=True,null=True,limit_choices_to={'is_deleted': False})
    commission_percentage = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    contact_person_name = models.CharField(max_length=128,blank=True,null=True)
    contact_person_email = models.EmailField(blank=True,null=True)
    contact_person_phone = models.CharField(max_length=50,blank=True,null=True)

    earned = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    paid = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    is_deleted = models.BooleanField(default=False)

    password_reset_otp = models.PositiveIntegerField(blank=True,null=True)

    account_no = models.CharField(max_length=128,blank=True,null=True)
    branch_name = models.CharField(max_length=128,blank=True,null=True)
    ifsc_code = models.CharField(max_length=128,blank=True,null=True)
    iban_no = models.CharField(max_length=128,blank=True,null=True)

    allow_delivery_agent = models.BooleanField(default=False)

    class Meta:
        db_table = 'clients_client'
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def __unicode__(self):
        return self.name + " - " + self.business_entity_name


class BusinessType(BaseModel):
    name = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'clients_business_type'
        verbose_name = _('business type')
        verbose_name_plural = _('business types')

    def __unicode__(self):
        return self.name


class BusinessCategory(BaseModel):
    name = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'clients_business_category'
        verbose_name = _('business category')
        verbose_name_plural = _('business categories')

    def __unicode__(self):
        return self.name