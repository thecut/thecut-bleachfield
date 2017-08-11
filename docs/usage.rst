=====
Usage
=====


1. Add ``BleachField`` to your form(s), with a widget of your choosing:

    .. code-block:: python

      from ckeditor.widgets import CKEditorWidget
      from django import forms
      from thecut.bleachfield.forms import BleachField


      class MyForm(forms.Form):

          content = BleachField(widget=CKEditorWidget())


2. Optionally provide custom clean options for bleach:

    .. code-block:: python

          content = BleachField(
              clean_options={
                  'tags': ['a', 'p', 'strong', 'em'],
                  'attributes': {'a': ['href', 'target', 'rel']},
                  'styles': [],
              },
          )
