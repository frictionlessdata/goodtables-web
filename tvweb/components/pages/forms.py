# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from werkzeug.datastructures import FileStorage
from flask_wtf import Form
from wtforms import fields
from wtforms import validators
from flask.ext.babel import gettext as _


class OnlyIfNot(object):

    """Field can have value only if not value in `match`."""

    def __init__(self, match=None, message=None):
        if match is None:
            raise ValueError
        self.match = match
        if not message:
            message = _('Cannot have a value if {0} has a value'.format(match))
        self.message = message

    def __call__(self, form, field):
        match = form.data.get(self.match)
        if match:
            if isinstance(field.data, FileStorage) and not field.data.filename:
                pass
            else:
                raise validators.ValidationError(self.message)


data_url_args = {
    'validators': [validators.URL(), OnlyIfNot('data_file'), validators.Optional()],
    'description': {
        'placeholder': 'Add your data source here.',
        'hint': ''
    }
}
data_file_args = data_url_args.copy()
data_file_args['validators'] = [OnlyIfNot('data_url'), validators.Optional()]
schema_url_args = {
    'validators': [validators.URL(), OnlyIfNot('schema_file'), validators.Optional()],
    'description': {
        'placeholder': 'Add your schema source here.',
        'hint': ''
    }
}
schema_file_args = schema_url_args.copy()
schema_file_args['validators'] = [OnlyIfNot('schema_url'), validators.Optional()]
format_args = {
    'choices': [('csv', 'CSV'), ('excel', 'Excel')], #, ('json', 'JSON')],
    'description': {
        'placeholder': 'CSV',
        'hint': ''
    }
}
with_schema_args = {
    'label': 'Add a schema?',
    'description': {
        'hint': ''
    }
}
schema_eg_args = {
    'choices': [
        ('', '-- Presets --'),
        ('https://raw.githubusercontent.com/okfn/tabular-validator/master/examples/hmt/spend-publishing-schema.json', 'HMT Spend Publishing'),
        ('https://raw.githubusercontent.com/okfn/tabular-validator/master/examples/hmt/bis-modified.json', 'BIS Modified')
    ],
    'description': {
        'placeholder': 'HMT Spend',
        'hint': ''
    }
}
fail_fast_args = {
    'label': 'Fail fast?',
    'description': {
        'hint': ''
    }
}
ignore_empty_rows_args = {
    'label': 'Ignore empty rows?',
    'description': {
        'hint': ''
    }
}
encoding_args = {
    'label': 'File encoding',
    'choices': [('', '-- Auto --'), ('utf-8', 'UTF-8'), ('ascii', 'ASCII'), ('ISO-8859-2', 'ISO-8859-2')],
    'description': {
        'hint': ''
    }
}


class RunForm(Form):
    data_url = fields.StringField(**data_url_args)
    data_file = fields.FileField(**data_file_args)
    format = fields.SelectField(**format_args)
    with_schema = fields.BooleanField(default=False, **with_schema_args)
    schema_url = fields.StringField(**schema_url_args)
    schema_file = fields.FileField(**schema_file_args)
    schema_eg = fields.SelectField(**schema_eg_args)
    fail_fast = fields.BooleanField(default=True, **fail_fast_args)
    encoding = fields.SelectField(**encoding_args)
    ignore_empty_rows = fields.BooleanField(default=False, **ignore_empty_rows_args)
