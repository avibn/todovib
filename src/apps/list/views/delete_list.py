from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from ..models import TodoList


class DeleteListView(View):
    def post(self, request, list_id, *args, **kwargs):
        todolist = get_object_or_404(TodoList, pk=list_id, owner=request.user)
        todolist.delete()

        return redirect(reverse("Home:index"))
