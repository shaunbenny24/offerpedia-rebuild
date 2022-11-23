from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel
from paypal.standard.models import ST_PP_COMPLETED
from django.conf import settings
from django.utils import timezone
import uuid


BANK_TRANSFER_CHOICE = (
    ('Pending',"Pending"),
    ('Completed',"Completed"),
    ('Cancelled',"Cancelled")
)


class AppUserPayment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='rel_payment_paytm')
    order_id = models.CharField(max_length=30,blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)
    response_code = models.IntegerField(blank=True,null=True)
    currency = models.CharField(max_length=4, null=True, blank=True)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    status_text = models.TextField()
    status = models.CharField(max_length=128, null=True, blank=True)
    status_code = models.CharField(max_length=128, null=True, blank=True)
    status_message = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'payments_app_user_payment'
        verbose_name = _('app user payment')
        verbose_name_plural = _('app user payments')
        ordering = ('-id',)

    def __unicode__(self):
        return self.order_id


class Payment(BaseModel):
    amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    currency = models.CharField(max_length=200,null=True,blank=True)
    language = models.CharField(max_length=200,null=True,blank=True)
    
    order_status = models.CharField(max_length=200,null=True,blank=True)
    
    tracking_id = models.CharField(max_length=200,null=True,blank=True)
    bank_ref_no = models.CharField(max_length=200,null=True,blank=True)
    failure_message = models.TextField(null=True,blank=True)
    payment_mode = models.CharField(max_length=200,null=True,blank=True)
    payment_type = models.CharField(max_length=200,null=True,blank=True)
    
    card_name = models.CharField(max_length=200,null=True,blank=True)
    status_code = models.CharField(max_length=200,null=True,blank=True)
    status_message = models.TextField(null=True,blank=True)
    
    billing_name = models.CharField(max_length=200,null=True,blank=True)
    billing_address = models.TextField(null=True,blank=True)
    billing_city = models.CharField(max_length=200,null=True,blank=True)
    billing_state = models.CharField(max_length=200,null=True,blank=True)
    billing_zip = models.CharField(max_length=200,null=True,blank=True)
    billing_country = models.CharField(max_length=200,null=True,blank=True)
    billing_tel = models.CharField(max_length=200,null=True,blank=True)
    billing_email = models.CharField(max_length=200,null=True,blank=True)
    
    delivery_name = models.CharField(max_length=200,null=True,blank=True)
    delivery_address = models.TextField(null=True,blank=True)
    delivery_city = models.CharField(max_length=200,null=True,blank=True)
    delivery_state = models.CharField(max_length=200,null=True,blank=True)
    delivery_zip = models.CharField(max_length=200,null=True,blank=True)
    delivery_country = models.CharField(max_length=200,null=True,blank=True)
    delivery_tel = models.CharField(max_length=200,null=True,blank=True)
    
    merchant_param1 = models.CharField(max_length=200,null=True,blank=True)
    merchant_param2 = models.CharField(max_length=200,null=True,blank=True)
    merchant_param3 = models.CharField(max_length=200,null=True,blank=True)
    merchant_param4 = models.CharField(max_length=200,null=True,blank=True)
    merchant_param5 = models.CharField(max_length=200,null=True,blank=True)
    
    is_updated = models.BooleanField(default=False)
     
    class Meta:
        db_table = 'payments_payment'
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
        ordering = ('-auto_id',)
  
    def __unicode__(self): 
        return "%s" %str(self.amount)
    

from django.conf import settings
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
def show_me_the_money(sender, **kwargs):

    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != settings.PAYPAL_MERCHANT_EMAIL_ADDRESS:
            pass
        if ipn_obj.custom == "Upgrade all users!":
            pass
    else:
        pass


def invalid(sender, **kwargs):
    print (invalid)

valid_ipn_received.connect(show_me_the_money)
invalid_ipn_received.connect(invalid)


class Transfer(models.Model):
    transfer_id = models.CharField(max_length=128)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    from_user = models.ForeignKey('advertisers.AppUser', on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey('advertisers.AppUser', on_delete=models.CASCADE, related_name='to_user')
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    class Meta:
        db_table = 'payments_transfer'
        verbose_name = _('transfer')
        verbose_name_plural = _('transfers')
        ordering = ('-auto_id',)

    def __unicode__(self):
        return self.transfer_id


class ClientPay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pay_id = models.CharField(max_length=128)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    from_user = models.ForeignKey('advertisers.AppUser', on_delete=models.CASCADE, related_name='from_user_%(class)s_objects')
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'payments_client_pay'
        verbose_name = _('client pay')
        verbose_name_plural = _('client pays')
        ordering = ('-auto_id',)

    def __unicode__(self):
        return self.payment_id


class ClientSettlement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.CharField(max_length=128)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'payments_client_settlement'
        verbose_name = _('client settlement')
        verbose_name_plural = _('client settlements')
        ordering = ('-auto_id',)

    def __unicode__(self):
        return self.transaction_id


class AdvertiserPayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.CharField(max_length=128)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    dealer = models.ForeignKey('advertisers.Advertiser', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'payments_advertiser_payment'
        verbose_name = _('advertiser payment')
        verbose_name_plural = _('advertiser payments')
        ordering = ('-auto_id',)

    def __unicode__(self):
        return self.transaction_id


class ClientRefund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    refund_id = models.CharField(max_length=128)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    campaign = models.ForeignKey('campaigns.Campaign', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'payments_client_refund'
        verbose_name = _('client refund')
        verbose_name_plural = _('client refunds')
        ordering = ('-auto_id',)

    def __unicode__(self):
        return self.refund_id


class DealerSettlementCampaignHistory(models.Model):
    advertiser_campaign = models.ForeignKey("campaigns.AdvertiserCampaign", on_delete=models.CASCADE)
    settlement = models.ForeignKey("payments.AdvertiserPayment", on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))],default=0)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'payments_settlement_campaign_history'
        verbose_name = 'settlement campaign history'
        verbose_name_plural = 'settlement campaign histories'
        ordering = ('-id',)

    def __unicode__(self):
        return str(self.id)


class BankTransfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transfer_id = models.CharField(max_length=128)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    user = models.ForeignKey('advertisers.AppUser', on_delete=models.CASCADE, related_name='bank_transfer_user')
    transaction_id = models.CharField(max_length=128,blank=True,null=True)
    settlement_amount = models.CharField(max_length=128,default=0)

    account_no = models.CharField(max_length=128)
    account_holder_name = models.CharField(max_length=128)
    iban = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    status = models.CharField(max_length=128,choices=BANK_TRANSFER_CHOICE,default="Pending")
    date = models.DateTimeField(default=timezone.now)

    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'payments_bank_transfer'
        verbose_name = _('bank transfer')
        verbose_name_plural = _('bank transfers')
        ordering = ('-auto_id',)

    def __unicode__(self):
        return self.transfer_id


class InviteCashback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    app_user = models.ForeignKey('advertisers.AppUser', on_delete=models.CASCADE,related_name='app_user')
    is_referring = models.BooleanField(default=False)
    refer = models.ForeignKey('advertisers.AppUser', on_delete=models.CASCADE, related_name='refer')
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'payments_invite_cashback'
        verbose_name = _('invite cashback')
        verbose_name_plural = _('invite cashbacks')
        ordering = ('-auto_id',)

    def __unicode__(self):
        return self.auto_id
        