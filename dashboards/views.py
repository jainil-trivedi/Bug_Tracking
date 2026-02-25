from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def adminDashboardView(request):
    return render(request,"dashboards/admin_dashboard.html")

@login_required(login_url="login")
def managerDashboardView(request):
    return render(request,"dashboards/manager_dashboard.html")

@login_required(login_url="login")
def developerDashboardView(request):
    return render(request,"dashboards/developer_dashboard.html")

@login_required(login_url="login")
def testerDashboardView(request):
    return render(request,"dashboards/tester_dashboard.html")