from django.urls import path

from . import views

app_name = "ghana"
urlpatterns = [
    path("study_sites", views.study_sites, name="study_sites"),
]
