from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class profile(models.Model):
    profile_pic=models.ImageField(blank=True)
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    Phonenumber=models.IntegerField(unique=True,blank=True,null=True)
    education=models.CharField(max_length=50,blank=True,null=True)
    other_info=models.CharField(max_length=100,blank=True,null=True)
    is_expert=models.BooleanField(default=False)

class Contract(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    land=models.FloatField(blank=True,null=True)
    Year_of_contract=models.FloatField(blank=True,null=True)
    date_posted=models.DateTimeField(default=timezone.now)    
    is_farmer=models.BooleanField(default=False)
    description=RichTextUploadingField(blank=True)