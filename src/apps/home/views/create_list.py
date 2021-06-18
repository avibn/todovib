from django.http.response import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from src.apps.list.models import TodoList

from ..forms import CreateListForm


class CreateListView(View):
    def get(self, request, *args, **kwargs):
        context = {"form": CreateListForm}
        return render(request, "home/create_list.html", context)

    def post(self, request, *args, **kwargs):
        form = CreateListForm(request.POST)
        if form.is_valid():
            TodoList.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                owner=request.user,
            )

            return redirect(reverse("Home:index"))
        return HttpResponseBadRequest("Invalid form.")
