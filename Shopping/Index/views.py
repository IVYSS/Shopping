from .models import Product,Product_type
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def show(request):
    search = request.GET.get('search', '')
    mytype = request.GET.get('mytype', '')
    print(mytype)
    print(search)
    product_type= Product_type.objects.all()
    product = Product.objects.filter(Q(is_hide=False)&(Q(name__icontains=search)))
    paginator = Paginator(product, 1)
    page = request.GET.get('page')
   
    product = paginator.get_page(page)
    return render(request, 'Index/home.html', context=
    {
        'product':product,
        'product_type':product_type
    })
def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product' : product
    }

    return render(request, 'Index/detail.html', context=context)
    
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
    context = {}       
    if request.method == 'POST':         
        fname = request.POST.get('fname')         
        lname = request.POST.get('lname')         
        username = request.POST.get('username')         
        email = request.POST.get('email')         
        password = request.POST.get('password')         
        password2 = request.POST.get('cpassword')
        print('-------------------------')
        print(fname)
        print(lname)
        print(username)
        print(email) 
        print(password)         
        print(password2)       
        if password == password2:             
                      
            user = User.objects.create_user(username,  email, password)
            user.fist_name = fname
            user.last_name = lname
            user.save()
            print("OK")             
            return redirect('login')
        else:             
            context['error'] = 'Password Not Match!!!'             
    return render(request, template_name='Index/signup.html', context=context)