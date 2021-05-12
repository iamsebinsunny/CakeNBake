from django.contrib import admin
from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('',views.indexpage,name="indexpage"),
    path('homepage/',views.homepage,name="homepage"),
    path('signup/',views.sign_up,name="sign-up"),
    path('login/',views.log_in,name="log-in"),
    path('logout/',views.log_out,name="log-out"),


    path('category/<str:category_name>',views.category_filter,name='filter'),
    path('checkout/<int:id>',views.checkout,name='checkout'),
    path('myorders/',views.my_orders,name="my-orders"),
    path('messages/',views.messages,name="messages"),
    

]
