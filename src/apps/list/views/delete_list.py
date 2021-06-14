from django.http.response import HttpResponse
from django.views import View


class DeleteListView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse('Delete list post req.')
