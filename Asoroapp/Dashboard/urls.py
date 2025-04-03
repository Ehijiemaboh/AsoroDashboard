from django.urls import path
from . import views

try:
    urlpatterns = [
    path("", views.index, name="index")
]
except:
    "path error"

