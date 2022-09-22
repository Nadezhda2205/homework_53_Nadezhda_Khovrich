from django.shortcuts import render, redirect
from tasks.models import Task
from django.core.handlers.wsgi import WSGIRequest
from tasks.services.config import CHOICES
import datetime


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'choices': CHOICES
    }
    return render(request=request, template_name='index.html', context=context)


def add_view(request:WSGIRequest):
    if request.method == 'POST':
        task_data = {
            'header': request.POST.get('header'),
            'status': request.POST.get('status'),
            'deadline': request.POST.get('deadline')
        }

        Task.objects.create(**task_data)
        return redirect('/')
    context = {
        'choices': CHOICES
    }    
    return render(request=request, template_name='add.html', context=context)


def edit_view(request: WSGIRequest):
    if request.method == 'POST':
        pk = request.GET.get('pk')
        task: Task = Task.objects.get(pk=pk)
        task.header = request.POST.get('header')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.save()
        return redirect('/')

    pk = request.GET.get('pk')
    task: Task = Task.objects.get(pk=pk)
    task.deadline = datetime.datetime.strftime(task.deadline, '%Y-%m-%d')
    context = {
        'task': task,
        'choices': CHOICES
    }
    return render(request=request, template_name='edit.html', context=context)


def delete_view(request):
    pk = request.GET.get('pk')
    Task.objects.filter(pk=pk).delete()
    return redirect('/')


def about_view(request):
    return render(request=request, template_name='about.html')
