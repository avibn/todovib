from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import ListItemForm
from ..models import ListItem, TodoList


class AddItemView(View):
    def get(self, request, list_id, *args, **kwargs):
        todolist = get_object_or_404(TodoList, pk=list_id, owner=request.user)
        context = {"form": ListItemForm, "list": todolist}

        return render(request, "list/add_item.html", context)

    def post(self, request, list_id, *args, **kwargs):
        get_object_or_404(TodoList, pk=list_id, owner=request.user)
        form = ListItemForm(request.POST)
        if form.is_valid():
            ListItem.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                todolist_id=list_id,
            )

            return redirect(reverse("List:view", args=[list_id]))
        return HttpResponseBadRequest("Invalid form.")
