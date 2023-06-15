# from typing import Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import check_password

from django.db.models import Q

User = get_user_model()


class EmailOrUsernameBackend(BaseBackend):
    def authenticate(self, request, username="None", password="None"):
        try:
            user = User.objects.get(
                Q(username__exact=username) | Q(email__exact=username)
            )
            if user.check_password(password):
                return user
        except user.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
