from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import *

app_name = "Home"
urlpatterns = [
    path("", login_required(HomeView.as_view()), name="index"),
    path("list/create/", login_required(CreateListView.as_view()), name="create_list"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
]
