from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# when sender User is saved (a signal), which is acknowledged by receiver
@receiver(post_save, sender=User)
# sender transmitts the following information in a signal - instance of user and whether user was created
def create_profile(sender, instance, created, **kwarg):
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwarg):
    instance.profile.save()
