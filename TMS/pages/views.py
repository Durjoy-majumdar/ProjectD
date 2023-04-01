from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def sample(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')