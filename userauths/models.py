from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length = 100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="userauths_user_set",  # Add this line
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="userauths_user_set",  # Add this line
        verbose_name="user permissions",
    )
