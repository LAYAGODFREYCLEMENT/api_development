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

    def create_superUser(self, email, password=None, **extra_fields):
        user = self.create(
            email,
            password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superUser = True
        user.save(using=self._db)
