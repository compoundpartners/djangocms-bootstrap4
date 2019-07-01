# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils import six
from django.utils.safestring import mark_safe
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _

from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.forms import ValidationError


def concat_classes(classes):
    """
    merges a list of classes and return concatinated string
    """
    return ' '.join(_class for _class in classes if _class)


def get_plugin_template(instance, prefix, name, templates):
    template = templates[0][0]
    try:
        select_template(['djangocms_bootstrap4/{}/{}/{}.html'.format(prefix, template, name)])
    except TemplateDoesNotExist:
        # TODO render a warning inside the template
        template = 'default'

    return 'djangocms_bootstrap4/{}/{}/{}.html'.format(prefix, template, name)


# use mark_safe_lazy to delay the translation when using mark_safe
# otherwise they will not be added to /locale/
# https://docs.djangoproject.com/en/1.11/topics/i18n/translation/#other-uses-of-lazy-in-delayed-translations
mark_safe_lazy = lazy(mark_safe, six.text_type)
