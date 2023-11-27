from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoices(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    """User model."""
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )

    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.USER,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    confirmation_code = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        default='XXXXX'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == RoleChoices.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == RoleChoices.MODERATOR

    @property
    def is_user(self):
        return self.role == RoleChoices.USER

    @property
    def is_admin_or_moderator(self):
        return self.is_admin or self.is_moderator
