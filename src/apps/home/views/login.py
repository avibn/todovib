from django.http.response import HttpResponse
from django.views import View

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Log in form.')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Log in post req.')