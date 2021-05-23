from django.db import models
from django.contrib.auth.models import User

# Create your models here.

categories = [
    ('Select Category','Select Category'),
    ('Popular flavours','Popular flavours'),
    ('Design Cakes','Design Cakes'),
    ('Jar Cakes','Jar Cakes'),
    ('Brownies','Brownies')
]

class cake_list(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices = categories , default = 'Select Category')
    description = models.CharField( max_length=300)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

class orders(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField(max_length=64)
    phone = models.CharField(max_length=30)
    house_name = models.CharField(max_length=80)
    location = models.CharField(max_length=60)
    pin = models.IntegerField()
    date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    cake_list = models.ForeignKey(cake_list,on_delete = models.CASCADE)
    status = models.CharField(max_length=30, default='Pending')
    order_status = models.CharField(max_length=30, default='True')


class messages(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=64)
    message = models.CharField( max_length=250)
    date = models.DateTimeField(auto_now = True)

