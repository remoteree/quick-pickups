from django.urls import path
from django.contrib import admin

from . import views

app_name = "sports"

urlpatterns = [
    path("", views.index, name="index"),
    #path("home", views.home, name="home"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("admin", admin.site.urls)
]