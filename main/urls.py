from django.urls import path
from main.views import show_main, register

app_name = "main"

urlpatterns = [
    path("", show_main, name="main"),
    path("register/", register, name="register"),
]
