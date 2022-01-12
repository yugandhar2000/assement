from typing import Reversible
from django.db import models
from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm, CustomerForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Customer, diplayusername
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request,"profiles/home.html")

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('myself')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect('myself')
            else:
                messages.info(request,"username or password is incorrect")
            

        context={}
        #return reverse_lazy('home')
        return render(request,"profiles/login.html",context)
        #return HttpResponseRedirect(Reversible())
        #return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('myself')
    else:
        form=CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('taskscreate')
            else:
                messages.info(request,"incorrect details check once or recreate")
                
        context ={'form': form}
        return render(request,"profiles/register.html",context)

class TaskCreate(CreateView):
    model=Customer
    fields="__all__"
    #fields = ['user','phone','profile_pic']
    success_url=reverse_lazy('login')
    
def myself(request):
    return render(request,'profiles/myself.html')

def diplayusername(request):
    displaynames = User.objects.all()
    return render(request,'profiles/userslist.html',{"diplayusername": displaynames})


def social(request):
    return render(request,'profiles/socialmedia.html')


def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profiles/account_settings.html', context)




def view_profile(request):
    context={'user':request.user}
    return render(request,"profiles/profile.html",context)


def logoutUser(request):
    logout(request)
    return redirect('home')


'''def userpage(request):
    context={}
    return render(request,'profiles/user.html',context)

class user_list(request, ListView):
    model = models.User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = context['user'].filter(user=self.request.user)
        #context['count'] = context['task'].filter(complete=False).count()
        return context'''

'''def userprofile(request):
    class Meta:
        model = Customer
    return render(request,'profiles/userpic.html')

    if request.method == 'POST':
        form = Customer(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Customer()
    return render(request,'profiles/userpic.html', {'form' : form})
    def success(request):
    return HttpResponse('successfully uploaded')'''
  
  



    

