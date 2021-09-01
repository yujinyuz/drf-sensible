from typing import Dict, Optional

from django.db import models

from .filters import UserFilter
from .models import User


def user_create(
    *, email: str, is_active: bool = True, password: Optional[str] = None
) -> User:
    user = User.objects.create_user(email=email, is_active=is_active, password=password)

    return user


# -------- Selectors --------
def user_list(*, filters=None) -> models.QuerySet:
    filters = filters or {}

    qs = User.objects.all()

    return UserFilter(filters, qs).qs


def user_get_login_data(*, user: User) -> Dict:
    return {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "is_superuser": user.is_superuser,
    }
