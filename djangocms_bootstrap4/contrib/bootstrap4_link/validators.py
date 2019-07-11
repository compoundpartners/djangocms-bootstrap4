# -*- coding: utf-8 -*-
import re

from djangocms_link.validators import IntranetURLValidator


class LocalORIntranetURLValidator(IntranetURLValidator):

    def __call__(self, value):
        if not value.startswith('/'):
            super().__call__(value)
