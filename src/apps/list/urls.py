from django.urls import path

from .views import *

app_name = 'List'
urlpatterns = [
    path('', ViewList.as_view(), name="view"),
    path('update/', UpdateListView.as_view(), name="update"),
    path('delete/', DeleteListView.as_view(), name="delete"),

    path('item/add/', AddItemView.as_view(), name="add_item"),
    path('item/<int:item_id>/update/', UpdateItemView.as_view(), name="update_item"),
    path('item/<int:item_id>/delete/', DeleteItemView.as_view(), name="delete_item"),
]
