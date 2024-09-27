from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm

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
                return render(request, 'accounts/register.html', {'form':form,'error': error_message})
            
            user = User.objects.create_user(username =username,password=password)
            login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/register.html',{'form':form})
    else:
        form = RegisterForm()
        context = {'form':form}
        return render(request, 'accounts/register.html',context)

def login_view(request):
    error_message = None
    forgot_password = None
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        #Checking if user exists by username
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            user_obj = None
            
        if user_obj is not None:    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next') or 'home'
                return redirect(next_url)
            else:
                forgot_password = "Wrong Password!! Try again"
                return render(request, 'accounts/login.html', {'forgot_password':forgot_password})
        else:
            error_message = "User not Registered."
            
    return render(request, 'accounts/login.html', {'error':error_message})

def logout_view(request):
    if request.method == "POST":
        return render(request, 'accounts/logout.html')
    else:
        logout(request)
        return redirect('home')

def forgotpassword_view(request):
        return render(request,'accounts/forgot_password.html')

#Home View
#Using the decorator
@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html')

# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/' 
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'registration/protected.html')