from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from register.forms import RegistrationForm
from .models import User,Member
#from passlib.hash import pbkdf2_sha256
def index(request):
    return render(request,'register/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

"""def register(request):
    #context = {"form":RegistrationForm}
    
    if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']
        #password = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
        #print(password)
        #User.objects.create(username = username, password = password)
        user =  User(username = request.POST['username'] , password = request.POST['password'],Email = request.POST['Email'])
        user.save()
        return render(request, "register/index.html",)
    else:
        return render(request, "register/registration.html",)"""

    
def user_login(request):
    if request.method == 'POST':
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        if User.objects.filter(username = request.POST['username'],password = request.POST['password'], Email = request.POST['Email']).exists():
            user =  User.objects.get(username = request.POST['username'],password = request.POST['password'], Email = request.POST['E-mail'])

            return HttpResponse("hello")
            return render(request, 'register/index.html', {'user':user})
        else:
            return HttpResponse("invalid login detail")
            return render(request, 'register/login.html', context)
    else:
        context = {'msg': 'invalid username and password'}
        return render(request, 'register/login.html', context)

def emp_signup(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return render(request, 'register/emplogin.html')
    else:
        return render(request, 'register/emp_signup.html')

def welcome(request):
    return render(request, 'register/welcome.html')

def emplogin(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'register/welcome.html', {'member': member})
        else:
            return HttpResponse("invalid login detail")
            return render(request, 'register/emp_signup.html', context)
    else:
        context = {'msg': 'Invalid username or password'}
        return render(request, 'register/emplogin.html', context)


"""user = User(username = request.POST['username'],password = request.POST['password'])
        if user:
            return HttpResponse("hello")
            return render(request, 'register/index.html', {'user':user})
            #else:
                #return HttpResponse("Your account was inactive.")
        #else:
            #print("Someone tried to login and failed.")
            #print("They used username: {} and password: {}".format(username,password))
            #return HttpResponse("Invalid login details given")
    else:
        return render(request, 'register/login.html', {})
"""
