# Generated by Django 5.1.4 on 2025-02-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0014_alter_booking_amt_alter_booking_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment_address',
            field=models.CharField(max_length=250),
        ),
    ]
