from django.shortcuts import render, redirect, get_object_or_404
from core.models import Task, Module, User
from .forms import TaskForm
from dashboards.decorators import role_required


# Create your views here.

@role_required(allowed_roles=['admin','manager'])
def taskListView(request):
    if request.user.role =='admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(module__project__manager=request.user)
    return render(request,'tasks/task_list.html',{'tasks': tasks})


@role_required(allowed_roles=['admin','manager'])
def taskCreateView(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            modules = Module.objects.all()
            developers = User.objects.filter(role='developer')
            return render(request,'tasks/task_create.html',{'form':form,'modules':modules,'developers':developers})
    else:
        form = TaskForm()
        modules = Module.objects.all()
        developers = User.objects.filter(role='developer')
        return render(request,'tasks/task_create.html',{'form':form,'modules':modules,'developers':developers})


@role_required(allowed_roles=['admin','manager','developer','tester'])
def taskDetailView(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request,'tasks/task_detail.html',{'task':task})


@role_required(allowed_roles=['admin','manager'])
def taskEditView(request, id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            modules = Module.objects.all()
            developers = User.objects.filter(role='developer')
            return render(request,'tasks/task_edit.html',{'form':form,'task':task,'modules':modules,'developers':developers})
    else:
        form = TaskForm(instance=task)
        modules = Module.objects.all()
        developers = User.objects.filter(role='developer')
        return render(request,'tasks/task_edit.html',{'form':form,'task':task,'modules': modules, 'developers': developers})


@role_required(allowed_roles=['admin','manager'])
def taskDeleteView(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'tasks/task_delete.html',{'task':task})
