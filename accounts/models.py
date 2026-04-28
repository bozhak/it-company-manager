from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Command(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)

    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commands"
    )

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        blank=True,
        null=True
    )

    command = models.ForeignKey(
        Command,
        on_delete=models.CASCADE,
        related_name="workers",
        blank=True,
        null=True
    )

    is_leader = models.BooleanField(default=False)