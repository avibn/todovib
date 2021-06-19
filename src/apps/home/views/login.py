from django.http.response import HttpResponse
from django.views import View
from django.contrib.auth import views as auth_views

class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True