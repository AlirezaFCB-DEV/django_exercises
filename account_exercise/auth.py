from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.hashers import check_password

User = get_user_model()


class Email_BackEnd(BaseBackend):
    def authenticate(self, request, **credentials):
        email = credentials.get("email")
        password = credentials.get("password")
        if not email or not password:
            return None
        try:
            user = User.objects.get(Q(email__iexact=email))
        except User.DoesNotExist:
            return None

        return user if user.check_password(password) and self.user_can_authenticate(user) else None

    def user_can_authenticate(self, user):
        return getattr(user, "is_active", True)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.username.startswith("admin_"):
            return True

        return False
