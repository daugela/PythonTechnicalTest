from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def display_name(self):
        return u"%s %s" % (self.user.first_name, self.user.last_name)

    display_name.short_description = "Who"

    def __str__(self):
        return f"{self.user.username}"

    def __unicode__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"
        db_table = "platform_user_profiles"


#  Define signals so our Profile model will be automatically created/updated when we create/update User instances
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
