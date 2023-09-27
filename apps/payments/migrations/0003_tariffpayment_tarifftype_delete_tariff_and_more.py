# Generated by Django 4.2.3 on 2023-09-26 09:41

from django.db import migrations, models
import django.db.models.deletion
import utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_product_limit'),
        ('payments', '0002_tariff_remove_wallet_seller_alter_payment_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TariffPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Payment amount')),
                ('period', models.PositiveIntegerField(blank=True, null=True, verbose_name='Period')),
                ('start_date', models.DateField(default=utils.time.get_current_date, verbose_name='Start date of the payment period')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date of payment period')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('product_limit', models.PositiveIntegerField(default=10, verbose_name='Product limit')),
                ('range_weight', models.PositiveIntegerField(default=0, verbose_name='Range weight')),
                ('is_active', models.BooleanField(blank=True, null=True, verbose_name='Is active')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='stores.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'Tariff Payment',
                'verbose_name_plural': 'Tariff Payments',
            },
        ),
        migrations.CreateModel(
            name='TariffType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('period', models.PositiveIntegerField(default=0, verbose_name='Period')),
                ('product_limit', models.PositiveIntegerField(default=10, verbose_name='Product limit')),
                ('range_weight', models.PositiveIntegerField(default=0, verbose_name='Range weight')),
            ],
            options={
                'verbose_name': 'Tariff Type',
                'verbose_name_plural': 'Tariff Types',
            },
        ),
        migrations.DeleteModel(
            name='Tariff',
        ),
        migrations.RemoveField(
            model_name='paymenttype',
            name='type',
        ),
        migrations.AddField(
            model_name='tariffpayment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payments.tarifftype', verbose_name='Tariff Type'),
        ),
    ]
