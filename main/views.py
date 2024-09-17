from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpRequest, HttpResponse


def show_main(request):
    context = {"npm": "2306123456", "name": "Pak Bepe", "class": "PBP E"}

    return render(request, "main.html", context)


def register(request: HttpRequest) -> HttpResponse:
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")

    context = {"form": form}
    return render(request, "register.html", context)
