# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


CODE_TYPE_CHOICES = (
    ('code', _('Inline code')),
    ('pre', _('Code block')),
    ('var', _('Variables')),
    ('kbd', _('User input')),
    ('samp', _('Sample output')),
)
HIDE_BLACKQUOTE_ALIGNMENT = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_HIDE_BLACKQUOTE_ALIGNMENT',
    False
)
