from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, email=None, password=None, **extra_fields):
        if not phone:
            raise ValueError("Telefon raqami kiritilishi shart!")
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(phone, email, password, **extra_fields)


class CustomUser(AbstractUser, CustomUserManager):
    username = None
    phone = models.CharField(max_length=20, unique=True)
    profession = models.CharField(max_length=50)
    image = models.FileField(upload_to="accounts/")
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]
    
    objects = CustomUserManager()
    
    @property
    def fullname(self):
        return f'{self.first_name} {self._last_name}'
