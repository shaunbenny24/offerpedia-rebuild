from django.contrib import admin
from payments.models import Payment, BankTransfer


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('auto_id','currency','amount','order_status')
admin.site.register(Payment,PaymentAdmin)


class BankTransferAdmin(admin.ModelAdmin):
    list_display = ('auto_id','date_added','amount','date','status','transfer_id')
admin.site.register(BankTransfer,BankTransferAdmin)
