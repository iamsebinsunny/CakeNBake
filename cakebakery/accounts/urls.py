from django.contrib import admin
from django.urls import path
from . import views
from products.views import CreateCheckoutSessionView

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
    path('cancel-order/<int:id>',views.cancel_order,name="cancel-order"),
    path('messages/',views.messages,name="messages"),

    path('landing-page/',views.landing_page,name="landing-page"),
    path('create-checkout-session/<int:id>',CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payment-successfull/',views.payment_successfull,name='payment-successfull'),
    path('payment-cancelled/',views.payment_cancelled,name='payment-cancelled')

    

]
