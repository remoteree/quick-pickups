from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connections, transaction

from .models import User
# Create your views here.

def index(request):
    return render(request, "../templates/pickups/index.html")