from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import ListItemForm
from ..models import ListItem, TodoList


class UpdateItemView(View):
    def get(self, request, list_id, item_id, *args, **kwargs):
        todolist = get_object_or_404(TodoList, pk=list_id, owner=request.user)
        item = get_object_or_404(ListItem, pk=item_id, todolist=todolist)
        context = {"form": ListItemForm(instance=item), "list": todolist, "item": item}

        return render(request, "list/add_item.html", context)

    def post(self, request, list_id, item_id, *args, **kwargs):
        form = ListItemForm(request.POST)
        if form.is_valid():
            item = get_object_or_404(
                ListItem, pk=item_id, todolist_id=list_id, todolist__owner=request.user
            )
            item.name = form.cleaned_data["name"]
            item.description = form.cleaned_data["description"]
            item.save()

            return redirect(reverse("List:view", args=[list_id]))
        return HttpResponseBadRequest("Invalid form.")
