from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    MALE, FEMALE = 1, 2
    GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    sign_up_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    subscription = models.CharField(max_length=10, null=True, blank=True)
    subscription_date = models.DateTimeField(null=True, blank=True)
    zip_code = models.CharField(max_length=8, null=True, blank=True)
    street = models.CharField(max_length=300, null=True, blank=True)
    number = models.CharField(max_length=5, null=True, blank=True)
    complement = models.CharField(max_length=300, null=True, blank=True)
    neighborhood = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    pro = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()