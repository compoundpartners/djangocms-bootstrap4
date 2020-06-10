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
    enable_row_bg_color = forms.CheckboxField(
        'Enable row background color',
        required=False,
        initial=True,
    )
    enable_row_bg_image = forms.CheckboxField(
        'Enable row background image',
        required=False,
        initial=True,
    )
    enable_row_bg_video = forms.CheckboxField(
        'Enable row background Video',
        required=False,
        initial=False,
    )
    enable_row_icon = forms.CheckboxField(
        'Enable row icon',
        required=False,
        initial=False,
    )
    enable_row_alignment = forms.CheckboxField(
        'Enable row alignment controls',
        required=False,
        initial=True,
    )
    enable_row_tag_type = forms.CheckboxField(
        'Enable Row Tag type',
        required=False,
        initial=False,
    )
    enable_row_gutter = forms.CheckboxField(
        'Enable Row Gutter control',
        required=False,
        initial=False,
    )
    enable_col_bg_color = forms.CheckboxField(
        'Enable col background color',
        required=False,
        initial=True,
    )
    enable_col_bg_image = forms.CheckboxField(
        'Enable col background image',
        required=False,
        initial=True,
    )
    show_button_context = forms.CheckboxField(
        'Show Context for Links/Buttons',
        required=False,
        initial=False,
    )
    enable_carousel_slide_title_anim = forms.CheckboxField(
        'Enable Carousel Slide title animation',
        required=False,
        initial=False,
    )
    enable_carousel_slide_video_bg = forms.CheckboxField(
        'Enable Carousel Slide video background',
        required=False,
        initial=False,
    )
    enable_carousel_slide_animate_title = forms.CheckboxField(
        'Enable Carousel Animate title',
        required=False,
        initial=False,
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

        if data['available_colors']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_'] = data['available_colors'].split(",")

        if data['enable_row_bg_color']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ROW_BG_COLOR'] = int(data['enable_row_bg_color'])

        if data['enable_row_bg_image']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ROW_BG_IMAGE'] = int(data['enable_row_bg_image'])

        if data['enable_row_bg_video']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ROW_BG_VIDEO'] = int(data['enable_row_bg_video'])

        if data['enable_row_icon']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ROW_ICON'] = int(data['enable_row_icon'])

        if data['enable_row_alignment']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ROW_ALIGNMENT'] = int(data['enable_row_alignment'])

        if data['enable_row_tag_type']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ROW_TAG_TYPE'] = int(data['enable_row_tag_type'])

        if data['enable_row_gutter']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_ROW_GUTTER'] = int(data['enable_row_gutter'])

        if data['enable_col_bg_color']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_COL_BG_COLOR'] = int(data['enable_col_bg_color'])

        if data['enable_col_bg_image']:
            settings['DJANGOCMS_BOOTSTRAP4_USE_COL_BG_IMAGE'] = int(data['enable_col_bg_image'])

        if data['show_button_context']:
            settings['DJANGOCMS_BOOTSTRAP4_SHOW_BUTTON_CONTEXT'] = int(data['show_button_context'])

        if data['enable_carousel_slide_title_anim']:
            settings['DJANGOCMS_BOOTSTRAP4_CAROUSEL_SLIDE_TITLE_ANIM'] = int(data['enable_carousel_slide_title_anim'])

        if data['enable_carousel_slide_video_bg']:
            settings['DJANGOCMS_BOOTSTRAP4_CAROUSEL_SLIDE_VIDEO_BG'] = int(data['enable_carousel_slide_video_bg'])

        if data['enable_carousel_slide_animate_title']:
            settings['DJANGOCMS_BOOTSTRAP4_ENABLE_CAROUSEL_SLIDE_ANIMATE_TITLE'] = int(data['enable_carousel_slide_animate_title'])

        return settings
