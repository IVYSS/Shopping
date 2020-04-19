
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
     return render(request, 'Index/index.html')

def login(request):
     return render(request, 'Index/login.html')

def signin(request):
     return render(request, 'Index/signin.html')