from django.urls import path 

from . import views

app_name = "api"

urlpatterns = [
    path("state/", views.states_list, name="states_list")
]
