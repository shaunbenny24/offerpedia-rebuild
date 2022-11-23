from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel
from decimal import Decimal
from versatileimagefield.fields import VersatileImageField
import datetime


STATUS = (
    ('open', 'Open'),
    ('closed', 'Closed'),
)


THEME = (
    ('theme-yellow', 'Yellow Theme'),
    ('theme-violet', 'Violet Theme'),
    ('theme-green', 'Green Theme'),
    ('theme-red', 'Red Theme'),
)


DESIGN_CHOICES = (
    ('titanium', 'Titanium'),
    ('red-flower', 'Red Flower'),
    ('news-letter-blue', 'News letter blue'),
    ('news-letter-violet', 'News letter violet'),
    ('news-letter-red', 'News letter red'),
    ('news-letter-green', 'News letter green'),
    ('news-letter-orange', 'News letter orange'),
)


BOOKING_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('failed', 'Failed'),
)


CASHBACK_TYPE = (
    ('to_referrer', 'To Referrer'),
    ('to_user', 'To User'),
)


class CampaignType(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField()
    icon = models.ImageField(upload_to="campaign_type/icon/")
    background_image = models.ImageField(upload_to="campaign_type/bg/",blank=True,null=True)
    amount_to_user = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    amount_from_client = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    is_ecommerce = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    class Meta:
        db_table = 'campaigns_campaign_type'
        verbose_name = _('campaign type')
        verbose_name_plural = _('campaign types')

    def __unicode__(self):
        return self.name


class Campaign(BaseModel):
    campaign_type = models.ForeignKey("campaigns.CampaignType", on_delete=models.CASCADE,limit_choices_to={'is_deleted': False})
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    public_description = models.TextField()
    is_ecommerce = models.BooleanField(default=False)

    from_date = models.DateField()
    to_date = models.DateField()
    pricing = models.ForeignKey("campaigns.CampaignPricing", on_delete=models.CASCADE,null=True,blank=True,limit_choices_to={'is_deleted': False})
    total_bookings = models.PositiveIntegerField(default=0)
    user_click_limit = models.PositiveIntegerField(default=250)

    status = models.CharField(max_length=128,choices=STATUS,default="open")
    private = models.BooleanField(default=False)

    active_clicks = models.PositiveIntegerField(default=0)
    dead_clicks = models.PositiveIntegerField(default=0)

    position = models.PositiveIntegerField(default=1)

    balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_need_enquiry = models.BooleanField(default=False)
    enquiry_button_text = models.CharField(max_length=128,blank=True,null=True)

    need_promo_code = models.BooleanField(default=False)
    number_of_promo_codes = models.PositiveIntegerField(default=0)
    promocode_length = models.PositiveIntegerField(default=4)
    expiry_date = models.DateField(blank=True,null=True)
    discount_percentage = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    discount_description = models.CharField(max_length=255,blank=True,null=True)

    need_cashback_promo_code = models.BooleanField(default=False)
    number_of_cashback_promo = models.PositiveIntegerField(default=0)
    cashback_highlights = models.TextField(blank=True,null=True)
    cashback_amount_from_client = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_to_user = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_to_referrer = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_collected = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_used = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_refunded = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    need_bill_amount_promo_code = models.BooleanField(default=False)
    bill_amount_highlights = models.TextField(blank=True,null=True)
    bill_amount_collected_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bill_amount_bonus_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bill_amount_net_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bill_amount_used_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bill_amount_refunded_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bill_amount_balance_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bill_amount_cashback_pricing = models.ForeignKey("campaigns.BillAmountCashbackPricing", on_delete=models.CASCADE,null=True,blank=True,limit_choices_to={'is_deleted': False})

    youtube_video_id = models.CharField(max_length=255,blank=True,null=True)
    featured_image = VersatileImageField('Featured Image',upload_to="campaigns/featured_image",blank=True,null=True)
    company_logo = VersatileImageField('Company Logo',upload_to="campaigns/company_logo",blank=True,null=True)

    need_cashback_voucher_promo_code = models.BooleanField(default=False)
    number_of_cashback_voucher_promo = models.PositiveIntegerField(default=0)
    cashback_voucher_highlights = models.TextField(blank=True,null=True)
    cashback_amount_voucher_from_client = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_voucher_to_user = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_voucher_to_referrer = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_voucher_collected = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_voucher_used = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_voucher_refunded = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_amount_voucher_balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    contact_email = models.EmailField(blank=True,null=True)
    contact_phone = models.CharField(max_length=128,blank=True,null=True)
    contact_address = models.TextField(blank=True,null=True)
    contact_website = models.CharField(null=True,blank=True,max_length=128)
    latitude = models.DecimalField(decimal_places=6, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))],blank=True,null=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))],blank=True,null=True)
    customizable_button_link = models.CharField(null=True,blank=True,max_length=128)
    customizable_button_text= models.CharField(null=True,blank=True,max_length=128)

    user_benifit = models.CharField(max_length=128,blank=True,null=True)
    referrer_benifit = models.CharField(max_length=128,blank=True,null=True)

    delivery_charge = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    sharable_content = models.TextField()

    def booking_status(self):
        is_closed = False

        if self.total_bookings >= self.total_seats_available:
            is_closed = True

        return {
            "is_closed" : is_closed
        }

    def days_left(self):
        days_left = 0
        today  = datetime.date.today()
        if today < self.to_date:
            days_left = (self.to_date - today).days + 1

        return days_left

    def estimated_click(self):
        return int(self.pricing.no_of_clicks)

    def clicks_left(self):
        balance_click = 0
        if self.pricing:
            balance_click = (self.pricing.no_of_clicks - self.active_clicks)
            if balance_click < 0:
                balance_click = 0

        return balance_click

    def get_graph_data(self):
        campaign_views = CampaignView.objects.filter(campaign=self)
        no_of_days = (self.to_date - self.from_date).days + 1
        date_list = []
        date_list_string = ""
        active_clicks = []
        dead_clicks = []
        for i in range(0, no_of_days):
            date_obj = self.from_date + datetime.timedelta(days=i)
            date_list.append(date_obj)
            date_string = date_obj.strftime('%d/%m/%Y')
            date_list_string += date_string+","

        if campaign_views:
            for date_list_obj in date_list:
                active_click = campaign_views.filter(time__date=date_list_obj,active_click=True).count()
                active_clicks.append(active_click)

                dead_click = campaign_views.filter(time__date=date_list_obj,active_click=False).count()
                dead_clicks.append(dead_click)

        results = {
            "date_list" : date_list,
            "active_clicks" : active_clicks,
            "dead_clicks" : dead_clicks,
            "date_list_string" : date_list_string[:-1]
        }
        return results

    def get_image(self):
        if self.company_logo:
            image= self.company_logo.crop['175x125'].url
        elif self.featured_image:
            image= self.featured_image.crop['175x125'].url
        else:
            image=''
        return image


    class Meta:
        db_table = 'campaigns_campaign'
        verbose_name = _('campaign')
        verbose_name_plural = _('campaigns')

    def __unicode__(self):
        return self.title


