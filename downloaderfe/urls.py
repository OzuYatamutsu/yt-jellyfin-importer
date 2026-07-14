from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("start/", views.start_job, name="start"),
    path("status/<int:job_id>/", views.status, name="status"),
]

