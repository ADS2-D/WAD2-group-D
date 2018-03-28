from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile, Team, Workout, WorkoutType


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
    team_id = forms.CharField(widget=forms.HiddenInput(), initial="", required=False)
    picture = forms.ImageField(help_text='Upload a photo for your team', required=False)

    class Meta:
        model = Team
        fields = ('name',)


class WorkoutForm(forms.ModelForm):
    workoutType = forms.ModelChoiceField(queryset=WorkoutType.objects.all())
    #picture = forms.ImageField(upload_to='workout_images', blank=True)

    reps = forms.IntegerField(initial=0)
    sets = forms.IntegerField(initial=0)
    weights = forms.IntegerField(initial=0)

    distance = forms.IntegerField(initial=0)
    cadence = forms.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        model = Workout
        fields = ('workoutType', 'reps', 'sets', 'weights', 'distance', 'cadence',)
