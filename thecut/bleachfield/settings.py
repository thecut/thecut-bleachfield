# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings


DEFAULT_CLEAN_OPTIONS = getattr(
    settings, 'BLEACHFIELD_DEFAULT_CLEAN_OPTIONS', {})
