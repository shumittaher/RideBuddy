# Generated by Django 5.0.4 on 2024-09-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0013_alter_messages_underlying_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
    ]
