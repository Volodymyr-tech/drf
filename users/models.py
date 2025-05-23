from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# from materials.models import Course, Lesson


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True)
    username = models.CharField(
        max_length=155, null=True, blank=True, verbose_name="Username"
    )
    city = models.CharField(
        max_length=20,
        verbose_name="Where do you live?",
        help_text="Choose a city",
        null=True,
        blank=True,
    )

    objects = CustomUserManager()  # Используем кастомный менеджер

    USERNAME_FIELD = "email"  # Указываем email вместо username
    REQUIRED_FIELDS = [
        "username",
    ]  # Поля, которые нужно запросить при создании суперюзера

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class Payments(models.Model):

    CASH = "cash"
    TRANSFER = "transfer"

    STATUS_CHOICES = [
        (CASH, "Cash"),  # data for admin panel
        (TRANSFER, "Transfer"),
    ]

    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="payments"
    )
    pay_data = models.DateTimeField(auto_now_add=True)
    payed_course = models.ForeignKey(
        "materials.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="payments",
    )
    payed_lesson = models.ForeignKey(
        "materials.Lesson",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="payments",
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    payment_type = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        blank=True,
        null=True,
    )
    link = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["-pay_data"]

    def __str__(self):
        return f"Payment for {self.user} - {self.amount} USD"
