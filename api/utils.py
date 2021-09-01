import typing

# from drf_spectacular.openapi import AutoSchema
from rest_framework import serializers


def create_serializer_class(name, fields):
    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    serializer_class = create_serializer_class(name="", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)


# class CustomAutoSchema(AutoSchema):
#     def get_request_serializer(self) -> typing.Any:
#         serializer = getattr(self.view, "InputSerializer", None)

#         if serializer:
#             return serializer()

#         return None

#     def get_response_serializers(self) -> typing.Any:
#         serializer = getattr(self.view, "OutputSerializer", None)
#         if serializer:
#             return serializer()
#         return None

#     def _get_paginator(self):
#         pagination_class = getattr(self.view, "Pagination", None)
#         if pagination_class:
#             return pagination_class()
#         return None

#     def _get_filter_parameters(self):
#         return super()._get_filter_parameters()

#     def _get_serializer_name(self, serializer, direction):
#         return self._view.__class__.__name__ + serializer.__class__.__name__
