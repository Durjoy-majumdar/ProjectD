from django.contrib import admin
from django.urls import path, include
from .views import sample, login

urlpatterns = [
    path('', sample, name="sample"),
    path('login', login, name='login'),
]