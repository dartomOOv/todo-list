from django import forms

from todo_list.models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple()
        }
