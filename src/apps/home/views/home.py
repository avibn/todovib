from django.http.response import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'GET request! {request.user.username}')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')