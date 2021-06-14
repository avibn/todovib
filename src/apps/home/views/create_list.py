from django.http.response import HttpResponse
from django.views import View

class CreateListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'CREATE LIST form.')

    def post(self, request, *args, **kwargs):
        return HttpResponse('CREATE list post req.')