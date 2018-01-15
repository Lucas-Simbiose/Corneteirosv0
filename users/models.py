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

class TeamData(models.Model):
    Corinthians, Vasco, Atletico_pr, Atletico_mg, Palmeiras = 1, 2, 3, 4, 5
    TEAM_CHOICES = (
        (Corinthians, 'Corinthians'),
        (Vasco, 'Vasco'),
        (Atletico_pr, 'Atletico_pr'),
        (Atletico_mg, 'Atletico_mg'),
        (Palmeiras, 'Palmeiras'),
    )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nome do Time')
    real_team = models.PositiveIntegerField(choices=TEAM_CHOICES, null=True, blank=True, verbose_name='Time do Coração')

    def __str__(self):
        return self.profile.user.username

@receiver(post_save, sender=Profile)
def create_or_update_profile_teamdata(sender, instance, created, **kwargs):
    if created:
        TeamData.objects.create(profile=instance)
    instance.teamdata.save()

class TeamCrest(models.Model):
    Grande, Pequeno, Medio = 1, 2, 3
    CREST_CHOICES = (
        (Grande, 'Grande'),
        (Pequeno, 'Pequeno'),
        (Medio, 'Médio'),
    )
    Verde, Vermelho, Azul, Amarelo, Preto = 1, 2, 3, 4, 5
    CORES = (
        (Verde, 'Verde'),
        (Vermelho, 'Vermelho'),
        (Azul, 'Azul'),
        (Amarelo, 'Amarelo'),
        (Preto, 'Preto'),
    )
    teamdata = models.OneToOneField(TeamData, on_delete=models.CASCADE)
    crest_type = models.PositiveSmallIntegerField(choices=CREST_CHOICES, null=True, blank=True, verbose_name='Brasão')
    stamp = models.PositiveSmallIntegerField(choices=CREST_CHOICES, null=True, blank=True, verbose_name='Estampa')
    adornment = models.PositiveSmallIntegerField(choices=CREST_CHOICES, null=True, blank=True, verbose_name='Adorno')
    collor1 = models.PositiveSmallIntegerField(choices=CORES, null=True, blank=True, verbose_name='Cor Brasão 1')
    collor2 = models.PositiveSmallIntegerField(choices=CORES, null=True, blank=True, verbose_name='Cor Brasão 2')
    collor3 = models.PositiveSmallIntegerField(choices=CORES, null=True, blank=True, verbose_name='Cor Brasão 3')

    def __str__(self):
        return self.teamdata.profile.user.username

@receiver(post_save, sender=TeamData)
def create_or_update_teamdata_teamcrest(sender, instance, created, **kwargs):
    if created:
        TeamCrest.objects.create(teamdata=instance)
    instance.teamcrest.save()

class TeamShirt(models.Model):
    A, B, C, D, E = 1, 2, 3, 4, 5
    SHIRT_CHOICES = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
        (E, 'E'),
    )
    Verde, Vermelho, Azul, Amarelo, Preto = 1, 2, 3, 4, 5
    CORES = (
        (Verde, 'Verde'),
        (Vermelho, 'Vermelho'),
        (Azul, 'Azul'),
        (Amarelo, 'Amarelo'),
        (Preto, 'Preto'),
    )
    teamdata = models.OneToOneField(TeamData, on_delete=models.CASCADE)
    shirt_type = models.PositiveSmallIntegerField(choices=SHIRT_CHOICES, null=True, blank=True, verbose_name='Modelo da Camisa')
    shirt_stamp = models.PositiveSmallIntegerField(choices=SHIRT_CHOICES, null=True, blank=True, verbose_name='Estampa da Camisa')
    collor1 = models.PositiveSmallIntegerField(choices=CORES, null=True, blank=True, verbose_name='Cor Brasão 1')
    collor2 = models.PositiveSmallIntegerField(choices=CORES, null=True, blank=True, verbose_name='Cor Brasão 2')
    collor3 = models.PositiveSmallIntegerField(choices=CORES, null=True, blank=True, verbose_name='Cor Brasão 3')

    def __str__(self):
        return self.teamdata.profile.user.username

@receiver(post_save, sender=TeamData)
def create_or_update_teamdata_teamshirt(sender, instance, created, **kwargs):
    if created:
        TeamShirt.objects.create(teamdata=instance)
    instance.teamshirt.save()