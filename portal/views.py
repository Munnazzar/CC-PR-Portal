from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from mongoengine.errors import DoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("portal:admin-panel")

    message = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("portal:admin-panel")
            else:
                message = "Invalid username or password"
        except DoesNotExist:
            message = "Invalid username or password"

    return render(request, "login.html", {"msg": message})


def logout_view(request):
    logout(request)
    return redirect("portal:login-page")


@login_required(login_url="portal:login-page")
def adminPanel(request):
    return render(
        request,
        "adminPanel.html",
        {"count": DevDayAttendence.objects.count(), "events": Event.objects.all()},
    )


@login_required(login_url="portal:login-page")
def adminPanelSchedule(request):
    if not request.user.is_superuser:
        return redirect("portal:admin-panel")
    return render(request, "adminPanelSchedule.html")
