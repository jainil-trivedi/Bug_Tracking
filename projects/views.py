from django.shortcuts import render, redirect, get_object_or_404
from core.models import Project, Module, User
from .forms import ProjectForm, ModuleForm
from dashboards.decorators import role_required

# Create your views here.

#project view:-

@role_required(allowed_roles=['admin','manager'])
def projectListView(request):
    projects = Project.objects.all()
    return render(request,'projects/project_list.html',{'projects': projects})


@role_required(allowed_roles=['admin','manager'])
def projectCreateView(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
        else:
            return render(request,'projects/project_create.html',{'form': form})
    else:
        form = ProjectForm()
        return render(request,'projects/project_create.html',{'form': form})


@role_required(allowed_roles=['admin','manager'])
def projectDetailView(request, id):
    project = get_object_or_404(Project, id=id)
    modules = Module.objects.filter(project=project)
    return render(request,'projects/project_detail.html',{'project': project, 'modules': modules})


@role_required(allowed_roles=['admin','manager'])
def projectEditView(request, id):
    project = get_object_or_404(Project,id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
        else:
            return render(request,'projects/project_edit.html',{'form': form,'project': project})
    else:
        form = ProjectForm(instance=project)
        return render(request,'projects/project_edit.html',{'form': form,'project': project})


@role_required(allowed_roles=['admin','manager'])
def projectDeleteView(request, id):
    project = get_object_or_404(Project,id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request,'projects/project_delete.html',{'project': project})
