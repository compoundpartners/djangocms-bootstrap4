# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import forms

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_link.cms_plugins import LinkPlugin
from djangocms_bootstrap4.helpers import concat_classes, get_plugin_template

from .models import Bootstrap4Carousel, Bootstrap4CarouselSlide
from .constants import (
    CAROUSEL_DEFAULT_SIZE,
    CAROUSEL_TEMPLATE_CHOICES,
    CAROUSEL_SLIDE_TEMPLATE_CHOICES
)

class Bootstrap4CarouselForm(forms.ModelForm):

    carousel_style = forms.ChoiceField(CAROUSEL_TEMPLATE_CHOICES, required=False)

    class Meta:
        model = Bootstrap4Carousel
        fields = '__all__'


class Bootstrap4CarouselSlideForm(forms.ModelForm):

    carousel_style = forms.ChoiceField(CAROUSEL_SLIDE_TEMPLATE_CHOICES, required=False)

    class Meta:
        model = Bootstrap4CarouselSlide
        fields = '__all__'



class Bootstrap4CarouselPlugin(CMSPluginBase):
    """
    Components > "Carousel" Plugin
    https://getbootstrap.com/docs/4.0/components/carousel/
    """
    model = Bootstrap4Carousel
    name = _('Carousel')
    module = _('Bootstrap 4')
    allow_children = True
    child_classes = ['Bootstrap4CarouselSlidePlugin']
    form = Bootstrap4CarouselForm

    fieldsets = [
        (None, {
            'fields': (
                'carousel_style',
                ('carousel_interval', 'full_width'),
                ('carousel_controls', 'carousel_indicators'),
                ('carousel_keyboard', 'carousel_wrap'),
                ('carousel_ride', 'carousel_pause'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
                'carousel_aspect_ratio',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'carousel', 'carousel', [[instance.carousel_style]] if instance.carousel_style else CAROUSEL_TEMPLATE_CHOICES
        )

    def render(self, context, instance, placeholder):
        link_classes = ['carousel', 'slide']

        full_width = 'full-width' if instance.full_width else ''
        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
            full_width,
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CarouselPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4CarouselSlidePlugin(CMSPluginBase):
    """
    Components > "Carousel Slide" Plugin
    https://getbootstrap.com/docs/4.0/components/carousel/
    """
    model = Bootstrap4CarouselSlide
    name = _('Carousel slide')
    module = _('Bootstrap 4')
    allow_children = True
    parent_classes = ['Bootstrap4CarouselPlugin']
    form = Bootstrap4CarouselSlideForm

    fieldsets = [
        (None, {
            'fields': (
                'carousel_style',
                'carousel_image',
                'carousel_video',
                'carousel_video_url',
                'background_color',
                ('title', 'animate_title',),
                'carousel_content',
            )
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('link', 'internal_link'),
                ('mailto', 'phone'),
                ('anchor', 'target'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        parent = instance.parent.get_plugin_instance()[0]
        width = float(context.get('width') or CAROUSEL_DEFAULT_SIZE[0])
        height = float(context.get('height') or CAROUSEL_DEFAULT_SIZE[1])

        if parent.carousel_aspect_ratio:
            aspect_width, aspect_height = tuple(
                [int(i) for i in parent.carousel_aspect_ratio.split('x')]
            )
            height = width * aspect_height / aspect_width

        context['instance'] = instance
        context['link'] = instance.get_link()
        if not context['link']:
            context['link'] = instance.link
        context['options'] = {
            'crop': 10,
            'size': (width, height),
            'upscale': True
        }
        if instance.background_color:
            instance.attributes['style'] = 'background-color: %s;' % instance.background_color
        return context

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'carousel', 'slide', [[instance.carousel_style]] if instance.carousel_style else CAROUSEL_SLIDE_TEMPLATE_CHOICES
        )


plugin_pool.register_plugin(Bootstrap4CarouselPlugin)
plugin_pool.register_plugin(Bootstrap4CarouselSlidePlugin)
