from django.contrib import admin
from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('signup/',views.sign_up,name="sign-up"),
    path('login/',views.log_in,name="log-in"),
    path('logout/',views.log_out,name="log-out"),
    

]
