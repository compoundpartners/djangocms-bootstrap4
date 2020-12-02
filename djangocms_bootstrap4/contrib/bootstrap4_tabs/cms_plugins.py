# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import get_plugin_template, concat_classes

from .constants import TAB_TEMPLATE_CHOICES
from .models import Bootstrap4Tab, Bootstrap4TabItem


class Bootstrap4TabPlugin(CMSPluginBase):
    """
    Components > "Navs - Tab" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    model = Bootstrap4Tab
    name = _('Tabs')
    module = _('Bootstrap 4')
    change_form_template = 'djangocms_bootstrap4/admin/tabs.html'
    allow_children = True
    child_classes = ['Bootstrap4TabItemPlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('title', 'show_title'),
                'background_color',
                ('tab_type', 'tab_alignment'),
                ('tab_index', 'tab_effect'),
                'full_width',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tab_style',
                'tag_type',
                'attributes',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'tabs', 'tabs', [[instance.tab_style]] if instance.tab_style else TAB_TEMPLATE_CHOICES
        )

    def render(self, context, instance, placeholder):
        full_width = 'full-width' if instance.full_width else ''
        classes = concat_classes([
            full_width,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        styles = instance.attributes.get('style', '').split(' ')
        if instance.background_color:
            styles.append('background: %s;' % instance.background_color)
        instance.attributes['style'] = ' '.join(styles)

        return super(Bootstrap4TabPlugin, self).render(
            context, instance, placeholder
        )



class Bootstrap4TabItemPlugin(CMSPluginBase):
    """
    Components > "Navs - Tab Item" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    model = Bootstrap4TabItem
    name = _('Tab item')
    module = _('Bootstrap 4')
    change_form_template = 'djangocms_bootstrap4/admin/tabs.html'
    allow_children = True
    parent_classes = ['Bootstrap4TabPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'tab_title',
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

    def get_render_template(self, context, instance, placeholder):
        parent = instance.parent.get_plugin_instance()[0]
        return get_plugin_template(
            instance, 'tabs', 'item', [[parent.tab_style]] if parent.tab_style else TAB_TEMPLATE_CHOICES
        )


plugin_pool.register_plugin(Bootstrap4TabPlugin)
plugin_pool.register_plugin(Bootstrap4TabItemPlugin)
