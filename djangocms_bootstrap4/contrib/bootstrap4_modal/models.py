# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from js_color_picker.fields import RGBColorField

from djangocms_bootstrap4.fields import TagTypeField, AttributesField

PERSENTAGES = (
    ('', 'default'),
    ('5', '5%'),
    ('25', '25%'),
    ('50', '50%'),
    ('75', '75%'),
    ('90', '90%'),
    ('100', '100%'),
)


COOKIE_SETTINGS = (
    ('', 'Show every time (default)'),
    ('once-per-session', 'Cap at one view per session'),
    ('once-ever', 'Show once ever'),
)

@python_2_unicode_compatible
class Bootstrap4Modal(CMSPlugin):
    """
    Components > "Modal" Plugin
    https://getbootstrap.com/docs/4.0/components/modal/
    """
    title = models.CharField(
        verbose_name=_('Title'),
        null=True,
        blank=True,
        max_length=255,
    )
    modal_id = models.CharField(
        verbose_name=_('Modal ID'),
        null=False,
        blank=True,
        max_length=255,
    )
    layout = models.CharField(
        verbose_name=_('Layout'),
        blank=True,
        max_length=255,
        help_text=_('Select a layout'),
    )
    percentage_scrolled = models.CharField(
        verbose_name=_('Percentage Scrolled'),
        blank=True,
        default='',
        max_length=255,
        choices=PERSENTAGES,
    )
    seconds_passed = models.PositiveSmallIntegerField(
        verbose_name=_('Seconds Passed'),
        blank=True,
        null=True,
    )
    cookie_settings = models.CharField(
        verbose_name=_('Cookie settings'),
        blank=True,
        default='',
        max_length=255,
        choices=COOKIE_SETTINGS,
    )
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)
