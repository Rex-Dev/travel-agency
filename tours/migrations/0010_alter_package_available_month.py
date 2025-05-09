# Generated by Django 5.1.4 on 2025-02-12 16:02

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_alter_package_available_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='available_month',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December'), (13, 'Every Month')], default='1', max_length=29),
        ),
    ]
