from django.http.response import HttpResponse
from django.views import View

class ViewList(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'LIST PAGE')