from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
        return render(request,'login.html')


def register(request):
        if request.method == 'POST':
            error = 0
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if User.objects.filter(email=email).exists():
                error = 1
                messages.warning(request,'Email is already exist')
            if User.objects.filter(username=username).exists():
                error = 1
                messages.warning(request, 'Username is already exist')
            if password != confirm_password:
                error = 1
                messages.warning(request, 'Password dont match')
            if error == 1:
                return redirect('register')
            else:
                user = User(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                return redirect('index')
        else:
            return render(request, 'register.html')
