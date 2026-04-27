from django.urls import path
from core.views import home_view
urlpatterns = [
    path("", home_view)
]

app_name = "core"
