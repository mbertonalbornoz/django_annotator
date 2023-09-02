from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskModelForm


# Create your views here.
def home(request):
    form = TaskModelForm()
    context = {
        "tasks": Task.objects.all(),
        "form": form,
    }
    return render(request, template_name="web/index.html", context=context)


def create_task(request):

    form = TaskModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = TaskModelForm()

    return redirect("/")


def delete_task(request, pk):

    Task.objects.filter(id=pk).delete()

    return redirect("/")
