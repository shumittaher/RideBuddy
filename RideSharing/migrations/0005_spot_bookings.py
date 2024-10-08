# Generated by Django 5.0.4 on 2024-07-09 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0004_remove_trips_round_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spot_Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spots_requested', models.IntegerField()),
                ('approval_status', models.BooleanField()),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RideSharing.trips')),
            ],
        ),
    ]
