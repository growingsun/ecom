# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mineral', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
