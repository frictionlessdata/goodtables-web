# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import (current_app as app, views, jsonify, request, render_template,
                   redirect, flash)
from flask.ext.babel import gettext as _
from . import exceptions


class BaseView(views.MethodView):

    """Defines the interface for all views.

    BaseView provides handlers for:

    * View access control based on the permissions of the current user
     * A message flashing/passing interface based on user actions
    * Content negotiation for json or full page response objects

    All views in the application should inherit from this view,
    overriding/extending as appropriate.

    """

    _template_ = ''
    _forms_ = {}
    _success_url_ = None
    _is_xhr_ = False

    def __init__(self, **kwargs):
        # set self.flash_categories on init as we need an app/request context
        self.flash_categories = self.get_flash_categories()

        # self.is_xhr can be set explicitly; otherwise detect from request
        self.is_xhr = self._is_xhr_ or request.is_xhr

    def dispatch_request(self, **kwargs):
        """Prepare data and validate access for all requests."""

        # Get the data for this request
        data = self.data(**kwargs)

        # Validate access for this request
        valid = self.validate_access(data, **kwargs)
        if not valid:
            return exceptions.unauthorized(request.is_xhr)

        return super(BaseView, self).dispatch_request(data, **kwargs)

    def data(self, **kwargs):
        """Populates the request context with data."""
        return {}

    def validate_access(self, data, **kwargs):
        """Provides the access policy for this user/view via a boolean return.

        The default implementation returns True for GET requests, and False
        for POST requests.

        Use this method on conjunction with the login_required decorator to
        protect all views.

        """

        # if request.method == 'GET':
        #     return True
        # return False
        return True

    def options(self, **kwargs):
        """Sets the OPTIONS method on the response headers."""
        return app.make_default_options_response()

    def get(self, data, **kwargs):
        """Handler for GET requests."""
        return self.response(**data)

    def post(self, data, **kwargs):
        """Handler for POST requests."""
        return self.response(**data)

    def put(self, data, **kwargs):
        """Handler for PUT requests."""
        return exceptions.method_not_allowed(request.is_xhr)

    def delete(self, data, **kwargs):
        """Handler for DELETE requests."""
        return exceptions.method_not_allowed(request.is_xhr)

    def get_success_url(self, **data):
        """Returns the URL for redirection on success."""
        return self._success_url_ or request.base_url

    def get_flash_categories(self):
        """Returns the available message flash categories."""
        return app.config['TABULAR_VALIDATOR_FLASH_CATEGORIES']

    def response(self, msg=None, msg_cat=None, success=False, **data):
        """Returns the response object for the request."""
        return self._prepared_response(msg=msg, msg_cat=msg_cat,
                                       success=success, **data)

    def _prepared_response(self, msg=None, msg_cat=None, success=False, **data):
        """Prepares the response object to be returned.

        This method performs content negotiation, based on whether the
        request is XHR or not (supported for POST requests only).
        If the request is XHR, then a json response object is returned.
        Else, a standard full page response is returned.
        """

        if self.is_xhr:
            if request.method in ('POST', 'PUT', 'PATCH'):
                serializable = {
                    'success': success,
                    # 'msg': msg,
                    # 'msg_cat': msg_cat,
                    'data': data
                }
            else:
                serializable = data
            response = jsonify(**serializable)

        else:
            if msg:
                flash(msg, msg_cat)
            if success:
                response = redirect(self.get_success_url(**data))
            else:
                response = render_template(self._template_, **data)

        return response


class APIView(BaseView):

    """Provides common logic for all API views."""

    _is_xhr_ = True
    _required_args_ = ()
    _optional_args_ = ()
    _type_map_ = {
        'null': None,
        'true': True,
        'false': False
    }

    def _translate_types(self, arguments):
        for k, v in arguments.items():
            if self._type_map_.get(v):
                arguments[k] = self._type_map_.get(v)
        return arguments

    def _ensure_args(self):
        # TODO: this.
        # if self._required_args_:
        #     for arg in self._required_args_:
        #     if not request.args.get(arg):
        #         # return exceptions.bad_request(self.is_xhr)
        #         pass
        pass

    def _process_args(self):
        allowed_args = self._required_args_ + self._optional_args_
        if allowed_args:
            arguments = dict([(arg, request.args.get(arg)) for arg in
                              allowed_args if request.args.get(arg)])
            return self._translate_types(arguments)
        else:
            return dict([])

    def data(self, **kwargs):
        data = super(APIView, self).data(**kwargs)
        processed_args = self._process_args()
        return data
