# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from cities.models import Country, City, State


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','web_code','flag','phone_code','phone_number_length')
admin.site.register(Country,CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name','state','country')
admin.site.register(City,CityAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name','country')
admin.site.register(State,StateAdmin)