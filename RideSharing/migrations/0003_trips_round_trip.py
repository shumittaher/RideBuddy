# Generated by Django 5.0.4 on 2024-06-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0002_trips_trip_owner_alter_trips_description_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='round_trip',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
