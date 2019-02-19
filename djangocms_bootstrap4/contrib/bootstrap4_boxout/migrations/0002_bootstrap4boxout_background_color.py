# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-19 06:47
from __future__ import unicode_literals

from django.db import migrations
import js_color_picker.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_boxout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4boxout',
            name='background_color',
            field=js_color_picker.fields.RGBColorField(blank=True, null=True, verbose_name='Background Color'),
        ),
    ]
