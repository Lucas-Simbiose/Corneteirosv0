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

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

class SoccerTeam(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Time de Futebol'
        verbose_name_plural = 'Times de Futebol'

class TeamData(models.Model):
    # Corinthians, Vasco, Atletico_pr, Atletico_mg, Palmeiras, Botafogo = 1, 2, 3, 4, 5, 6
    # TEAM_CHOICES = (
    #     (Corinthians, 'Corinthians'),
    #     (Vasco, 'Vasco'),
    #     (Atletico_pr, 'Atletico_pr'),
    #     (Atletico_mg, 'Atletico_mg'),
    #     (Palmeiras, 'Palmeiras'),
    #     (Botafogo, 'Botafogo'),
    # )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nome do Time')
    soccerteam = models.ForeignKey(SoccerTeam, null=True, blank=True, verbose_name='Time do Coração', on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.user.username

    class Meta:
        verbose_name = 'Team Data'

# @receiver(post_save, sender=Profile)
# def create_or_update_profile_teamdata(sender, instance, created, **kwargs):
#     if created:
#         TeamData.objects.create(teamdata=instance)
#     instance.teamdata.save()

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

    class Meta:
        verbose_name = 'Team Crest'

# @receiver(post_save, sender=TeamData)
# def create_or_update_teamdata_teamcrest(sender, instance, created, **kwargs):
#     if created:
#         TeamCrest.objects.create(teamcrest=instance)
#     instance.teamcrest.save()

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

    class Meta:
        verbose_name = 'Team Shirt'

# @receiver(post_save, sender=TeamData)
# def create_or_update_teamdata_teamshirt(sender, instance, created, **kwargs):
#     if created:
#         TeamShirt.objects.create(teamshirt=instance)
#     instance.teamshirt.save()


class RealTournament(models.Model):
    tournament = models.CharField(max_length=45)

    def __str__(self):
        return self.tournament

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'

class UserTournament(models.Model):
    teamdata = models.ForeignKey(TeamData, on_delete=models.CASCADE)
    realtournament = models.ForeignKey(RealTournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.teamdata.profile.user.username + " - " + str(self.realtournament)

    class Meta:
        verbose_name = 'Torneio do Usuário'
        verbose_name_plural = 'Torneios do Usuário'

class TeamTournament(models.Model):
    soccerteam = models.ForeignKey(SoccerTeam, on_delete=models.CASCADE)
    realtournament = models.ForeignKey(RealTournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.realtournament.tournament + " - " + self.soccerteam.name

    class Meta:
        verbose_name = 'Torneio do Time'
        verbose_name_plural = 'Torneios dos Times'

class Round(models.Model):
    realtournament = models.ForeignKey(RealTournament, on_delete=models.CASCADE)
    round_number = models.PositiveIntegerField()

    def __str__(self):
        return "Rodada número " + str(self.round_number)

    class Meta:
        verbose_name = 'Rodada'
        verbose_name_plural = 'Rodadas'

class Match(models.Model):
    soccerteam_home = models.ForeignKey(SoccerTeam, related_name='soccerteam_home', on_delete=models.CASCADE)
    soccerteam_away = models.ForeignKey(SoccerTeam, related_name='soccerteam_away', on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    match_number = models.PositiveIntegerField(null=True, blank=True)
    result_home_team = models.PositiveIntegerField(default=0)
    result_away_team = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Rodada " + str(self.round.round_number) + " - " + self.soccerteam_home.name + " vs " + self.soccerteam_away.name

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

class Hint(models.Model):
    realtournament = models.ForeignKey(RealTournament, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    usertournament = models.ForeignKey(UserTournament, on_delete=models.CASCADE)
    hint_home_team = models.PositiveIntegerField(null=True, blank=True)
    hint_away_team = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.match.soccerteam_home.name + " " + str(self.hint_home_team) + " - " + str(self.hint_away_team) + " " + self.match.soccerteam_away.name

    class Meta:
        verbose_name = 'Palpite'
        verbose_name_plural = 'Palpites'

# class UserMatchHint(models.Model):
#     hint = models.ForeignKey(Hint, on_delete=models.CASCADE)
#     match = models.ForeignKey(Match, on_delete=models.CASCADE)
#     usertournament = models.ForeignKey(UserTournament, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = 'Palpite do Usuário'
#         verbose_name_plural = 'Palpites do Usuário'