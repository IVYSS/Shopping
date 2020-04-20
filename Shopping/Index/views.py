
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
# Create your views here.

def show(request):
     return render(request, 'Index/index.html')

def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('show')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='Index/login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('show')

def signup(request):
     return render(request, 'Index/signup.html')