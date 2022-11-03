from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connections, transaction
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .models import User
# Create your views here.

def index(request):
    return render(request, "../templates/pickups/index.html")

#def home(request):
#    return render(request, "../templates/pickups/home.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("sports:index"))
        else:
            messages.error(request,"Invalid username or password.")
    else:
        return render(request=request, template_name="../templates/pickups/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("sports:index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "../templates/pickups/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "../templates/pickups/register.html", {
                "message": "Username already taken."
            })
        # login(request, user)
        return HttpResponseRedirect(reverse("sports:login_view"))
    else:
        return render(request, "../templates/pickups/register.html")