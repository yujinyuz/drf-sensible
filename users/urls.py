from django.urls import path

from . import apis

urlpatterns = [
    path("", apis.UserListApi.as_view(), name="list"),
    path("", apis.UserCreateApi.as_view(), name="create"),
    path("/me", apis.UserMeApi.as_view(), name="me"),
]
