from django.urls import path
from .views import login_view

app_name = "auth"

urlpatterns = [
    path("login/", login_view, name='login'),
    path("register/", login_view, name='register'),
    path("logout", login_view, name='logout'),
]