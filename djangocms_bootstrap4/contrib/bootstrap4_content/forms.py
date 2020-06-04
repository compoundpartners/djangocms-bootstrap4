# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import Textarea
from django.utils.text import slugify

from .constants import BLOCKQUOTE_LAYOUTS

BLOCKQUOTE_LAYOUT_CHOICES = BLOCKQUOTE_LAYOUTS
if len(BLOCKQUOTE_LAYOUT_CHOICES) == 0 or len(BLOCKQUOTE_LAYOUT_CHOICES[0]) != 2:
    BLOCKQUOTE_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + BLOCKQUOTE_LAYOUTS)), ('default',) + BLOCKQUOTE_LAYOUTS)


class Bootstrap4CodeForm(forms.ModelForm):


    class Meta:
        # When used inside djangocms-text-ckeditor
        # this causes the label field to be prefilled with the selected text.
        widgets = {
            'code_content': Textarea(attrs={'class': 'js-ckeditor-use-selected-text'}),
        }


class BootstrapBlockquoteForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=BLOCKQUOTE_LAYOUT_CHOICES, required=False)
