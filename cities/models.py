from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from decimal import Decimal


class Country(models.Model):
    name = models.CharField(max_length=128)
    local_name = models.CharField(max_length=128,blank=True,null=True)
    web_code = models.CharField(max_length=128)
    country_code = models.CharField(max_length=128,blank=True,null=True)
    region = models.CharField(max_length=128,blank=True,null=True)
    continent = models.CharField(max_length=128,blank=True,null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    surface_area = models.DecimalField(decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))],blank=True,null=True)
    population = models.DecimalField(decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))],blank=True,null=True)
    flag = models.ImageField(upload_to="countries/flags/",blank=True,null=True)
    phone_code = models.CharField(max_length=128,blank=True,null=True)
    is_active = models.BooleanField(default=False)
    phone_number_length = models.PositiveIntegerField(blank=True,null=True)

    class Meta:
        db_table = 'cities_country'
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey('cities.Country', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    
    class Meta:
        db_table = 'cities_state'
        verbose_name = _('state')
        verbose_name_plural = _('states')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=128)
    state = models.ForeignKey('cities.State', on_delete=models.CASCADE,blank=True,null=True)
    country = models.ForeignKey('cities.Country', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    is_district = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'cities_city'
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        ordering = ('name',)

    def __unicode__(self):
        return self.name