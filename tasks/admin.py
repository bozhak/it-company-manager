from django.contrib import admin
from tasks.models import TaskType, Task, Archive, Project
from django.contrib.auth.admin import UserAdmin

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "deadline", "created_at", "task_type"]
    list_filter = ["title", "status", "created_at", "task_type"]
    search_fields = ["title", "task_type__name"]

admin.register(Archive)
admin.register(Project)
admin.site.register(TaskType)


