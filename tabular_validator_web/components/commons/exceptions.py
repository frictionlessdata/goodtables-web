"""Custom HTTP exception classes. Content-negotiation compatible."""
from flask import jsonify, render_template
from flask.ext.babel import gettext as _


def unauthorized(is_xhr):
    return Unauthorized(is_xhr=is_xhr).response()


def permission_denied(is_xhr):
    return PermissionDenied(is_xhr=is_xhr).response()


def bad_request(is_xhr):
    return BadRequest(is_xhr=is_xhr).response()


def not_found(is_xhr):
    return NotFound(is_xhr=is_xhr).response()


def method_not_allowed(is_xhr):
    return MethodNotAllowed(is_xhr=is_xhr).response()


class BaseHTTPException(Exception):
    """Base handler class for content-negotiated HTTP not found errors."""

    status_code = None

    def __init__(self, is_xhr=False):
        Exception.__init__(self)
        self.msg = ''
        self.msg_cat = ''
        self.is_xhr = is_xhr

    def serializable(self):
        serializable = {
            'msg': self.msg,
            'msg_cat': self.msg_cat,
            'status_code': self.status_code
        }
        return serializable

    def response(self):
        if self.is_xhr:
            response = jsonify(**self.serializable())
            response.status_code = self.status_code
        else:
            response = render_template('404.html', **self.serializable())
        return response


class BadRequest(BaseHTTPException):
    """Handler class for HTTP bad request errors."""

    status_code = 400

    def __init__(self, is_xhr=False):
        super(BadRequest, self).__init__(is_xhr=is_xhr)
        self.msg = _('Something is wrong with the request data.')
        self.msg_cat = 'danger'


class Unauthorized(BaseHTTPException):
    """Handler class for HTTP unauthorized errors."""

    status_code = 401

    def __init__(self, is_xhr=False):
        super(Unauthorized, self).__init__(is_xhr=is_xhr)
        self.msg = _('You are unauthorized to access this resource.')
        self.msg_cat = 'danger'


class PermissionDenied(BaseHTTPException):
    """Handler class for HTTP permission denied errors."""

    status_code = 403

    def __init__(self, is_xhr=False):
        super(PermissionDenied, self).__init__(is_xhr=is_xhr)
        self.msg = _('You are not permitted to access this resource.')
        self.msg_cat = 'danger'


class NotFound(BaseHTTPException):
    """Handler class for HTTP not found errors."""

    status_code = 404

    def __init__(self, is_xhr=False):
        super(NotFound, self).__init__(is_xhr=is_xhr)
        self.msg = _('The page you were looking for cannot be found.')
        self.msg_cat = 'danger'


class MethodNotAllowed(BaseHTTPException):
    """Handler class for HTTP method not allowed errors."""

    status_code = 405

    def __init__(self, is_xhr=False):
        super(MethodNotAllowed, self).__init__(is_xhr=is_xhr)
        self.msg = _('The HTTP method used is not supported on this view.')
        self.msg_cat = 'danger'
