# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Boxout


class Bootstrap4BoxoutPlugin(CMSPluginBase):
    """
    Components > "Boxout" Plugin
    https://getbootstrap.com/docs/4.0/components/boxout/
    """
    model = Bootstrap4Boxout
    name = _('Boxout')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/boxout.html'
    change_form_template = 'djangocms_bootstrap4/admin/boxout.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'fluid',
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
        link_classes = ['boxout']
        if instance.fluid:
            link_classes.append('boxout-fluid')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4BoxoutPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4BoxoutPlugin)
