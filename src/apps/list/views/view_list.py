from django.shortcuts import get_object_or_404, render
from django.views import View

from ..models import TodoList


class ViewList(View):
    def get(self, request, list_id, *args, **kwargs):
        todolist = get_object_or_404(TodoList, pk=list_id, owner=request.user)
        all_lists = TodoList.objects.filter(owner=request.user)
        context = {"list": todolist, "all_lists": all_lists}

        return render(request, "list/view_list.html", context)