class Invoice(BaseModel):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    invoice_no = models.CharField(max_length=128)
    billing_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    payment_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bill_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    billing_percentage = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    
    amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    paid = models.DecimalField(decimal_places=3,default=0, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    balance = models.DecimalField(decimal_places=3,default=0, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    invoice_date = models.DateField()
    due_date = models.DateField(blank=True,null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_invoice'
        verbose_name = _('invoice')
        verbose_name_plural = _('invoices')

    def __unicode__(self):
        return str(self.invoice_date)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey("campaigns.Invoice", on_delete=models.CASCADE)
    bill_amount_cashback = models.ForeignKey("campaigns.CampaignBillAmountCashbackCode", on_delete=models.CASCADE,blank=True,null=True)
    payment = models.ForeignKey("payments.ClientPay", on_delete=models.CASCADE,blank=True,null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_invoice_item'
        verbose_name = _('invoice item')
        verbose_name_plural = _('invoice items')

    def __unicode__(self):
        return str(self.invoice.invoice_date)


class Receipt(BaseModel):
    invoice = models.ForeignKey("campaigns.Invoice", on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.DecimalField(decimal_places=3,default=0, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    balance = models.DecimalField(decimal_places=3,default=0, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_receipt'
        verbose_name = _('receipt')
        verbose_name_plural = _('receipts')

    def __unicode__(self):
        return str(self.date)


class InvoiceMail(models.Model):
    name = models.TextField(blank=True,null=True,max_length=128)
    email = models.EmailField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)

    class Meta:
        db_table = 'invoices_mail'
        verbose_name = _('invoice mail')
        verbose_name_plural = _('invoice mails')

    def __unicode__(self):
        return str(self.name)


class CampaignRegion(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    country = models.ForeignKey("cities.Country", on_delete=models.CASCADE)
    state = models.ForeignKey("cities.State", on_delete=models.CASCADE,blank=True,null=True)
    city = models.ForeignKey("cities.City", on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = 'campaigns_campaign_state'
        verbose_name = _('campaign state')
        verbose_name_plural = _('campaign states')

    def __unicode__(self):
        return self.campaign.title


class BillAmountCollection(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bonus_percentage = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bonus_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    date = models.DateField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_bill_amount_collection'
        verbose_name = _('bill amount collection')
        verbose_name_plural = _('bill amount collections')

    def __unicode__(self):
        return self.campaign.title + " - " + str(self.amount)


class CampaignAccessibleRegion(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    country = models.ForeignKey("cities.Country", on_delete=models.CASCADE)
    state = models.ForeignKey("cities.State", on_delete=models.CASCADE,blank=True,null=True)
    city = models.ForeignKey("cities.City", on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = 'campaigns_campaign_accessible_region'
        verbose_name = _('campaign accessible region')
        verbose_name_plural = _('campaign accessible regions')

    def __unicode__(self):
        return self.campaign.title


class PromoCode(BaseModel):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    code = models.CharField(max_length=128)
    expiry_date = models.DateField()
    discount_percentage = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    discount_description = models.CharField(max_length=255)

    is_deleted = models.BooleanField(default=False)

    def status(self):
        is_expired = False

        today = datetime.date.today()
        if self.expiry_date < today:
            is_expired = True

        return {
            "is_expired" : is_expired,
        }

    class Meta:
        db_table = 'campaigns_promo_code'
        verbose_name = _('promo code')
        verbose_name_plural = _('promo codes')

    def __unicode__(self):
        return self.code


class CampaignContent(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_content'
        verbose_name = _('campaign content')
        verbose_name_plural = _('campaign contents')

    def __unicode__(self):
        return self.title


class CampaignGallery(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    title = models.CharField(max_length=128,blank=True,null=True)
    image = models.ImageField(upload_to="campaigns/gallery")

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_gallery'
        verbose_name = _('campaign gallery')
        verbose_name_plural = _('campaign galleries')

    def __unicode__(self):
        return self.title


class CampaignPricing(BaseModel):
    campaign_type = models.ForeignKey("campaigns.CampaignType", on_delete=models.CASCADE)
    no_of_clicks = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_pricing'
        verbose_name = _('campaign pricing')
        verbose_name_plural = _('campaign pricings')

    def __unicode__(self):
        return str(self.amount) + " - " + str(self.no_of_clicks)


class BillAmountCashbackPricing(BaseModel):
    amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    percentage = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    percentage_to_user = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    percentage_to_referrer = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    bonus_percentage = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'bill_amount_cashback_pricing'
        verbose_name = _('billamount cashback pricing')
        verbose_name_plural = _('billamount cashback pricings')

    def __unicode__(self):
        return str(self.amount)


class EmailTemplate(BaseModel):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    design = models.CharField(max_length=128,choices=DESIGN_CHOICES)

    content1 = models.TextField(null=True,blank=True)
    content2 = models.TextField(null=True,blank=True)
    content3 = models.TextField(null=True,blank=True)
    content4 = models.TextField(null=True,blank=True)
    content5 = models.TextField(null=True,blank=True)
    content6 = models.TextField(null=True,blank=True)
    content7 = models.TextField(null=True,blank=True)
    content8 = models.TextField(null=True,blank=True)
    content9 = models.TextField(null=True,blank=True)
    content10 = models.TextField(null=True,blank=True)
    content11 = models.TextField(null=True,blank=True)
    content12 = models.TextField(null=True,blank=True)
    content13 = models.TextField(null=True,blank=True)
    content14 = models.TextField(null=True,blank=True)
    content15 = models.TextField(null=True,blank=True)

    image1 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image2 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image3 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image4 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image5 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image6 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image7 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image8 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image9 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image10 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image11 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image12 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image13 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image14 = models.ImageField(upload_to="email/template/",blank=True,null=True)
    image15 = models.ImageField(upload_to="email/template/",blank=True,null=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_email_template'
        verbose_name = _('email template')
        verbose_name_plural = _('email templates')

    def __unicode__(self):
        return self.design


class SentEmail(BaseModel):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    email_template = models.ForeignKey("campaigns.EmailTemplate", on_delete=models.CASCADE)
    groups = models.ManyToManyField("contacts.Group")
    total_contacts = models.PositiveIntegerField(default=0)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_sent_email'
        verbose_name = _('sent email')
        verbose_name_plural = _('sent emails')

    def __unicode__(self):
        return self.campaign.title


class Booking(BaseModel):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    email_template = models.ForeignKey("campaigns.EmailTemplate", on_delete=models.CASCADE)
    contact = models.ForeignKey("contacts.Contact", on_delete=models.CASCADE)
    promo_code = models.ForeignKey("campaigns.PromoCode", on_delete=models.CASCADE,null=True,blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    seats = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=128,choices=BOOKING_CHOICES,default="pending")
    amount = models.DecimalField(decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField(blank=True,null=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_booking'
        verbose_name = _('booking')
        verbose_name_plural = _('bookings')

    def __unicode__(self):
        return self.campaign.title


class CampaignView(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    email_template = models.ForeignKey("campaigns.EmailTemplate", on_delete=models.CASCADE,blank=True,null=True)
    contact = models.ForeignKey("contacts.Contact", on_delete=models.CASCADE,blank=True,null=True)
    refferer = models.ForeignKey("advertisers.AppUser", on_delete=models.CASCADE,related_name="refferer_%(class)s_objects",blank=True,null=True)
    app_user = models.ForeignKey("advertisers.AppUser", on_delete=models.CASCADE,related_name="appuser_%(class)s_objects",blank=True,null=True)
    cashback_active = models.BooleanField(default=False)
    dealer = models.ForeignKey("advertisers.Advertiser", on_delete=models.CASCADE,blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True)
    refferal_type = models.CharField(max_length=128,null=True,blank=True)
    visitor_ip_address = models.GenericIPAddressField()
    active_click = models.BooleanField(default=False)
    after_expired = models.BooleanField(default=False)
    visited_from = models.ForeignKey("cities.City", on_delete=models.CASCADE,null=True,blank=True)

    user_agent_browser_family = models.CharField(max_length=128,blank=True,null=True)
    user_agent_browser_version = models.CharField(max_length=128,blank=True,null=True)
    user_agent_os_family = models.CharField(max_length=128,blank=True,null=True)
    user_agent_os_version = models.CharField(max_length=128,blank=True,null=True)
    user_agent_device_family = models.CharField(max_length=128,blank=True,null=True)
    user_agent_device_brand = models.CharField(max_length=128,blank=True,null=True)
    user_agent_device_model = models.CharField(max_length=128,blank=True,null=True)

    cashback_promocode = models.CharField(max_length=128,blank=True,null=True)

    class Meta:
        db_table = 'campaigns_campaign_view'
        verbose_name = _('campaign view')
        verbose_name_plural = _('campaign views')
        ordering = ('-time',)

    def __unicode__(self):
        return self.campaign.title


class CampaignViewCashbackClaim(models.Model):
    campaign_view = models.ForeignKey("campaigns.CampaignView", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    cashback_code = models.CharField(max_length=128)
    country = models.ForeignKey("cities.Country", on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_view_cashback_claim'
        verbose_name = _('cashback claim')
        verbose_name_plural = _('cashback claims')

    def __unicode__(self):
        return str(self.phone)


class CampaignViewVoucherClaim(models.Model):
    campaign_view = models.ForeignKey("campaigns.CampaignView", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    voucher_code = models.CharField(max_length=128)
    country = models.ForeignKey("cities.Country", on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_view_voucher_claim'
        verbose_name = _('voucher claim')
        verbose_name_plural = _('voucher claims')

    def __unicode__(self):
        return str(self.phone)


class UserCampaign(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    app_user = models.ForeignKey("advertisers.AppUser", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    active_clicks = models.PositiveIntegerField(default=0)
    dead_clicks = models.PositiveIntegerField(default=0)
    earned = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    paid = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    is_withdrawed = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_user_campaign'
        verbose_name = _('user campaign')
        verbose_name_plural = _('user campaign')

    def __unicode__(self):
        return self.campaign.title


class AdvertiserCampaign(models.Model):
    date = models.DateField(blank=True,null=True)
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    advertiser = models.ForeignKey("advertisers.Advertiser", on_delete=models.CASCADE)
    earned = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    paid = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    balance = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    class Meta:
        db_table = 'campaigns_advertiser_campaign'
        verbose_name = _('advertiser campaign')
        verbose_name_plural = _('advertiser campaign')

    def __unicode__(self):
        return self.campaign.title


class CampaignCashbackPromocode(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    campaign_view = models.ForeignKey("campaigns.CampaignView", on_delete=models.CASCADE)
    promocode = models.CharField(max_length=128)
    cashback_code = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_cashback_promocode'
        verbose_name = _('campaign cashback promocode')
        verbose_name_plural = _('campaign cashback promocodes')

    def __unicode__(self):
        return self.campaign.title


class CampaignVoucherPromocode(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    voucher_code = models.CharField(max_length=128)
    is_used = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_voucher_promocode'
        verbose_name = _('campaign voucher promocode')
        verbose_name_plural = _('campaign voucher promocodes')

    def __unicode__(self):
        return self.voucher_code


class CampaignCashbackAmount(models.Model):
    cashback_claim = models.ForeignKey("campaigns.CampaignViewCashbackClaim", on_delete=models.CASCADE,blank=True,null=True)
    voucher_claim = models.ForeignKey("campaigns.CampaignViewVoucherClaim", on_delete=models.CASCADE,blank=True,null=True)
    bill_amount_cashback_claim = models.ForeignKey("campaigns.CampaignBillAmountCashbackClaim", on_delete=models.CASCADE,blank=True,null=True)
    cashback_type = models.CharField(max_length=128,choices=CASHBACK_TYPE)
    claim_name = models.CharField(max_length=120, blank=True, null=True)
    amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    refferer = models.ForeignKey("advertisers.AppUser", on_delete=models.CASCADE,blank=True,null=True)
    order = models.ForeignKey("orders.Order",on_delete=models.CASCADE,blank=True,null=True)

    is_withdrawed = models.BooleanField(default=False)
    is_admin_verified = models.BooleanField(default=False)
    expiry_date = models.DateField()
    date = models.DateField()
    time = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    is_invoice = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_campaign_cashback_amount'
        verbose_name = _('campaign cashback amount')
        verbose_name_plural = _('campaign cashback amounts')
        ordering = ('-id',)

    def __unicode__(self):
        return str(self.amount)


class CampaignBillAmountCashbackCode(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    bill_amount_cashback_claim = models.ForeignKey("campaigns.CampaignBillAmountCashbackClaim", on_delete=models.CASCADE,blank=True,null=True)
    bill_amount = models.DecimalField(default=0,decimal_places=3, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    cashback_code = models.CharField(max_length=128)
    receipt_number = models.CharField(max_length=128,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_invoiced = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_bill_amount_cashback_promocode'
        verbose_name = _('bill amount promocode')
        verbose_name_plural = _('bill amount promocodes')

    def cashback_claim(self):
        if CampaignBillAmountCashbackClaim.objects.filter(is_deleted=False,cashback_code=self.cashback_code).exists():
            return CampaignBillAmountCashbackClaim.objects.filter(is_deleted=False,cashback_code=self.cashback_code)[0]
        else:
            return None

    def __unicode__(self):
        return self.campaign.title


class CampaignBillAmountCashbackClaim(models.Model):
    campaign_view = models.ForeignKey("campaigns.CampaignView", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    cashback_code = models.CharField(max_length=128)
    country = models.ForeignKey("cities.Country", on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    is_applied = models.BooleanField(default=False)

    class Meta:
        db_table = 'campaigns_bill_amount_cashback_claim'
        verbose_name = _('cashback claim')
        verbose_name_plural = _('cashback claims')

    def __unicode__(self):
        return str(self.phone)


class CampaignEnquiry(models.Model):
    campaign_view = models.ForeignKey("campaigns.CampaignView", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField(blank=True,null=True)

    class Meta:
        db_table = 'campaigns_campaign_enquiry'
        verbose_name = _('cashback enquiry')
        verbose_name_plural = _('cashback enquiries')

    def __unicode__(self):
        return str(self.name)
