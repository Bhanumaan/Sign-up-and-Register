from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import context
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def index(request):
    return render(request,'index.html', {'title':'index'})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()


            messages.success(request,f"your account has been created ! You are now able to login")
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form':form,'title':'register here'})


def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            form=login(request,user)
            messages.success(request, f'welcome {username} !!' )
            return redirect('index')
        else:
            messages.info(request,f'account does not exist please sign in ')
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form,'title':'log in '})










