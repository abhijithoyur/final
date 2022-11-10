from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'form.html')
        else:
            messages.info(request,'invalid username or password')
            return redirect('/')
    return render(request,"login.html")

def form(request):
    return render(request,'form.html')
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user already exists")
                return redirect('registration')
            user=User.objects.create_user(username=username,password=pass1)
            user.save()
            return render(request,'login.html')
    return render(request,'afterlogin.html')
def finalform(request):
    return render(request,'finalform.html')
def submiting(request):
    return render(request,'order_confirming.html')