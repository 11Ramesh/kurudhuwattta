from django.shortcuts import render,redirect
from .models import *
from .form import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.







def register_view(request):
     if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_view')  # Replace 'success' with the name of the URL pattern for you
        else:
            return render(request, 'register/register.html', {'form': form})

     else:
        form = UserRegisterForm()
    
        return render(request, 'register/register.html', {'form': form})



def home_view(request): 
    return render(request, 'home/home.html')




def login_check(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        # destinations = UserRegister.objects.all()
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
           
            print(password)
            if user is not None:
                login(request, user)
                return redirect('home_view')  # Redirect to a success page
            else:
                form = LoginForm()
                return render(request, 'login/login.html', {'form': form})



    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})
