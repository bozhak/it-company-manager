from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Worker, Position, Command


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name", "position"]
    list_filter = ["username", ]
    search_fields = ["username", "position__name"]


admin.site.register(Position)
admin.site.register(Command)


