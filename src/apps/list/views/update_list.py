from django.http.response import HttpResponse
from django.views import View

class UpdateListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'UPDATE LIST form.')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Update list post req.')