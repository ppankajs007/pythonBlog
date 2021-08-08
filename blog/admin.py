from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import UserDetails,Post
# Register your models here.

class UserDetailsAdmin(ModelAdmin):
    list_display = ['user_id','phone_number','address','create_date','updated_date']

class UserPost(ModelAdmin):
    list_display = ['user_id','title','create_date']

admin.site.register(UserDetails,UserDetailsAdmin)
admin.site.register(Post,UserPost)
