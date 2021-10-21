from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

class product(models.Model):
    product_image=models.ImageField(blank=False)
    name=models.CharField(max_length=100,blank=False)
    quantity=models.FloatField(null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    date_posted=models.DateTimeField(default=timezone.now)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    tags=TaggableManager(blank=True)
    description=RichTextUploadingField(blank=True)
    is_sold=models.BooleanField(default=False)
    city=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return str(self.name+" from "+self.city)
    
    def get_absolute_url(self):
        return reverse('store')

class order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=True)
    Transaction_id=models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.pk)
    
    @property
    def get_total_amount(self):
        orderItems=self.orderitem_set.all()
        total=sum([item.get_payable_amount for item in orderItems])
        return total

class orderItem(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    Transaction_id=models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.pk)

    @property
    def get_payable_amount(self):
        return self.product.price*self.product.quantity