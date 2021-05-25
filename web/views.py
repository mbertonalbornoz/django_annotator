import datetime

from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaModelForm

# Create your views here.
def home(request):
    form = TareaModelForm()
    context = {
        "tareas": Tarea.objects.all(),
        "form": form,
    }
    return render(request, template_name="web/index.html", context=context)


def crear_tarea(request):

    form = TareaModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = TareaModelForm()

    context = {
        "tareas": Tarea.objects.all(),
        "form": form,
    }

    return render(request, "web/index.html", context=context)


def borrar_tarea(request, pk):

    Tarea.objects.filter(id=pk).delete()

    return redirect("/")
