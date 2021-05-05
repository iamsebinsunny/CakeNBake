from django import forms
from .models import cake_list

class add_cake_form(forms.ModelForm):
    class Meta:
        model = cake_list
        fields = ['name','description','price','image']