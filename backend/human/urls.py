from django.urls import path, re_path

from . import views

app_name = "human"

urlpatterns = [
    path("", views.human_list, name="list"),
    path("<str:username>/", views.human_detail, name="detail"),
]
