from django.views.generic import ListView
from src.apps.list.models import TodoList


class HomeView(ListView):
    context_object_name = "lists"
    template_name = "home/index.html"

    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user)
