# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-06 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_carousel', '0003_bootstrap4carouselslide_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4carousel',
            name='full_width',
            field=models.BooleanField(default=False, verbose_name='Show Full Width'),
        ),
    ]
