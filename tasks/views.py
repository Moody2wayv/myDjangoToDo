# tasks/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    """
    Display the list of tasks for the logged-in user.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered HTML of the task list page.
    """
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    """
    Create a new task.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered HTML of the task creation form.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, task_id):
    """
    Update an existing task.

    Parameters:
    request (HttpRequest): The HTTP request object.
    task_id (int): The ID of the task to be updated.

    Returns:
    HttpResponse: The rendered HTML of the task update form.
    """
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    """
    Delete an existing task.

    Parameters:
    request (HttpRequest): The HTTP request object.
    task_id (int): The ID of the task to be deleted.

    Returns:
    HttpResponse: The rendered HTML of the task delete confirmation page.
    """
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
