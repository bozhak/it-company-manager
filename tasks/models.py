from django.db import models
from django.db.models import ForeignKey, ManyToManyField
from django.db.models.fields import CharField
from django.conf import settings


class TaskType(models.Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        URGENT = "URGENT", "Urgent"
        HIGH = "HIGH", "High"
        MEDIUM = "MEDIUM", "Medium"
        LOW = "LOW", "Low"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=10,
        choices=Priority,
        default=Priority.MEDIUM
    )

    task_type = ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    assignees = ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )

    def __str__(self):
        return (
            f"{self.name} {self.description} "
            f"{self.is_completed} {self.deadline} "
            f"{self.priority} {self.task_type} "
            f"{self.assignees}"
        )
