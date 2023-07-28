from django import forms
from django.forms import NumberInput

from catalog.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(label="Deadline", required=False, widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ["name", "content", "deadline", "tags"]
