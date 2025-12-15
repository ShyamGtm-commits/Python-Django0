import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm
from django.views import View
from django.contrib.auth.decorators import login_required


# Create your views here.



# def task_list(request):
#     tasks = Tasks.objects.all()
#     return render(request, 'tasks/task_list.html',{'tasks': tasks})

class task_list(View):
    def get(self, request):
            tasks = Tasks.objects.all()
            return render(request, 'tasks/task_list.html',{'tasks': tasks})

# def task_detail(request, pk):
#     task = get_object_or_404(Tasks, pk=pk)
#     return render(request, 'tasks/task_detail.html', {'task': task})

class task_detail(View):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        return render(request, 'tasks/task_detail.html', {'task': task})
    
class BannerPageView(View):
    def get(self, request, pk=None):  
            task = get_object_or_404(Tasks, pk=pk)
            return render(request, "tasks/task_page.html", {"task": task})

    


# # creating a new task
# def task_create(request):
    
#     form = TaskForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('task_list')
#     return render(request, 'tasks/form.html', {'form': form})

class task_create(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'tasks/form.html', {'form': form})
          
    def post(self, request):
        form = TaskForm(request.POST , request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            form.save()
            return redirect('tasks:task_list')
        return render(request, 'tasks/form.html', {'form': form})

# # now for updation of the tasks 
# def task_update(request, pk):
#     task = get_object_or_404(Tasks, pk=pk)
#     form = TaskForm(request.POST or None, instance = task)
#     if form.is_valid():
#         form.save()
#         return redirect('task_list')
#     return render(request, 'tasks/form.html', {'form': form})

class task_update(View):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'tasks/form.html', {'form': form})

    def post(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        form = TaskForm(request.POST or None, request.FILES, instance = task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
        return render(request, 'tasks/form.html', {'form': form})
     

# def task_delete(request, pk):
#     task = get_object_or_404(Tasks, pk=pk)
#     if request.method == "POST":
#         task.delete()
#         return redirect('task_list')
#     return render(request, 'tasks/confirm_delete.html', {'task': task})

class task_delete(View):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        return render(request, 'tasks/confirm_delete.html', {'task': task})
    
    def post(self, request, pk):
            task = get_object_or_404(Tasks, pk=pk)
            task.delete()
            return redirect('tasks:task_list')

@login_required(login_url="/users/login")       
def task_new(request):
    if request.method == 'POSt':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_new.html')
