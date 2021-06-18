from django.http.response import HttpResponse
from django.views import View

class SignupView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Sign up form.')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Sign up post req.')