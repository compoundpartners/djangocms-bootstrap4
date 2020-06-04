# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_link.models import AbstractLink
from djangocms_icon.fields import Icon
from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES
from js_color_picker.fields import RGBColorField

from .constants import LINK_CHOICES, LINK_SIZE_CHOICES, LINK_ALIGNMENTS

from .validators import LocalORIntranetURLValidator

# 'link' type is added manually as it is only required for this plugin
COLOR_STYLE_CHOICES = (
    ('link', _('Link')),
) + COLOR_STYLE_CHOICES


@python_2_unicode_compatible
class Bootstrap4Link(AbstractLink):
    """
    Components > "Button" Plugin
    https://getbootstrap.com/docs/4.0/components/buttons/
    """
    url_validators = [
        LocalORIntranetURLValidator(),
    ]

    external_link = models.CharField(
        verbose_name=_('External link'),
        blank=True,
        max_length=2040,
        validators=url_validators,
        help_text=_('Provide a link to an external source.'),
    )
    link_type = models.CharField(
        verbose_name=_('Type'),
        choices=LINK_CHOICES,
        default=LINK_CHOICES[0][0],
        max_length=255,
        help_text=_('Adds either the .btn-* or .text-* classes.'),
    )
    link_color = RGBColorField(
        verbose_name=_('Color'),
        blank=True,
        null=True
    )
    link_context = models.CharField(
        verbose_name=_('Context'),
        choices=COLOR_STYLE_CHOICES,
        blank=True,
        max_length=255,
    )
    link_size = models.CharField(
        verbose_name=_('Size'),
        choices=LINK_SIZE_CHOICES,
        blank=True,
        max_length=255,
    )
    link_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=LINK_ALIGNMENTS,
        blank=True,
        max_length=255,
    )
    link_outline = models.BooleanField(
        verbose_name=_('Outline'),
        default=False,
        help_text=_('Applies the .btn-outline class to the elements.'),
    )
    link_block = models.BooleanField(
        verbose_name=_('Block'),
        default=False,
        help_text=_('Extends the button to the width of its container.'),
    )
    modal_id = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('Modal Id'),
        help_text=_('Do not include a preceding "#" symbol.'),
    )
    icon_left = Icon(
        verbose_name=_('Icon left'),
    )
    icon_right = Icon(
        verbose_name=_('Icon right'),
    )
    no_link = models.BooleanField(
        verbose_name=_('No Link'),
        default=False,
    )


    def __str__(self):
        return str(self.pk)

    def get_link(self):
        if self.no_link:
            return ''
        return super(Bootstrap4Link, self).get_link()

    def clean(self):
        if not self.no_link:
            super(Bootstrap4Link, self).clean()
