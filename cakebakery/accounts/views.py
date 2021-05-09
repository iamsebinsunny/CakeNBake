from django.shortcuts import render,reverse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from products.models import cake_list
from .forms import SignUpForm
from products.forms import make_order_form


# Create your views here.

def indexpage(request):
    context = dict()
    context['title'] = 'indexpage'
    return render(request,'accounts/index.html',context)

def homepage(request):
    context = dict()
    items = cake_list.objects.all()
    context['items'] = items
    return render(request,'accounts/homepage.html',context)

def sign_up(request):
    form = SignUpForm(request.POST or None)
    context= dict()
    context["form"] = form
    if request.method == "POST":
        if form.is_valid: 
            user=form.save()
            login(request,user)      
            return redirect(reverse('accounts:homepage'))
    return render(request,'accounts/sign_up.html',context)

def log_in(request):
    form = AuthenticationForm(request, data=request.POST)
    context= dict()
    context["form"] = form
    if request.method == "POST":
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username,password=password)
            login(request,user)  
            if user.is_superuser:
                return redirect(reverse('admin:dashboard'))
            if user:    
                return redirect(reverse('accounts:homepage'))
    return render(request,'accounts/log_in.html',context)

def log_out(request):
    logout(request)
    messages.success(request,'successfully logged out')
    return redirect(reverse('accounts:log-in'))

def checkout(request,id):
    context = dict()
    customer=request.user
    form = make_order_form(request.POST or None)
    context['customer'] = customer
    context['form'] = form
    if request.method == "POST":
        if form.is_valid: 
            order=form.save(commit = False)    
            order.user_id = customer.id
            order.cake_list_id = id
            order = order.save()
            print(order) 
            return redirect(reverse('accounts:homepage'))
    return render(request,'accounts/delivery_details.html',context)