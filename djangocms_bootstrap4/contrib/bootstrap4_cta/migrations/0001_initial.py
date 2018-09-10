# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-15 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_bootstrap4.fields

from djangocms_bootstrap4.constants import TAG_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Cta',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_cta_bootstrap4cta', serialize=False, to='cms.CMSPlugin')),
                ('fluid', models.BooleanField(default=False, help_text='Adds the .cta-fluid class.', verbose_name='Fluid')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
