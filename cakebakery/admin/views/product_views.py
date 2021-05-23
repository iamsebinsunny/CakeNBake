from django.shortcuts import render,reverse,redirect,get_object_or_404
from products.forms import add_cake_form
from products.models import cake_list
from django.contrib import messages 

# Create your views here.

def add_cake(request):
    context = dict()
    form = add_cake_form()
    lists = cake_list.objects.all()
    context['form'] = form
    context['lists'] = lists
    if request.method == 'POST':
        form = add_cake_form(request.POST,request.FILES)   
        if form.is_valid():
            form.save() 
            messages.info(request,'Product added successfully')
    return render(request,'admin/add_view_products.html',context)

def update_cake(request,id):
    context = dict()
    form = add_cake_form()
    item=cake_list.objects.get(id=id)
    context['form'] = form
    context['item'] = item
    if request.method == 'POST':  
        form = add_cake_form(request.POST,request.FILES, instance = item)   
        if form.is_valid():
            form.save()
            return redirect(reverse('admin:add-cake')) 
    return render(request,'admin/update_products.html',context)

def delete_cake(request,id):
    item = get_object_or_404(cake_list,id=id)
    item.delete()
    messages.error(request,'Product deleted successfully')
    return redirect(reverse('admin:add-cake'))