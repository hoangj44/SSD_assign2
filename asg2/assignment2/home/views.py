from django.shortcuts import render

def index(request):
	return render(request, 'home/front.html')

def register(request):
	return render(request, 'register/register.html')

def reset(request):
	return render(request, 'reset/reset.html')

def login(request):
	return render(request, 'login/login.html')
