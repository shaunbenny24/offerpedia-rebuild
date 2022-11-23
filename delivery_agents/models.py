# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel
from versatileimagefield.fields import VersatileImageField
import uuid


class DeliveryAgent(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'delivery_agents_delivery_agent'
        verbose_name = _('Delivery Agent')
        verbose_name_plural = _('Delivery Agents')
        ordering = ('id',)

    def __str__(self):
        return "%s - %s" %(self.user.username,self.phone)


