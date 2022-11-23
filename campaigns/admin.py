from django.contrib import admin
from . models import UserCampaign, CampaignView, CampaignCashbackAmount, Campaign

# Register your models here.
admin.site.register(UserCampaign)
admin.site.register(CampaignView)
admin.site.register(CampaignCashbackAmount)
admin.site.register(Campaign)