from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

try:
    def index(request):
          return render(request, "Dashboard/index.html", {})
except:
    "View error"

