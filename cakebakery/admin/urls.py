from django.contrib import admin
from django.urls import path
from . import views

app_name="admin"

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('update',views.update_profile,name='update-profile'),
    path('user-list',views.user_list,name='user-list'),
    
    

]
