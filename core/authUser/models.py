from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, passage_user_id, password=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um email")

        email = self.normalize_email(email)

        user = self.model(
            id=uuid.uuid4(),
            email=email,
            passage_user_id=passage_user_id,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, passage_user_id="admin", password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, passage_user_id, password, **extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    passage_user_id = models.CharField(max_length=255, unique=True)

    name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["passage_user_id"]

    def __str__(self):
        return self.email