from django.http.response import HttpResponse
from django.views import View

class AddItemView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Add item to list FORM.')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Create item post req.')