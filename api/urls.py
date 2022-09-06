from django.urls import path
from .views import apihome

urlpatterns = [
    path('',apihome, name = "list-create"),
]