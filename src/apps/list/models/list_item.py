from .list import TodoList
from django.db import models


class ListItem(models.Model):
    name = models.TextField(max_length=50, help_text="The name of the item.")
    description = models.TextField(
        max_length=318, null=True, blank=True, help_text="The description of the item."
    )
    # tags, MANY TO MANY
    todolist = models.ForeignKey(
        TodoList,
        on_delete=models.CASCADE,
        help_text="The list of the item.",
        related_name="items",
    )
    completed = models.BooleanField(
        default=False, help_text="The completion status of the task."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item name: {self.name}"

    def __repr__(self) -> str:
        return f"<ListItem name='{self.name}' owner='{self.owner.username}'>"
