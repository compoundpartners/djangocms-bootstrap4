# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.template import TemplateDoesNotExist
from django.template.loader import select_template

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Boxout

BOXOUT_TEMPLATES = getattr(
    settings,
    'DJANGOCMS_BOXOUT_TEMPLATES',
    (('', _('Configure this list in settings (DJANGOCMS_BOXOUT_TEMPLATES)')),)
)


class Bootstrap4BoxoutPlugin(CMSPluginBase):
    """
    Components > "Boxout" Plugin
    https://getbootstrap.com/docs/4.0/components/boxout/
    """
    model = Bootstrap4Boxout
    name = _('Boxout')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/boxout/default/boxout.html'
    TEMPLATE_NAME = 'djangocms_bootstrap4/boxout/%s/boxout.html'
    change_form_template = 'djangocms_bootstrap4/admin/boxout.html'
    allow_children = True
    #child_classes = ['TextPlugin', 'Bootstrap4LinkPlugin',
        #'Bootstrap4PicturePlugin', 'Bootstrap4CollapsePlugin',
        #'FilePlugin', 'PromoUnitPlugin']

    fieldsets = [
        (None, {
            'fields': (
                #'fluid',
                'title',
                'full_width',
                'background_color',
                'layout',
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
        if instance.full_width:
            link_classes.append('full-width')
        if instance.fluid:
            link_classes.append('boxout-fluid')
        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes
        if instance.background_color:
            instance.attributes['style'] = 'background: %s;' % instance.background_color

        return super(Bootstrap4BoxoutPlugin, self).render(
            context, instance, placeholder
        )

    def get_render_template(self, context, instance, placeholder):
        layout = instance.layout
        if layout:
            template = self.TEMPLATE_NAME % layout
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template


    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'layout':
            if not 'widget' in kwargs:
                kwargs['widget'] = forms.Select()
            kwargs['widget'].choices = BOXOUT_TEMPLATES
        return super(Bootstrap4BoxoutPlugin, self).formfield_for_choice_field(db_field, request, **kwargs)


plugin_pool.register_plugin(Bootstrap4BoxoutPlugin)
