from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "To do"
        IN_PROGRESS = "in_progress", "In progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=Status,
        default=Status.TODO
    )

    execution_status = models.IntegerField(default=0)

    github_link = models.CharField(max_length=255, null=True, blank=True)
    solution_link = models.CharField(max_length=255, null=True, blank=True)

    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks"
    )


class Archive(models.Model):
    project = models.ManyToManyField(
        Project,
        related_name="archives",
    )

    worker = models.ForeignKey(
    settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="archives"
    )

    archived_at = models.DateTimeField(auto_now_add=True)

