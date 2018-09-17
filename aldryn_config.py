# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):

    grid_size = forms.NumberField(
        'Maximum columns to support, default is 12.',
        required=False
    )
    enable_icons = forms.CheckboxField(
        'Enable icon support',
        required=False,
        initial=True,
    )
    enable_jumbotron = forms.CheckboxField(
        'Enable Jumbotron support',
        required=False,
        initial=True,
    )
    enable_cta = forms.CheckboxField(
        'Enable CTA support',
        required=False,
        initial=True,
    )
    enable_boxout = forms.CheckboxField(
        'Enable Boxout support',
        required=False,
        initial=True,
    )
    available_colors = forms.CharField(
        'Available colors',
        required=False,
    )

    def to_settings(self, data, settings):
        if data['grid_size']:
            settings['DJANGOCMS_BOOTSTRAP4_GRID_SIZE'] = int(data['grid_size'])

        if data['enable_icons']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ICONS'] = int(data['enable_icons'])

        if data['enable_jumbotron']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_JUMBOTRON'] = int(data['enable_jumbotron'])

        if data['enable_cta']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_CTA'] = int(data['enable_cta'])

        if data['enable_boxout']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_BOXOUT'] = int(data['enable_boxout'])

        if data['available_colors']:
            settings['DJANGOCMS_BOOTSTRAP4_AVAILABLE_COLORS'] = data['available_colors'].split(",")

        return settings
