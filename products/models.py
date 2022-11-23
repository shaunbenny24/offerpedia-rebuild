import uuid
from decimal import Decimal
from versatileimagefield.fields import VersatileImageField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from main.models import BaseModel


class ProductCategory(BaseModel):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField(blank=True,null=True)
    image = VersatileImageField('Image',upload_to='products/categories/')
    
    is_deleted = models.BooleanField(default=False)

    def get_image(self):
        if self.image:
            image= self.image.crop['130x130'].url
        else:
            image=''
        return image
    
    class Meta:
        db_table = 'products_category'
        verbose_name = _('products category')
        verbose_name_plural = _('products categories')
        ordering = ('name',)      
    
    def __str__(self): 
        return self.name


class ProductVarient(BaseModel):
    varient_name = models.CharField(max_length=128,unique=True)
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'products_varient'
        verbose_name = _('product Varients')
        verbose_name_plural = _('product Varients')
        ordering = ('varient_name',)      
    
    def __str__(self): 
        return self.varient_name


class ProductSubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128,unique=True)
    category = models.ForeignKey("products.ProductCategory",limit_choices_to={'is_deleted': False},blank=True,null=True,on_delete=models.CASCADE)
    image = VersatileImageField('Image',upload_to='products/categories/',blank=True,null=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'products_sub_category'
        verbose_name = _('products subcategory')
        verbose_name_plural = _('products subcategories')
        ordering = ('name',)      
    
    def __str__(self): 
        return self.name


class MetaKeyword(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'meta_keywords'
        verbose_name = _('Meta Keyword')
        verbose_name_plural = _('Meta Keywords')
        ordering = ('name',)      

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True)
    featured_image = VersatileImageField('Featured Image',upload_to='products/featured_images',blank=True,null=True)
    youtube_video = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey("products.ProductCategory",limit_choices_to={'is_deleted': False},blank=True,null=True,on_delete=models.CASCADE)
    sub_category = models.ForeignKey("products.ProductSubCategory",limit_choices_to={'is_deleted': False},blank=True,null=True,on_delete=models.CASCADE)
    varients = models.ManyToManyField(ProductVarient,blank=True)

    price = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cost = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    tax = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    mrp = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    stock = models.PositiveIntegerField(default=1)
    first_time_stock = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    low_stock_limit = models.PositiveIntegerField(default=1)
    discount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    meta_keywords = models.ManyToManyField(MetaKeyword)
    meta_description = models.TextField(null=True, blank=True)
    campaign = models.ForeignKey("campaigns.Campaign",on_delete=models.CASCADE,blank=True,null=True)
    out_of_stock_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    hide = models.BooleanField(default=False)
    free = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def get_image(self):
        if self.featured_image:
            image= self.featured_image.crop['300x300'].url
        else:
            image=''
        return image

    def get_admin_image(self):
        if self.featured_image:
            image= self.featured_image.crop['125x125'].url
        else:
            image=''
        return image
    
    class Meta:
        db_table = 'products_product'
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('name',)  
        
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey("products.Product",on_delete=models.CASCADE)
    image = VersatileImageField('Image',upload_to='products/')
    is_deleted = models.BooleanField(default=False)

    def get_image(self):
        if self.image:
            image= self.image.crop['100x100'].url
        else:
            image=''
        return image
    
    class Meta:
        db_table = 'products_product_image'
        verbose_name = _('product image')
        verbose_name_plural = _('product images')
        ordering = ('product',)  
        
    def __str__(self):
        return self.product.name


