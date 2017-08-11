# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import bleach
from django.forms import CharField

from . import settings


class BleachField(CharField):

    clean_options = settings.DEFAULT_CLEAN_OPTIONS

    def __init__(self, *args, **kwargs):
        clean_options = kwargs.pop('clean_options', {})
        self._clean_options = self.clean_options.copy()
        self._clean_options.update(clean_options)
        super(BleachField, self).__init__(*args, **kwargs)

    def get_clean_options(self):
        return self._clean_options

    def to_python(self, value):
        return bleach.clean(value, **self.get_clean_options())
