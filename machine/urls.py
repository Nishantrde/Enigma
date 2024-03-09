from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("enigma", views.enigma, name="enigma"),
    path("logout_page", views.logout_page, name="logout_page"),
    path("register", views.register, name="register"),
]


