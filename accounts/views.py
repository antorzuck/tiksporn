from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import *

# Create your views here.

def signup(request):
	if request.method == 'POST':
		username= request.POST['user']
		email = request.POST['mail']
		password= request.POST['passw']
		password1= request.POST['passw1']
		
		if len(username) < 4:
			messages.error(request, "Username must be 5 characters long.")
			return redirect('/')
		if password != password1:
			messages.error(request, "password not matched")
			return redirect('/')
		try:
			usr= User.objects.get(username=username)
			messages.error(request, "Username Already Exist!")
			return redirect('/')
		except User.DoesNotExist:
			usr=User.objects.create_user(username=username, password=password, email=email)
			usr.save()
			messages.info(request, "Account successfuly created. now please login!")
			return redirect ('/')


def hlogin(request):
	if request.method == 'POST':
		username= request.POST['u']
		password= request.POST['p']
		
		user= authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.info(request, "Successfully Login")
			return redirect('/')
		else:
			messages.error(request, "Incorrect username or password")
			return redirect('/')
			
			
def hlogout(request):
	logout(request)
	messages.error(request, "Logout")
	return redirect('/')
	
def tagview(request, tag):
	filter_tag = Video.objects.filter(tags__name__in=[tag])
	
	
	context={
		'tg':filter_tag,
	
	}
	return render(request, 'tagview.html', context)
	

def pp(request):
	return render(request, 'privacypolicy.html')
	
def about(request):
	return render(request, 'aboutus.html')