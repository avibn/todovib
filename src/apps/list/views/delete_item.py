from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from ..models import ListItem


class DeleteItemView(View):
    def post(self, request, list_id, item_id, *args, **kwargs):
        item = get_object_or_404(
            ListItem, pk=item_id, todolist_id=list_id, todolist__owner=request.user
        )
        item.delete()

        return redirect(reverse("List:view", args=[list_id]))
