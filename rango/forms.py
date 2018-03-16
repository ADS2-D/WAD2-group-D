from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile, Team


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', )


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'teamid', 'picture')

