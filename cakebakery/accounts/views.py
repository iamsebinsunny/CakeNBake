from django.shortcuts import render,reverse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages as mssg
from products.models import cake_list,orders,messages
from .forms import SignUpForm
from products.forms import make_order_form,message_form


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

def category_filter(request,category_name):
    context = dict()
    items = cake_list.objects.filter(category = category_name)
    context['items'] = items
    return render(request,'accounts/homepage.html',context)

def sign_up(request):
    form = SignUpForm(request.POST or None)
    context= dict()
    context["form"] = form
    if request.method == "POST":
        if form.is_valid(): 
            user=form.save()
            login(request,user)      
            return redirect(reverse('accounts:homepage'))
        else:
            mssg.info(request,form.errors)
            return render(request,'accounts/sign_up.html',context)
    return render(request,'accounts/sign_up.html',context)

def log_in(request):
    form = AuthenticationForm(request, data=request.POST)
    context= dict()
    context["form"] = form
    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username,password=password)
            login(request,user)  
            if user.is_superuser:
                return redirect(reverse('admin:dashboard'))
            if user:    
                return redirect(reverse('accounts:homepage'))
        else:
            return render(request,'accounts/log_in.html',context)    
    return render(request,'accounts/log_in.html',context)

def log_out(request):
    logout(request)
    return redirect(reverse('accounts:log-in'))

def my_orders(request):
    context = dict()
    user = request.user
    myorders = orders.objects.filter(user_id = user.id).order_by('-date')
    context['orders'] = myorders
    return render(request,'accounts/my_orders.html',context)

def cancel_order(request,id):
    order = orders.objects.get(id = id)
    order.order_status = 'Cancelled'
    order.save()
    mssg.info(request,'Order cancelled successfully. Refund will be credited to your bank account within 3-4 working days')
    return redirect(reverse('accounts:my-orders'))


def messages(request):
    context = dict()
    form = message_form(request.POST or None)
    context['form'] = form
    if request.method == "POST":
        if form.is_valid: 
            order=form.save()
            mssg.info(request,'Thank you for filling the form. Will get back to you soon')
    return render(request,'accounts/messages.html',context)

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
            context['id'] = id
            return render(request,'accounts/landingpage.html',context)
    return render(request,'accounts/delivery_details.html',context)

def landing_page(request):
    return render(request,'accounts/landingpage.html')

def payment_cancelled(request):
    cancel_order = orders.objects.latest('id')
    if cancel_order.status == 'Pending':
        cancel_order.delete()
    return redirect(reverse('accounts:homepage'))

def payment_successfull(request):
    success_order = orders.objects.latest('id')
    success_order.status = 'Success'
    success_order.save()
    return redirect(reverse('accounts:my-orders'))