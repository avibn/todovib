from django.http.response import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request, id, *args, **kwargs):
        return HttpResponse(f'{id} :: GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')