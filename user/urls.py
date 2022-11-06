from django.contrib import admin
from django.urls import path,include
from . import views

# Uygulama oluşturduktan sonra URL için app_name kullanmak zorundasın.

app_name = "user"

# User uygulaması URL'leri
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

]