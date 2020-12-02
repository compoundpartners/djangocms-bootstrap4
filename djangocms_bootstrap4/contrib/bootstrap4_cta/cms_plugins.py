# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
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
    change_form_template = 'djangocms_bootstrap4/admin/cta.html'

    #Template handling
    render_template = 'djangocms_bootstrap4/cta.html'  # The default fallback template
    TEMPLATE_NAME = 'djangocms_bootstrap4/cta{separator}{variant}.html'

    def get_render_template(self, context, instance, placeholder):
        if instance.layout:
            separator = '__'
            template = self.TEMPLATE_NAME.format(separator=separator, variant=instance.layout)
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template
    # End template handling

    allow_children = True
    child_classes = ['TextPlugin', 'Bootstrap4LinkPlugin', 'FilePlugin']

    fieldsets = [
        (None, {
            'fields': (
                'layout',
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

        styles = instance.attributes.get('style', '').split(' ')
        if instance.background_color:
            styles.append('background: %s;' % instance.background_color)
        instance.attributes['style'] = ' '.join(styles)

        return super(Bootstrap4CtaPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4CtaPlugin)
