from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Profile, TeamData, TeamCrest, TeamShirt
from users.forms import SignUpForm, ProfileForm, TeamDataForm, TeamCrestForm, TeamShirtForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            teamdata = TeamData.objects.create(profile=profile)
            TeamCrest.objects.create(teamdata=teamdata)
            TeamShirt.objects.create(teamdata=teamdata)
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