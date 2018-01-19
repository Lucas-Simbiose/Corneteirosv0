from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Profile, TeamData, TeamCrest, TeamShirt, UserTournament, Hint
from users.forms import SignUpForm, ProfileForm, TeamDataForm, TeamCrestForm, TeamShirtForm, UserTournamentForm, \
    BolaoForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            teamdata = TeamData.objects.create(profile=profile)
            TeamCrest.objects.create(teamdata=teamdata)
            TeamShirt.objects.create(teamdata=teamdata)
            # UserTournament.objects.create(teamdata=teamdata)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dados_time')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/users/login')
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'perfil.html', {'form': form})

@login_required(login_url='/users/login')
def teamdata(request):
    if request.method == "POST":
        form = TeamDataForm(request.POST, instance=request.user.profile.teamdata)
        if form.is_valid():
            form.save()
    else:
        form = TeamDataForm(instance=request.user.profile.teamdata)

    return render(request, 'dados_time.html', {'form': form})

@login_required(login_url='/users/login')
def teamcrest(request):
    if request.method == "POST":
        form = TeamCrestForm(request.POST, instance=request.user.profile.teamdata.teamcrest)
        if form.is_valid():
            form.save()
    else:
        form = TeamCrestForm(instance=request.user.profile.teamdata.teamcrest)

    return render(request, 'escudo_time.html', {'form': form})

@login_required(login_url='/users/login')
def teamshirt(request):
    if request.method == "POST":
        form = TeamShirtForm(request.POST, instance=request.user.profile.teamdata.teamshirt)
        if form.is_valid():
            form.save()
    else:
        form = TeamShirtForm(instance=request.user.profile.teamdata.teamshirt)

    return render(request, 'camisa_time.html', {'form': form})

@login_required(login_url='/users/login')
def usertournament(request):
    if request.method == "POST":
        form = UserTournamentForm(request.POST, instance=request.user.profile.teamdata)
        if form.is_valid():
            user = form.save()
            user.realtournament = form.cleaned_data.get('realtournament')
            UserTournament.objects.create(teamdata=request.user.profile.teamdata, realtournament=user.realtournament)
    else:
        form = UserTournamentForm()

    return render(request, 'torneios_usuario.html', {'form': form})

@login_required(login_url='/users/login')
def bolao(request):
    if request.method == "POST":
        form = BolaoForm(request.POST, instance=request.user.profile.teamdata)
        if form.is_valid():
            user = form.save()
            user.match = form.cleaned_data.get('match')
            user.realtournament = UserTournament.objects.get(realtournament=user.match.round.realtournament)
            user.usertournament = UserTournament.objects.get(teamdata=request.user.profile.teamdata)
            user.hint_home_team = form.cleaned_data.get('hint_home_team')
            user.hint_away_team = form.cleaned_data.get('hint_away_team')
            Hint.objects.create(realtournament=user.realtournament.realtournament, match=user.match, usertournament=user.usertournament, hint_home_team=user.hint_home_team, hint_away_team=user.hint_away_team)
    else:
        form = BolaoForm()

    return render(request, 'bolao.html', {'form': form})