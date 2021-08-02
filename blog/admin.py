from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import UserDetails
# Register your models here.

class UserDetailsAdmin(ModelAdmin):
    list_display = ['user_id','phone_number','address','create_date','updated_date']
    verbose_name = 'User Details'

admin.site.register(UserDetails,UserDetailsAdmin)
