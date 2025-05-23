from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """
    Модель пользователя
    """

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, verbose_name="Email пользователя")
    phone = PhoneNumberField(blank=True, verbose_name="Телефон пользователя")
    city = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Город пользователя"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар пользователя",
    )
    tg_nick = models.CharField(max_length=100, verbose_name="Telegram ник", unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
