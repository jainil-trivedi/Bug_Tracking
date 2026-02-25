from django.shortcuts import render,redirect
from .forms import UserSignupForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def userSignupView(request):
    if request.method =="POST":
      form = UserSignupForm(request.POST or None)
      if form.is_valid():
        form.save()
        return redirect('login') #error
      else:
        return render(request,'core/signup.html',{'form':form})  
    else:
        form = UserSignupForm()
        return render(request,'core/signup.html',{'form':form})
    
def userLoginView(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            email    = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user     = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                if user.role == "admin":
                    return redirect("adminDashboard")
                elif user.role == "manager":
                    return redirect("managerDashboard")
                elif user.role == "developer":
                    return redirect("developerDashboard")
                elif user.role == "tester":
                    return redirect("testerDashboard")
            else:
                return render(request, 'core/login.html', {'form': form, 'error': 'Invalid email or password'})
    else:
        form = UserLoginForm()
        return render(request, 'core/login.html', {'form': form})

def userLogoutView(request):
    logout(request)
    return redirect('login')

