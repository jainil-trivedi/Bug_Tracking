from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required

# Create your views here.
#@login_required(login_url="login")
@role_required(allowed_roles=["admin"])
def adminDashboardView(request):
    return render(request,"dashboards/admin_dashboard.html")

#@login_required(login_url="login")
@role_required(allowed_roles=["manager"])
def managerDashboardView(request):
    return render(request,"dashboards/manager_dashboard.html")

#@login_required(login_url="login")
@role_required(allowed_roles=["developer"])
def developerDashboardView(request):
    return render(request,"dashboards/developer_dashboard.html")

#@login_required(login_url="login")
@role_required(allowed_roles=["tester"])
def testerDashboardView(request):
    return render(request,"dashboards/tester_dashboard.html")