from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile, Team, Workout


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text='Please enter a username.')
    password = forms.CharField(widget=forms.PasswordInput(), help_text='Please enter a password.')
    email = forms.CharField(help_text='Please enter email here.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(help_text='Upload a profile picture.', required=False)

    class Meta:
        model = UserProfile
        fields = ('picture',)


class TeamForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Add the name for your new team")
    team_id = forms.CharField(widget=forms.HiddenInput(), initial = "", required=False)
    picture = forms.ImageField(help_text = 'Upload a photo for your team', required=False)

    class Meta:
        model = Team
        fields = ('name',)


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('workout_id', 'reps', 'sets', 'weights', 'distance', 'cadence',)
