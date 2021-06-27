from django.contrib.auth.models import User
from django.db import models


class TodoList(models.Model):
    name = models.TextField(max_length=50, help_text="The name of the list.")
    description = models.TextField(
        max_length=318, null=True, blank=True, help_text="The description of the list."
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The owner of the list.",
        related_name="lists",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Todo list title: {self.name}"

    def __repr__(self) -> str:
        return f"<TodoList name='{self.name}' owner='{self.owner.username}'>"
