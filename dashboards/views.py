from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from core.models import Project, Bug, Module, User , Task

# Create your views here.
#@login_required(login_url="login")
@role_required(allowed_roles=["admin"])
def adminDashboardView(request):
    projects = Project.objects.all()
    total_projects = projects.count()
    total_users = User.objects.count()
    total_tasks = Task.objects.count()

    for project in projects:
        project.total_tasks = Task.objects.filter(module__project=project).count()

    return render(request, "dashboards/admin_dashboard.html", {'projects': projects,'total_projects': total_projects,'total_users': total_users,'total_tasks': total_tasks,})

#@login_required(login_url="login")
@role_required(allowed_roles=["manager"])
def managerDashboardView(request):
    projects = Project.objects.filter(manager=request.user)
    my_projects = projects.count()
    total_modules = Module.objects.filter(project__manager=request.user).count()
    total_tasks = Task.objects.filter(module__project__manager=request.user).count()

    for project in projects:
        project.total_tasks = Task.objects.filter(module__project=project).count()
        project.pending_tasks = Task.objects.filter(module__project=project, status='Pending').count()

    return render(request, "dashboards/manager_dashboard.html",{'projects': projects,'my_projects': my_projects,'total_modules': total_modules,'total_tasks': total_tasks,})

#@login_required(login_url="login")
@role_required(allowed_roles=["developer"])
def developerDashboardView(request):
    from core.models import Task, Bug, TimeLog
    assigned_tasks = Task.objects.filter(assigned_to=request.user)
    total_tasks = assigned_tasks.count()
    total_bugs = Bug.objects.filter(assigned_to=request.user).count()
    total_timelogs = TimeLog.objects.filter(developer=request.user).count()
    pending_tasks = assigned_tasks.filter(status='Pending').count()
    return render(request, "dashboards/developer_dashboard.html", {'assigned_tasks': assigned_tasks,'total_tasks': total_tasks,'total_bugs': total_bugs,'total_timelogs': total_timelogs,'pending_tasks': pending_tasks,})

#@login_required(login_url="login")
@role_required(allowed_roles=["tester"])
def testerDashboardView(request):
    return render(request,"dashboards/tester_dashboard.html")