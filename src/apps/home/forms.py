from django.forms import ModelForm

from src.apps.list.models import TodoList


class CreateListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ("name", "description")
