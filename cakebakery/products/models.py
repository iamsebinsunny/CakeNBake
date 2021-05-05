from django.db import models

# Create your models here.
class cake_list(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField( max_length=60)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
