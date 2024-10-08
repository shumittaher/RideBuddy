# Generated by Django 5.0.4 on 2024-08-09 14:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0005_spot_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot_bookings',
            name='requester_comments',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spot_bookings',
            name='spots_requested',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
