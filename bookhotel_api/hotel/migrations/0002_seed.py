# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from hotel.models import Hotel


def run(apps, schema_editor):
    Hotel.objects.bulk_create([
        Hotel(
            name='Lakewood',
            excellence_rating=3,
            rate_week_regular=110,
            rate_week_loyalty=80,
            rate_weekend_regular=90,
            rate_weekend_loyalty=80,
        ),
        Hotel(
            name='Bridgewood',
            excellence_rating=4,
            rate_week_regular=160,
            rate_week_loyalty=110,
            rate_weekend_regular=60,
            rate_weekend_loyalty=50,
        ),
        Hotel(
            name='Ridgewood',
            excellence_rating=5,
            rate_week_regular=220,
            rate_week_loyalty=100,
            rate_weekend_regular=150,
            rate_weekend_loyalty=40,
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(run)
    ]
