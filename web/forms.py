from django import forms

from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "task",
            "date",
            "time",
        ]

        widgets = {
            "task": forms.TextInput(attrs={"class": "form-control", }),
            "date": forms.TextInput(attrs={"class": "form-control", }),
            "time": forms.TextInput(attrs={"class": "form-control", }),
        }
