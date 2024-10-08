# Generated by Django 5.0.4 on 2024-06-28 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='trip_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trips',
            name='description_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
