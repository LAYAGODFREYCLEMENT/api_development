from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
            email = self.normalize_email
            user = self.model(email=email, **extra_fields)
            user.set_password(pasword)
            user.save(using=self._db)
            return user

    def super_user():
        pass
