from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel
import uuid


STATUS = (
    ('pending','Pending'),
    ('shipped','Shipped'),
    ('delivered','Delivered'),
)

CANCEL_STATUS = (
    ('pending','Pending'),
    ('progress','In Progress'),
    ('completed','Completed'),
)

PAYMENT_STATUS = (
    ('pending','Pending'),
    ('received','Received'),
    ('failed','Failed'),
)

PAYMENT_METHOD = (
    ('cash_on_delivary','Cash On Delivary'),
    ('online_payment','Online Payment'),
)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    order_id = models.CharField(max_length=128)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)  
    billing_address = models.ForeignKey("advertisers.AppUserAddress",on_delete=models.CASCADE,null=True)
    app_user = models.ForeignKey("advertisers.AppUser",on_delete=models.CASCADE,related_name='customer')
    refferer = models.ForeignKey("advertisers.AppUser",on_delete=models.CASCADE,blank=True,null=True,related_name='refferer')
    campaign = models.ForeignKey("campaigns.Campaign",on_delete=models.CASCADE,blank=True,null=True)
    client = models.ForeignKey("clients.Client",on_delete=models.CASCADE, blank=True, null=True)
    total_tax_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    total_discount_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    amount_payable = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    total_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))]) 
    
    order_status = models.CharField(max_length=128,choices=STATUS,default="pending")
    payment_status = models.CharField(max_length=128,choices=PAYMENT_STATUS,default="pending")
    payment_method = models.CharField(max_length=128,choices=PAYMENT_METHOD)
    cancel_status = models.CharField(max_length=128,choices=CANCEL_STATUS,default="pending")
    cancel_reason = models.CharField(max_length=128,blank=True,null=True)

    cashback_used = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    cashback_type = models.CharField(max_length=128,blank=True,null=True)
    amount_to_referer = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    amount_to_user = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    delivery_charge = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))]) 

    delivery_agent = models.ForeignKey('delivery_agents.DeliveryAgent',on_delete=models.CASCADE,blank=True,null=True)
    accepted_by_delivery_agent = models.BooleanField(default=False)
    rejected_by_delivery_agent = models.BooleanField(default=False)

    is_cancelled = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    date_updated = models.DateField(blank=True,null=True)

    class Meta:
        db_table = 'orders_order'
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ('-date_added',)
    
    def __str__(self): 
        return "%s - %s" %(str(self.app_user.phone),str(self.amount_payable))

    def get_order_items(self):
        return OrderItem.objects.filter(order=self)

    def total_taxable_amount(self):
        order_items = OrderItem.objects.filter(order=self)
        total_taxable_amount = 0
        for order_item in order_items:
            total_taxable_amount += order_item.taxable_amount()

        return total_taxable_amount

    def payment_received(self) :
        payment_status = self.payment_status
        amount = 0
        if payment_status == 'received':
            amount = self.amount_payable
        return amount


class OrderItem(models.Model):
    order = models.ForeignKey("orders.Order",on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product",on_delete=models.CASCADE)
    varient = models.CharField(max_length=128,blank=True,null=True)
    qty = models.IntegerField(default=0)
    cost = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    price = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    tax = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    tax_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    discount_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    subtotal = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    mrp = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    date_updated = models.DateField(blank=True,null=True)

    is_deleted = models.BooleanField(default=False)
     
    class Meta:
        db_table = 'orders_order_item'
        verbose_name = _('order item')
        verbose_name_plural = _('order items')
        ordering = ('product',) 
         
    def taxable_amount(self):
        return str(self.subtotal) - str(self.tax_amount)     
    
    def __str__(self): 
        return "%s - %s" %(str(self.product.name),str(self.qty)) 


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    app_user = models.OneToOneField("advertisers.AppUser",on_delete=models.CASCADE)
    amount_payable = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    is_deleted= models.BooleanField(default=False)

    class Meta:
        db_table = 'app_users_cart'
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-id',)

    def __str__(self):
        return self.app_user.phone


class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey("orders.Cart",on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product",on_delete=models.CASCADE)
    varient = models.CharField(max_length=128,blank=True,null=True)
    qty = models.IntegerField()
    mrp = models.DecimalField(null=True,blank=True,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cost = models.DecimalField(null=True,blank=True,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    price = models.DecimalField(null=True,blank=True,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    subtotal = models.DecimalField(null=True,blank=True,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    is_deleted = models.BooleanField(default=False)
    is_processing = models.BooleanField(default=False)

    class Meta:
        db_table = 'app_users_cart_item'
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')
        ordering = ('product',)

    def __str__(self):
        return self.product.name
  