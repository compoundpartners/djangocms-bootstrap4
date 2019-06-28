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

from .models import Bootstrap4Modal

MODAL_TEMPLATES = getattr(
    settings,
    'DJANGOCMS_MODAL_TEMPLATES',
    (('', _('Configure this list in settings (DJANGOCMS_MODAL_TEMPLATES)')),)
)


class Bootstrap4ModalPlugin(CMSPluginBase):
    """
    Components > "Modal" Plugin
    https://getbootstrap.com/docs/4.0/components/modal/
    """
    model = Bootstrap4Modal
    name = _('Modal')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/modal/default/modal.html'
    TEMPLATE_NAME = 'djangocms_bootstrap4/modal/%s/modal.html'
    change_form_template = 'djangocms_bootstrap4/admin/modal.html'
    allow_children = True
    #child_classes = ['TextPlugin', 'Bootstrap4LinkPlugin', 'Bootstrap4PicturePlugin', 'Bootstrap4CollapsePlugin', 'FilePlugin']

    fieldsets = [
        (None, {
            'fields': (
                'title',
                'modal_id',
                'layout',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        link_classes = ['modal']

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])

        instance.attributes['class'] = classes

        return super(Bootstrap4ModalPlugin, self).render(
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
            kwargs['widget'].choices = MODAL_TEMPLATES
        return super(Bootstrap4ModalPlugin, self).formfield_for_choice_field(db_field, request, **kwargs)


plugin_pool.register_plugin(Bootstrap4ModalPlugin)
