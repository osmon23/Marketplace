# Generated by Django 4.2.3 on 2023-08-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Confirmation Code'),
        ),
    ]