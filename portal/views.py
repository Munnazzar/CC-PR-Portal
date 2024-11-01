from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from mongoengine.errors import DoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', block=True)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("portal:admin-panel")

    message = ""
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Attempt to sign user in
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("portal:admin-panel")
            else:
                message = "Invalid username or password."
        else:
            message = "Invalid username or password."
    return render(request, "login.html", {"login_form": login_form, "msg": message})

@login_required(login_url="portal:login-page")
def logout_view(request):
    logout(request)
    return redirect("portal:login-page")


@login_required(login_url="portal:login-page")
def adminPanel(request):
    return render(
        request,
        "adminPanel.html",
        {"count": DevDayAttendance.objects.count(), "events": Event.objects.all()},
    )


@login_required(login_url="portal:login-page")
def adminPanelSchedule(request):
    if not request.user.is_superuser:
        return redirect("portal:admin-panel")
    return render(request, "adminPanelSchedule.html")

def page_not_found_404(request, exception=404):
    return render(
        request,
        "404.html",
        status=404,
    )

def limit_exceeded_403(request, exception=403):
    return render(
        request,
        "403.html",
        status=403,
    )
