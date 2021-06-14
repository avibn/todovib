from django.http.response import HttpResponse
from django.views import View

class UpdateItemView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Update item FORM')

    def post(self, request, *args, **kwargs):
        return HttpResponse('update item post REQ')