# Generated by Django 4.1.3 on 2022-11-23 11:20

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('delivery_agents', '0001_initial'),
        ('campaigns', '0001_initial'),
        ('products', '0001_initial'),
        ('advertisers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount_payable', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('is_deleted', models.BooleanField(default=False)),
                ('app_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='advertisers.appuser')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'db_table': 'app_users_cart',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('order_id', models.CharField(max_length=128)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('total_tax_amount', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('total_discount_amount', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('amount_payable', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('total_amount', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=128)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('received', 'Received'), ('failed', 'Failed')], default='pending', max_length=128)),
                ('payment_method', models.CharField(choices=[('cash_on_delivary', 'Cash On Delivary'), ('online_payment', 'Online Payment')], max_length=128)),
                ('cancel_status', models.CharField(choices=[('pending', 'Pending'), ('progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=128)),
                ('cancel_reason', models.CharField(blank=True, max_length=128, null=True)),
                ('cashback_used', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('cashback_type', models.CharField(blank=True, max_length=128, null=True)),
                ('amount_to_referer', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('amount_to_user', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('delivery_charge', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('accepted_by_delivery_agent', models.BooleanField(default=False)),
                ('rejected_by_delivery_agent', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_updated', models.DateField(blank=True, null=True)),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='advertisers.appuser')),
                ('billing_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisers.appuseraddress')),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.campaign')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('delivery_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery_agents.deliveryagent')),
                ('refferer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refferer', to='advertisers.appuser')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'orders_order',
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varient', models.CharField(blank=True, max_length=128, null=True)),
                ('qty', models.IntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('tax', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('tax_amount', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('discount_amount', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('subtotal', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('mrp', models.DecimalField(decimal_places=3, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('date_updated', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
                'db_table': 'orders_order_item',
                'ordering': ('product',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('varient', models.CharField(blank=True, max_length=128, null=True)),
                ('qty', models.IntegerField()),
                ('mrp', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('cost', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('subtotal', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_processing', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'cart item',
                'verbose_name_plural': 'cart items',
                'db_table': 'app_users_cart_item',
                'ordering': ('product',),
            },
        ),
    ]
