from django.contrib import admin

from .models import TodoList, ListItem

admin.site.register(TodoList)
admin.site.register(ListItem)
