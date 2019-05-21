# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import js_color_picker.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_tabs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4tab',
            name='background_color',
            field=js_color_picker.fields.RGBColorField(blank=True, colors={'#0067A5': 'Dark Blue', '#009fe3': 'Blue', '#0A80C7': 'Medium Blue', '#2D9CDE': 'Light Blue', '#34BCE1': 'Sky', '#545454': 'Dark Grey', '#68C0B5': 'Teal', '#69CCE7': 'Light Sky', '#6d6d6d': 'Grey', '#8FD1E9': 'Very Light Sky', '#96D0C9': 'Light Teal', '#999': 'Light Grey', '#9B8DA5': 'Purple', '#B8AEBF': 'Light Purple', '#BBE9E4': 'Very Light Teal', '#C6BDCB': 'Very Light Purple', '#F2F2F2': 'Very Light Grey', '#F8EB91': 'Yellow', '#FEF4B4': 'Light Yellow', '#FF0000': 'White'}, mode='both', null=True, verbose_name='Background Color'),
        ),
        migrations.AddField(
            model_name='bootstrap4tab',
            name='full_width',
            field=models.BooleanField(default=False, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='bootstrap4tab',
            name='show_title',
            field=models.BooleanField(default=False, verbose_name='Show Title'),
        ),
        migrations.AddField(
            model_name='bootstrap4tab',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Full Width'),
        ),
    ]
