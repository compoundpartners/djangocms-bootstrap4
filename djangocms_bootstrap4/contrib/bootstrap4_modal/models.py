# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from js_color_picker.fields import RGBColorField

from djangocms_bootstrap4.fields import TagTypeField, AttributesField

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
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)
