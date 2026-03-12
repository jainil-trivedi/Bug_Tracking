from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from core.models import Project, Bug

# Create your views here.
#@login_required(login_url="login")
@role_required(allowed_roles=["admin"])
def adminDashboardView(request):
    projects = Project.objects.all()
    total_projects = projects.count()
    return render(request,"dashboards/admin_dashboard.html",{"projects": projects,"total_projects": total_projects})

#@login_required(login_url="login")
@role_required(allowed_roles=["manager"])
def managerDashboardView(request):
    projects = Project.objects.filter(manager=request.user)
    my_projects = projects.count()
    return render(request,"dashboards/manager_dashboard.html",{"projects": projects,"my_projects": my_projects})

#@login_required(login_url="login")
@role_required(allowed_roles=["developer"])
def developerDashboardView(request):
    return render(request,"dashboards/developer_dashboard.html")

#@login_required(login_url="login")
@role_required(allowed_roles=["tester"])
def testerDashboardView(request):
    return render(request,"dashboards/tester_dashboard.html")