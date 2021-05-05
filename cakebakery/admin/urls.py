from django.contrib import admin
from django.urls import path
from .views import admin_views,product_views

app_name="admin"

urlpatterns = [
    path('',admin_views.dashboard,name='dashboard'),
    path('update',admin_views.update_profile,name='update-profile'),
    path('user-list',admin_views.user_list,name='user-list'),
    
    path('add-cake',product_views.add_cake,name='add-cake'),
    path('update-cake/<int:id>',product_views.update_cake,name='update-cake'),
    path('delete-cake/<int:id>',product_views.delete_cake,name='delete-cake')

]
