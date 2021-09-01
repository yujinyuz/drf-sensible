from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from api.mixins import ApiAuthMixin, ApiErrorsMixin
from api.pagination import LimitOffsetPagination, get_paginated_response

from . import services
from .models import User


class UserCreateApi(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.CharField()
        password = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = (
                "id",
                "email",
            )

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response()


class UserListApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        # Important: If we use BooleanField, it will default to False
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = (
                "id",
                "email",
            )

    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = services.user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self,
        )


class UserMeApi(ApiAuthMixin, APIView):
    def get(self, request):
        data = services.user_get_login_data(user=request.user)

        return Response(data)
