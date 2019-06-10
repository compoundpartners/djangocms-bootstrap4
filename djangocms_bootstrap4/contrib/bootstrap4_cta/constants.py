# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CTA_LAYOUT_CHOICES = getattr(
    settings,
    'CTA_LAYOUT_CHOICES',
    (('', _('Configure this list in settings (CTA_LAYOUT_CHOICES)')),)
)
