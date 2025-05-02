from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, "Dashboard/index.html")

def individuals(request):
    return render (request, "Dashboard/individuals.html")

def mechanics(request):
    return render (request, "Dashboard/mechanics.html")

def messages(request):
    return render (request, "Dashboard/messages.html")

def settings(request):
    return render (request, "Dashboard/settings.html")

def support(request):
    return render (request, "Dashboard/support.html")