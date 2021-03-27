from django.shortcuts import render

def home(request):
    return render(request, "gifApp/home.html")

def login(request):
    return render(request, "gifApp/login.html")