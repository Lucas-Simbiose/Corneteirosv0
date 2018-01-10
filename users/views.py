from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from users.forms import SignUpForm, ProfileForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/users/login')
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'perfil.html', {'form': form})