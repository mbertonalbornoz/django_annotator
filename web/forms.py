from django import forms

from .models import Tarea


# class TareaForm(forms.Form):
#     tarea = forms.CharField(label="Tarea:", max_length=140)
#     dia = forms.DateField(label="Día:")
#     hora = forms.TimeField(label="Hora:")


class TareaModelForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            "tarea",
            "dia",
            "hora",
        ]

        widgets = {
            "tarea": forms.TextInput(
                attrs={"class": "form-control", "class": "col-md-4",}
            ),
            "dia": forms.TextInput(
                attrs={"class": "form-control", "class": "col-md-4",}
            ),
            "hora": forms.TextInput(
                attrs={"class": "form-control", "class": "col-md-4",}
            ),
        }
