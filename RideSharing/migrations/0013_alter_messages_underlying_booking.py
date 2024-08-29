# Generated by Django 5.0.4 on 2024-08-29 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0012_alter_messages_underlying_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='underlying_booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RideSharing.spot_bookings'),
        ),
    ]
