# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_icon.fields

from ..constants import LINK_ALIGNMENTS


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_link', '0002_add_icons'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4link',
            name='link_alignment',
            field=models.CharField(blank=True, choices=LINK_ALIGNMENTS, max_length=255, verbose_name='Alignment'),
        ),
    ]
