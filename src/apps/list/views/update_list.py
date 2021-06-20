from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from src.apps.home.forms import CreateListForm

from ..models import TodoList


class UpdateListView(View):
    def get(self, request, list_id, *args, **kwargs):
        todolist = get_object_or_404(TodoList, pk=list_id, owner=request.user)
        context = {"form": CreateListForm(instance=todolist)}

        return render(request, "home/create_list.html", context)

    def post(self, request, list_id, *args, **kwargs):
        form = CreateListForm(request.POST)
        if form.is_valid():
            todolist = get_object_or_404(TodoList, pk=list_id, owner=request.user)
            todolist.name = form.cleaned_data["name"]
            todolist.description = form.cleaned_data["description"]
            todolist.save()

            return redirect(reverse("List:view", args=[list_id]))
        return HttpResponseBadRequest("Invalid form.")
