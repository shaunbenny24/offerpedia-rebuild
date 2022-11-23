from django.contrib import admin
from main.models import Mode, Settings


class ModeAdmin(admin.ModelAdmin):
    list_display = ('readonly','maintenance','down')
admin.site.register(Mode,ModeAdmin)


admin.site.register(Settings)
