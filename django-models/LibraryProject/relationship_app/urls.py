from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import your views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="authentication/logout.html"), name="logout"),
]

