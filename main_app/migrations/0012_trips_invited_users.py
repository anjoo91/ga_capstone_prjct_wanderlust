# Generated by Django 4.2.4 on 2023-08-26 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0011_trips_country_alter_destinations_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='invited_users',
            field=models.ManyToManyField(blank=True, related_name='invited_trips', to=settings.AUTH_USER_MODEL),
        ),
    ]
