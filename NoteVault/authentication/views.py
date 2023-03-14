from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RegisterForm

# Create your views here.
from .models import CustomUser


def home(request):
    return render(request, "home.html")


def login_user(request):
    if request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("password")
        if x := authenticate(password=password, username=email):
            login(request, x)
            return render(request, "home.html")
    return render(request, "login.html")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
        return render(request, "register.html", {"errors": form.errors.items})
    return render(request, "register.html", {"register_form": RegisterForm()})
