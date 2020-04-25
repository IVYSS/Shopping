from .models import Product,Product_type,Order_products,Address
from Profile.models import Order,Payment
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.checks import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from Index.forms import CheckoutFrom
from decimal import *
from django.contrib.auth.forms import PasswordChangeForm
from .form import ModelProduct

import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"




# Create your views here.

def show(request):
    search = request.GET.get('search', '')
    mytype = request.GET.get('mytype', '')
    print(mytype)
    print(search)
    product_type= Product_type.objects.all()
    product = Product.objects.filter(Q(is_hide=False)&(Q(name__icontains=search)))
    paginator = Paginator(product, 2)
    page = request.GET.get('page')
   
    product = paginator.get_page(page)
    return render(request, 'Index/home.html', context=
    {
        'product':product,
        'product_type':product_type
    })

def Checkout(request):
    if request.method == 'POST':
        my_form = CheckoutFrom(request.POST or None)
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            if my_form.is_valid():
                street_address = my_form.cleaned_data.get('street_address') 
                apartment_address = my_form.cleaned_data.get('apartment_address')
                country = my_form.cleaned_data.get('country')
                zip = my_form.cleaned_data.get('zip')
                default = my_form.cleaned_data.get('default')
                payment_option = my_form.cleaned_data.get('payment_option')
                adddress = Address (
                    user = request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country = country,
                    zip = zip,
                    default = default,
                    payment_option = payment_option,
                )
                adddress.save()
                order.delivery_place = adddress
                order.save()

                if payment_option == 'S':
                    return redirect("payment", payment_option = 'stripe')
                elif payment_option == 'P':
                    return redirect("payment", payment_option = 'paypal')
                else:
                    messages.warning(request, "Invalid payment option selected")
                    return redirect("checkout")
        
        except ObjectDoesNotExist:
            messages.warning(request, "You do not have an active order")
            return redirect("order-summary")
       
    else:
        my_form = CheckoutFrom()
        context = {
            'my_form':my_form
        }
    return render(request, 'Index/checkout.html', context)
    
    
def PaymentView(request, payment_option):
    if request.method == 'POST':
        order = Order.objects.get(user=request.user, ordered=False)
        token = request.POST.get('stripeToken')
        my_amount = int(order.get_total() * 100)
        print(request.POST.get('stripeToken'))
        print(type(2000))
        print(type(my_amount))
        print(my_amount)
        try:
            charge = stripe.Charge.create(
                amount = my_amount,      
                currency="thb",
                source=token,
            )        
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = request.user
            payment.method = 'S'
            payment.amount = order.get_total()
            payment.save()

            order.ordered = True
            order.payment = payment
            
            order.save()
            

            messages.success(request, "Your order was successful!")
            return redirect("/")

        except stripe.error.CardError as e:
        
            body = e.json_body
            err = body.get('error', {})
            messages.warning(request, f"{err.get('message')}")
            return redirect("/")
        
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.warning(request, "Rate limit error")
            return redirect("/")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            print(e)
            messages.warning(request, "Invalid parameters")
            return redirect("/")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.warning(request, "Not authenticated")
            return redirect("/")

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.warning(request, "Network error")
            return redirect("/")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.warning(
                request, "Something went wrong. You were not charged. Please try again.")
            return redirect("/")

        except Exception as e:
            # send an email to ourselves
            messages.warning(
                request, "A serious error occurred. We have been notifed.")
            return redirect("/")       
    else:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {
            'order' : order
        }
        return render(request, 'Index/payment.html' , context)
    return render(request, 'Index/payment.html')

@login_required
def OrderSummary(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {
            'order': order
            }
        return render(request, 'Index/order_summary.html',context)
    except ObjectDoesNotExist:
        messages.warning(request, "You do not have an active order")
        return redirect("/")

@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    order_product, created = Order_products.objects.get_or_create(product_id=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        
        # check if the order item is in the order
        if order.products.filter(product_id__name=product.name).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "This product quantity was updated.")
        else:
            order.products.add(order_product)
            messages.info(request, "This product was added to your cart.")
        
    else:
        date = timezone.now()
        order = Order.objects.create(user=request.user, date=date)
        order.products.add(order_product)
        messages.info(request, "This product was added to your cart.")
       
    return redirect("order-summary")

@login_required
def remove_from_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product_id__name=product.name).exists():
            order_product = Order_products.objects.filter(product_id=product, user=request.user, ordered=False)[0]
            order.products.remove(order_product)
            order_product.delete()
            messages.info(request, "This product was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This product was not in your cart")
            return redirect("product_detail", product_id=product_id)
    
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product_detail", product_id=product_id)
   

@login_required
def remove_single_product_from_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product_id__name=product.name).exists():
            order_product = Order_products.objects.filter(product_id=product, user=request.user, ordered=False)[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.products.remove(order_product)
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This product was not in your cart")
            return redirect("order-summary")    
    else:
        messages.info(request, "You do not have an active order")
        return redirect("order-summary")
    

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

@login_required
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
            context['error'] = 'Password Not Match'             
    return render(request, template_name='Index/signup.html', context=context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


# Model Form
def make_product(request):

    product_type = Product_type.objects.all()
    if request.method == 'POST':
        form = ModelProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            type_id = request.POST.get('type')
            product.product_type_id = Product_type.objects.get(pk=type_id)
            product.sale_user_id = request.user
            form.save()
    else:
        form = ModelProduct()
    context = {
        'form' : form,
        'type' : product_type
    }

    return render(request, 'Index/make-product.html', context=context)