from django.contrib.auth.views import LoginView


class LoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True
