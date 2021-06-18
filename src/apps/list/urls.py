from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

app_name = "List"
urlpatterns = [
    path("", login_required(ViewList.as_view()), name="view"),
    path("update/", login_required(UpdateListView.as_view()), name="update"),
    path("delete/", login_required(DeleteListView.as_view()), name="delete"),

    path("item/add/", login_required(AddItemView.as_view()), name="add_item"),
    path(
        "item/<int:item_id>/update/",
        login_required(UpdateItemView.as_view()),
        name="update_item",
    ),
    path(
        "item/<int:item_id>/delete/",
        login_required(DeleteItemView.as_view()),
        name="delete_item",
    ),
]
