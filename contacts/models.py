from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel
from decimal import Decimal
    
    
class Group(BaseModel):
    name = models.CharField(max_length=128)
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'contacts_group'
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __unicode__(self):
        return self.name
    

class Contact(BaseModel):
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE,blank=True,null=True)
    country = models.ForeignKey("cities.Country", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    
    groups = models.ManyToManyField("contacts.Group")
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'contacts_contact'
        verbose_name = _('contact')
        verbose_name_plural = _('contact')

    def __unicode__(self):
        return self.name

