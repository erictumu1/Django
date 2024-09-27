from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .form import RegisterForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            #Checks if a user exists
            if User.objects.filter(username=username).exists():
                error_message= "Username already exists. Enter a different name"
                return render(request, 'cars/register.html', {'form':form,'error': error_message})
            
            user = User.objects.create_user(username =username,password=password)
            login(request,user)
            return redirect('home')
        else:
            return render(request,'cars/register.html',{'form':form})
    else:
        form = RegisterForm()
        context = {'form':form}
        return render(request, 'cars/register.html',context)

def login_view(request):
    error_message = None
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'cars/login.html', {'error':error_message})

def logout_view(request):
    if request.method == "POST":
        return render(request, 'cars/logout.html')
    else:
        logout(request)
        return redirect('home')

#Home View
#Using the decorator
@login_required
def home_view(request):
    return render(request, 'cars/home.html')

# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/' 
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'cars/protected.html')