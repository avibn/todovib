from django.http.response import HttpResponse
from django.views import View

class DeleteItemView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse('DELETE item post req.')