from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)

    return render(request, 'add_task.html', {'form': form})
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')
def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.status = True
    task.save()
    return redirect('/')
tasks = Task.objects.all().order_by('-id')