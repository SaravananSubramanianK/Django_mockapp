from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from app.forms import *
from app.models import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    user_form = UserForm()
    edu_form = EducationForm()
    if request.method=='POST':
        user_form = UserForm(request.POST)
        edu_form= EducationForm(request.POST)
        if user_form.is_valid() and edu_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            edu = edu_form.save(commit=False)
            edu.user=user
            edu.save()
            send_mail('Registration confirmation',
                      'Thanks for registering in our job portal,your registration is successfull',
                      'sarosaran0508@gmail.com',
                      [user.email],
                      fail_silently=False,
                    
                    )
          
    d = {'user_form':user_form,'edu_form':edu_form}
    return render(request,'register.html',context=d)

def Log_in(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect(reverse('education'))
        else:
            raise ValidationError('user is not active')
    return render(request,'login.html')

@login_required
def Log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Log_in'))

@login_required
def education(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    edu = Education.objects.get(username=username)
    d = {'user':user,'edu':edu}
    return render(request,'profile.html',context=d)

@login_required
def change_pword(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    if request.method=='POST':
        pass_word = request.POST['password']
        user.set_password(pass_word)
        user.save()
    return render(request,'change_pword.html')

def reset_pword(request):
    if request.method == 'POST':
        us = request.POST['username']
        user = User.objects.get(username=us)
        pw = request.POST['password']
        user.set_password(pw)
        user.save()
    return render(request,'reset_pword.html')


