from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user_id = models.OneToOneField(to=User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16,unique=True,null=True)
    address = models.TextField()
    country = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    profile_image = models.ImageField(upload_to='static/profile')
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class Post(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_image  = models.ImageField(upload_to='static/posts',null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
