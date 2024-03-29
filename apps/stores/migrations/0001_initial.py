# Generated by Django 4.2.3 on 2023-09-25 10:51

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='stores.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Fuel type',
                'verbose_name_plural': 'Fuel types',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('country_of_origin', models.CharField(max_length=100, verbose_name='Country of origin')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('range_weight', models.PositiveSmallIntegerField(default=0, verbose_name='Range weight')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stores.category', verbose_name='Category')),
                ('fuel_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stores.fueltype', verbose_name='Fuel type')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('logo', models.ImageField(upload_to='stores/<django.db.models.fields.CharField>/', verbose_name='Logo')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='accounts.seller', verbose_name='Seller')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('value', models.TextField(verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='stores.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Specification',
                'verbose_name_plural': 'Specifications',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('text', models.TextField(max_length=5000, verbose_name='Text')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='stores.review', verbose_name='Parent')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='stores.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/None/', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='stores.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Discount')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='stores.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product Discount',
                'verbose_name_plural': 'Product Discounts',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stores.store', verbose_name='Store'),
        ),
    ]
