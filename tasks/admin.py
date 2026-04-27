from django.contrib import admin
from tasks.models import TaskType, Task
from django.contrib.auth.admin import UserAdmin

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["priority", "name", "deadline", "is_completed", "task_type"]
    list_filter = ["name", "task_type", "priority", "deadline", "is_completed"]
    search_fields = ["name", "task_type__name"]


admin.site.register(TaskType)


