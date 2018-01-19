# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, TeamData, TeamCrest, TeamShirt, UserTournament, Hint


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obrigatório. Informe um email válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'birth_date', 'cpf', 'gender', 'zip_code', 'street', 'number', 'complement', 'neighborhood', 'city', 'state')

class TeamDataForm(forms.ModelForm):
    class Meta:
        model = TeamData
        fields = ('team_name', 'real_team')

class TeamCrestForm(forms.ModelForm):
    class Meta:
        model = TeamCrest
        fields = ('crest_type', 'stamp', 'adornment', 'collor1', 'collor2', 'collor3')

class TeamShirtForm(forms.ModelForm):
    class Meta:
        model = TeamShirt
        fields = ('shirt_type', 'shirt_stamp', 'collor1', 'collor2', 'collor3')

class UserTournamentForm(forms.ModelForm):
    class Meta:
        model = UserTournament
        fields = ('realtournament',)

class BolaoForm(forms.ModelForm):
    class Meta:
        model = Hint
        fields = ('match', 'hint_home_team', 'hint_away_team',)