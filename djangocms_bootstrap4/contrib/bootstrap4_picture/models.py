# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from cms.models import CMSPlugin

from djangocms_picture.models import AbstractPicture
from filer.fields.file import FilerFileField


@python_2_unicode_compatible
class Bootstrap4Picture(AbstractPicture):
    """
    Content > "Image" Plugin
    https://getbootstrap.com/docs/4.0/content/images/
    """
    picture_fluid = models.BooleanField(
        verbose_name=_('Responsive'),
        default=True,
        help_text=_('Adds the .img-fluid class to make the image responsive.'),
    )
    picture_rounded = models.BooleanField(
        verbose_name=_('Rounded'),
        default=False,
        help_text=_('Adds the .rounded class for round corners.'),
    )
    picture_thumbnail = models.BooleanField(
        verbose_name=_('Thumbnail'),
        default=False,
        help_text=_('Adds the .img-thumbnail class.'),
    )
    svg = FilerFileField(
        verbose_name=_('SVG Image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )


    def __str__(self):
        return str(self.pk)

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey, it's required to copy over
        # the reference from the instance to the new plugin.
        self.picture = oldinstance.picture
        self.svg = oldinstance.svg

    def get_short_description(self):
        if self.external_picture:
            return self.external_picture
        if self.picture and self.picture.label:
            return self.picture.label
        if self.svg and self.svg.label:
            return self.svg.label
        return _('<file is missing>')

    def clean(self):
        # there can be only one link type
        if self.link_url and self.link_page_id:
            raise ValidationError(
                ugettext(
                    'You have given both external and internal links. '
                    'Only one option is allowed.'
                )
            )

        # you shall only set one image kind
        if not self.picture and not self.external_picture and not self.svg:
            raise ValidationError(
                ugettext(
                    'You need to add either an image, svg image '
                    'or a URL linking to an external image.'
                )
            )

        # certain cropping options do not work together, the following
        # list defines the disallowed options used in the ``clean`` method
        invalid_option_pairs = [
            ('use_automatic_scaling', 'use_no_cropping'),
            ('use_automatic_scaling', 'thumbnail_options'),
            ('use_no_cropping', 'use_crop'),
            ('use_no_cropping', 'use_upscale'),
            ('use_no_cropping', 'thumbnail_options'),
            ('thumbnail_options', 'use_crop'),
            ('thumbnail_options', 'use_upscale'),
        ]
        # invalid_option_pairs
        invalid_option_pair = None

        for pair in invalid_option_pairs:
            if getattr(self, pair[0]) and getattr(self, pair[1]):
                invalid_option_pair = pair
                break

        if invalid_option_pair:
            message = ugettext(
                'Invalid cropping settings. '
                'You cannot combine "{field_a}" with "{field_b}".'
            )
            message = message.format(
                field_a=self._meta.get_field(invalid_option_pair[0]).verbose_name,
                field_b=self._meta.get_field(invalid_option_pair[1]).verbose_name,
            )
            raise ValidationError(message)

    @property
    def is_responsive_image(self):
        if self.svg:
            return False
        super().is_responsive_image

    @property
    def img_src(self):
        if self.svg:
            return self.svg.url
        elif self.external_picture:
            return self.external_picture
        elif self.picture and self.use_no_cropping:
            return self.picture.url
        elif not self.picture:
            return ''
        return super().img_src
