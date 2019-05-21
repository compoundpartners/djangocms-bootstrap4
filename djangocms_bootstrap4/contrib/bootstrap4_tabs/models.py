# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import TagTypeField, AttributesField
from js_color_picker.fields import RGBColorField

from .constants import (
    TAB_TEMPLATE_CHOICES,
    TAB_TYPE_CHOICES,
    TAB_ALIGNMENT_CHOICES,
    TAB_EFFECT_CHOICES,
)


@python_2_unicode_compatible
class Bootstrap4Tab(CMSPlugin):
    """
    Components > "Navs - Tab" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        null=True,
        blank=True,
    )
    show_title = models.BooleanField(
        verbose_name=_('Show title'),
        default=False,
    )
    full_width = models.BooleanField(
        verbose_name=_('Full Width'),
        default=False,
    )
    background_color = RGBColorField(
        verbose_name=_('Background Color'),
        blank=True,
        null=True
    )
    tab_style = models.CharField(
        verbose_name=_('Template'),
        choices=TAB_TEMPLATE_CHOICES,
        default=TAB_TEMPLATE_CHOICES[0][0],
        max_length=255,
        help_text=_('This is the template that will be used for the component.'),
    )
    tab_type = models.CharField(
        verbose_name=_('Type'),
        choices=TAB_TYPE_CHOICES,
        default=TAB_TYPE_CHOICES[0][0],
        max_length=255,
    )
    tab_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=TAB_ALIGNMENT_CHOICES,
        blank=True,
        max_length=255,
    )
    tab_index = models.PositiveIntegerField(
        verbose_name=_('Index'),
        null=True,
        blank=True,
        help_text=_('Index of element to open on page load starting at 1.'),
    )
    tab_effect = models.CharField(
        verbose_name=_('Animation effect'),
        choices=TAB_EFFECT_CHOICES,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return self.title or str(self.pk)

    def get_short_description(self):
        if self.title:
            return self.title
        text = '({}) '.format(self.tab_type)

        if self.tab_alignment:
            text += '.{}'.format(self.tab_alignment)
        return text


@python_2_unicode_compatible
class Bootstrap4TabItem(CMSPlugin):
    """
    Components > "Navs - Tab Item" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    tab_title = models.CharField(
        verbose_name=_('Tab title'),
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return self.tab_title
