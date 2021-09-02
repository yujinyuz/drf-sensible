from django.core.exceptions import ValidationError

from rest_framework import exceptions as rest_exceptions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.errors import get_error_message


class ApiAuthMixin:
    """
    Equivalent of `DEFAULT_PERMISSION_CLASSSES`
    """

    authentication_classes = (
        JWTAuthentication,
        SessionAuthentication,
    )
    permission_classes = (IsAuthenticated,)


class ApiErrorsMixin:
    """
    Mixin that transforms Django and Python exceptions into rest_framework ones.
    without the mixin, they return 500 status code which is not desired.
    """

    expected_exceptions = {
        ValueError: rest_exceptions.ValidationError,
        ValidationError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied,
    }

    def handle_exception(self, exc):

        if isinstance(exc, (rest_exceptions.ValidationError)):
            exc.status_code = 422

        if isinstance(exc, tuple(self.expected_exceptions.keys())):
            drf_exception_class = self.expected_exceptions[exc.__class__]  # type: ignore
            drf_exception = drf_exception_class(get_error_message(exc))

            return super().handle_exception(drf_exception)  # type: ignore

        return super().handle_exception(exc)  # type: ignore
