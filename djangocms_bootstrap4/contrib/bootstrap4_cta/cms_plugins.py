# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Cta


class Bootstrap4CtaPlugin(CMSPluginBase):
    """
    Components > "Cta" Plugin
    https://getbootstrap.com/docs/4.0/components/cta/
    """
    model = Bootstrap4Cta
    name = _('Call To Action')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/cta.html'
    change_form_template = 'djangocms_bootstrap4/admin/cta.html'
    allow_children = True
    child_classes = ['TextPlugin', 'Bootstrap4LinkPlugin', 'FilePlugin']

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
                'background_color',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        link_classes = ['cta']
        if instance.fluid:
            link_classes.append('cta-fluid')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes
        if instance.background_color:
            instance.attributes['style'] = 'background: %s;' % instance.background_color

        return super(Bootstrap4CtaPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4CtaPlugin)
