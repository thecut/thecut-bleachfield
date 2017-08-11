# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.test import TestCase
from mock import patch
from thecut.bleachfield.forms import BleachField


class TestFormBleachField(TestCase):
    """Tests for :py:class:`thecut.bleachfield.forms.BleachField`."""

    @patch('bleach.clean')
    def test_calls_bleach_clean_when_form_is_validated(self, fake_clean):

        class BleachFieldForm(forms.Form):
            content = BleachField()

        form = BleachFieldForm(data={'content': 'content'})
        self.assertTrue(form.is_valid())

        # Enure bleach.clean() was actually called.
        fake_clean.assert_called_once_with('content')

    @patch('bleach.clean')
    def test_calls_bleach_clean_with_clean_options_kwarg_when_form_is_validated(self, fake_clean):  # noqa: E501
        custom_clean_options = {
            'tags': ['a', 'p', 'strong', 'em'],
            'attributes': {'a': ['href', 'target', 'rel']},
            'styles': [],
        }

        class BleachFieldForm(forms.Form):
            content = BleachField(clean_options=custom_clean_options)

        form = BleachFieldForm(data={'content': 'content'})
        self.assertTrue(form.is_valid())

        # Enure bleach.clean() was actually called with custom clean options.
        fake_clean.assert_called_once_with('content', **custom_clean_options)

    @patch('bleach.clean')
    def test_calls_bleach_clean_with_clean_options_attribute_when_form_is_validated(self, fake_clean):  # noqa: E501

        class CustomBleachField(BleachField):
            clean_options = {
                'tags': ['a'],
                'attributes': {'a': ['href']},
                'styles': [],
            }

        class BleachFieldForm(forms.Form):
            content = CustomBleachField()

        form = BleachFieldForm(data={'content': 'content'})
        self.assertTrue(form.is_valid())

        # Enure bleach.clean() was actually called with custom clean options
        # class attribute.
        fake_clean.assert_called_once_with('content',
                                           **CustomBleachField.clean_options)

    @patch('bleach.clean')
    def test_calls_bleach_clean_with_merged_clean_options_attribute_and_kwarg_when_form_is_validated(self, fake_clean):  # noqa: E501

        class CustomBleachField(BleachField):
            clean_options = {
                'tags': ['a'],
                'styles': [],
            }

        custom_clean_options = {'attributes': {'a': ['href']}}

        class BleachFieldForm(forms.Form):
            content = CustomBleachField(
                clean_options=custom_clean_options)

        form = BleachFieldForm(data={'content': 'content'})
        self.assertTrue(form.is_valid())

        # Enure bleach.clean() was actually called with custom clean options
        # class attribute.
        merged_clean_options = CustomBleachField.clean_options.copy()
        merged_clean_options.update(custom_clean_options)
        fake_clean.assert_called_once_with('content', **merged_clean_options)
