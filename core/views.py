from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from tasks.models import Task


@login_required
def home_view(request):
    num_users = get_user_model().objects.count()
    num_tasks = Task.objects.count()
    num_is_done = 1

    context = {
        "num_users": num_users,
        "num_tasks": num_tasks,
        "num_is_done": num_is_done,
    }

    return render(request, "pages/home.html", context=context)