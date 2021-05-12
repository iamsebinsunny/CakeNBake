from django import forms
from .models import cake_list,orders,messages

class add_cake_form(forms.ModelForm):
    class Meta:
        model = cake_list
        fields = ['name','category','description','price','image']

class make_order_form(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['first_name','last_name','email','phone','house_name','pin','location']

class message_form(forms.ModelForm):
    class Meta:
        model = messages
        fields = '__all__'