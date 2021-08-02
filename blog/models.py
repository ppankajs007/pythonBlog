from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user_id = models.OneToOneField(to=User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16,unique=True,null=True)
    address = models.TextField()
    country = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    profile_image = models.ImageField(upload_to='assets/img')
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    def __str__(self):
        return "%s" % self.user_id
