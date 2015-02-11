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


class RunForm(Form):
    data_url = fields.StringField(validators=[validators.URL(),
                                              OnlyIfNot('data_file'),
                                              validators.Optional()])
    schema_url = fields.StringField(validators=[validators.URL(),
                                                OnlyIfNot('schema_file'),
                                                validators.Optional()])
    data_file = fields.FileField(validators=[OnlyIfNot('data_url'),
                                             validators.Optional()])
    schema_file = fields.FileField(validators=[OnlyIfNot('schema_url'),
                                               validators.Optional()])
