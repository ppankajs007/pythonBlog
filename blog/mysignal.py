from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from blog.models import UserDetails

@receiver(post_save,sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user_id=instance)