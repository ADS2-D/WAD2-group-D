from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile, Team, Workout


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class TeamForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Add the name for your new team")
    team_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Team
        fields = ('name', 'team_id', 'picture')


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('workout_id', 'reps', 'sets', 'weights', 'distance', 'cadence',)
