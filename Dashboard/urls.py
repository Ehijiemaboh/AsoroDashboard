from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("individuals", views.individuals, name="individuals"),
    path("mechanics", views.mechanics, name="mechanics"),
    path("messages", views.messages, name="messages"),
    path("settings", views.settings, name="settings"),
    path("support", views.support, name="support"),
    
]
