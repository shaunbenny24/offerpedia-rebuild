from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel
from decimal import Decimal
from versatileimagefield.fields import VersatileImageField
import uuid


class Advertiser(BaseModel):
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50,unique=True)
    address = models.TextField(blank=True,null=True)

    earned = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    paid = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    account_no = models.CharField(max_length=128,blank=True,null=True)
    branch_name = models.CharField(max_length=128,blank=True,null=True)
    ifsc_code = models.CharField(max_length=128,blank=True,null=True)
    iban_no = models.CharField(max_length=128,blank=True,null=True)
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'advertisers_advertiser'
        verbose_name = _('advertiser')
        verbose_name_plural = _('advertisers')

    def __unicode__(self):
        return self.name


class DealerRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length=128)

    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'advertisers_dealer_request'
        verbose_name = _('dealer-request')
        verbose_name_plural = _('dealer-requests')

    def __unicode__(self):
        return self.name


class AppUser(BaseModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    firstname = models.CharField(max_length=128,blank=True,null=True)
    lastname = models.CharField(max_length=128,blank=True,null=True)
    email = models.EmailField(null=True,blank=True) 
    phone = models.CharField(max_length=128)
    address = models.TextField(null=True,blank=True)
    otp_number = models.PositiveIntegerField()

    country = models.ForeignKey('cities.Country', on_delete=models.CASCADE,blank=True,null=True)
    state = models.ForeignKey('cities.State', on_delete=models.CASCADE,blank=True,null=True)
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE,blank=True,null=True,limit_choices_to={'is_district': True})

    earned = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    paid = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    transferred = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    shopping = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    gifts = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashbacks = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bank_transfer = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    invitation_code = models.CharField(max_length=128,blank=True,null=True)
    invitation_used = models.PositiveIntegerField(default=0)
    promocode = models.CharField(max_length=128,blank=True,null=True)
    referals = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    is_deleted = models.BooleanField(default=False)

    def name(self):
        name = ""
        if self.firstname:
            name = self.firstname
        if self.lastname:
            name += " " + self.lastname
        if not self.firstname and not self.lastname:
            name = self.phone

        return name

    class Meta:
        db_table = 'app_user'
        verbose_name = _('App User')
        verbose_name_plural = _('App Users')
        ordering = ('firstname',)
  
    def __unicode__(self): 
        return self.name()


class AppUserAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    app_user = models.ForeignKey("advertisers.AppUser",on_delete=models.CASCADE)

    name = models.CharField(max_length=128,blank=True,null=True)
    road_number = models.CharField(max_length=128,blank=True,null=True)
    block_number = models.CharField(max_length=128,blank=True,null=True)
    building_number = models.CharField(max_length=128,blank=True,null=True)
    villa_or_flat_no = models.CharField(max_length=128,blank=True,null=True)
    zip_code = models.CharField(max_length=128,blank=True,null=True)
    additional_directions = models.CharField(max_length=128,blank=True,null=True)

    is_active = models.BooleanField(default=False)

    is_deleted= models.BooleanField(default=False)

    class Meta:
        db_table = 'app_user_address'
        verbose_name = _('App User Address')
        verbose_name_plural = _('App Users Address')
        ordering = ('-id',)

    def __str__(self):
        return str(self.road_number)


class AppUserInvite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invitation_code = models.CharField(max_length=128)
    referrer = models.ForeignKey('advertisers.AppUser', on_delete=models.CASCADE)
    target_device_platform = models.CharField(max_length=128)
    target_device_version = models.CharField(max_length=128)
    target_device_ip = models.CharField(max_length=128)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'advertisers_app_user_invite'
        verbose_name = _('advertiser invite')
        verbose_name_plural = _('advertiser invites')
        ordering = ('-time',)
  
    def __unicode__(self): 
        return self.invitation_code

