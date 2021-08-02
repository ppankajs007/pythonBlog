from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login as userLogin,logout as userLogout
from .models import UserDetails
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            messages.warning(request,'Required all fields *')
            return redirect('login')
        else:
            user = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
            if user is not None:
                userLogin(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Username and password is wrong')
                return redirect('register')
    else:
        return render(request,'login.html')

def logout(request):
    userLogout(request)
    return redirect('/')



def register(request):
        if request.method == 'POST':
            error = 0
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if firstname == '' or lastname == '' or username == '' or email == '' or password == '':
                messages.warning(request, 'Required all fields *')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    error = 1
                    messages.warning(request,'Email is already exist')
                if User.objects.filter(username=username).exists():
                    error = 1
                    messages.warning(request, 'Username is already exist')
                if password != confirm_password:
                    error = 1
                    messages.warning(request, 'Password dont match')
                if error:
                    return redirect('register')
                else:
                    user = User(first_name=firstname,last_name=lastname,username=username,email=email,password=make_password(password))
                    user.save()
                    userDetails = authenticate(request, username=username,password=password)
                    userLogin(request,userDetails)
                    return redirect('profile')
        else:
            return render(request, 'register.html')



def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            phone_number = request.POST.get('phone_number')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            address = request.POST.get('address')
            country = request.POST.get('country')
            state = request.POST.get('state')

            userProfileData = UserDetails.objects.get(user_id=request.user.id)

            if userProfileData.phone_number != phone_number:
                if UserDetails.objects.filter(phone_number=phone_number).exists():
                    messages.warning(request, 'Phone number is exist')
                    return redirect('profile')
            userUpdate = User.objects.get(id=request.user.id)
            userUpdate.first_name = first_name
            userUpdate.last_name = last_name
            userUpdate.save()
            userProfileData = UserDetails.objects.get(user_id=request.user.id)
            userProfileData.phone_number = phone_number
            userProfileData.address = address
            userProfileData.country = country
            userProfileData.state = state
            userProfileData.save()
            if request.FILES:
                userProfileData.profile_image = request.FILES['profile_image']
                userProfileData.save()
            messages.warning(request, 'Profile update successfuly')
            return redirect('profile')
        else:
            details = {}
            details['data'] = UserDetails.objects.get(user_id=request.user.id)
            return render(request,'profile.html',details)
    else:
        return redirect('login')
