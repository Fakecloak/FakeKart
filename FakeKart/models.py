from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from itertools import product


# Create your models here.


def getFileName(request,filename):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_filename = "%s%s"%(current_time,filename)
    return os.path.join('uploads/',new_filename)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False,null=False)
    images = models.ImageField(upload_to=getFileName, null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    status= models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False,null=False)
    vendor = models.CharField(max_length=100, blank=False,null=False)
    product_images = models.ImageField(upload_to=getFileName, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.IntegerField(null=False, blank=False)
    selling_price = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    status= models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)
    trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")

    def __str__(self):
        return self.name


class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at= models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty * self.product.selling_price
    
class Favorite(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
