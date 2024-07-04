from django.urls import path
from . import views

urlpatterns = [
    path("enigma", views.enigma),
    path("", views.doc),
]


