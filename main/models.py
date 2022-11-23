import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from django.core.validators import MinValueValidator


BOOL_CHOICES = ((1, 'Yes'), (0, 'No'))

THEME_CHOICES = (
    ('teal', 'Teal'),
    ('blue', 'Blue'),
    ('bluegrey', 'Blue Grey'),
    ('cyan-600', 'Cyan'),
    ('green', 'Green'),
    ('lightgreen', 'Light Green'),
    ('purple-400', 'Purple'),
    ('red-400', 'Red'),
    ('pink-400', 'Pink'),
    ('brown', 'Brown'),
    ('grey-600', 'Grey'),
    ('orange', 'Orange')
)

PRINT_CHOICES = (
    ('a4', 'A4'),
    ('compact', 'Compact(77mm)'),
)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    creator = models.ForeignKey("auth.User",blank=True, on_delete=models.CASCADE,related_name="creator_%(class)s_objects")
    updator = models.ForeignKey("auth.User",blank=True, on_delete=models.CASCADE,related_name="updator_%(class)s_objects")
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    a_id = models.PositiveIntegerField(blank=True,null=True)

    class Meta:
        abstract = True


class Mode(models.Model):
    readonly = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)
    down = models.BooleanField(default=False)

    class Meta:
        db_table = 'mode'
        verbose_name = _('mode')
        verbose_name_plural = _('mode')
        ordering = ('id',)

    class Admin:
        list_display = ('id', 'readonly', 'maintenance', 'down')

    def __unicode__(self):
        return str(self.id)


class Settings(models.Model):
    minimum_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    paytm_merchant_id = models.CharField(max_length=128,blank=True,null=True)
    paytm_merchant_key = models.CharField(max_length=128,blank=True,null=True)
    paytm_sales_wallet_guid = models.CharField(max_length=128,blank=True,null=True)
    paytm_merchant_guid = models.CharField(max_length=128,blank=True,null=True)
    paytm_cashback_wallet_guid = models.CharField(max_length=128,blank=True,null=True)
    paytm_cashback_merchant_guid = models.CharField(max_length=128,blank=True,null=True)
    commission_percentage = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bank_transfer_minimum_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    referal_bonus = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    invitation_code_length = models.PositiveIntegerField(default=0)
    invitation_usage_limit = models.PositiveIntegerField(default=0)
    referral_for_both = models.BooleanField(default=False)
    total_invitation = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'main_settings'
        verbose_name = _('settings')
        verbose_name_plural = _('settings')
        ordering = ('id',)

    def __unicode__(self):
        return str(self.id)


