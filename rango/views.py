from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rango.forms import UserForm, UserProfileForm, TeamForm, WorkoutForm
from rango.models import User, UserProfile, Workout, Team, WorkoutType


def home(request):
    response = render(request, 'rango/index.html')
    return response


def about(request):
    return render(request, 'rango/about.html')


@login_required
def user_redirect(request):
    if request.user.is_authenticated():
        username = request.user.username
        return user_profile(request, username)
    else:
        return HttpResponseRedirect(reverse('home'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Your WWWorkout account has been disabled.')
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            return render(request, 'rango/login.html', {'invalid_login': 'Your login details are invalid.'})
    else:
        return render(request, 'rango/login.html', {'invalid_login': ''})


def register(request):
    context_dict = {}

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['registered'] = registered

    if registered:
        return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request, 'rango/register.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_profile(request, username):
    context_dict = {}

    if request.user.is_authenticated():
        if username == request.user.username:
            context_dict['own_profile'] = True
        else:
            context_dict['own_profile'] = False
    try:
        profile_user = User.objects.get(username=username)
        context_dict['workouts'] = Workout.objects.filter(user=profile_user).order_by('-date').reverse()
        context_dict['user_profile'] = UserProfile.objects.get(user=profile_user)
        context_dict['teams'] = Team.objects.filter(users=profile_user)
        context_dict['team_number'] = len(context_dict['teams'])
    except User.DoesNotExist:
        context_dict['workouts'] = None
        context_dict['user_profile'] = None
        context_dict['team_number'] = 0
        context_dict['teams'] = None

    return render(request, 'rango/profile.html', context_dict)


def user_timeline(request, username):
    context_dict = {}

    try:
        user = User.objects.filter(username=username)
        context_dict['workouts'] = Workout.objects.filter(user=user).order_by('-date')
        context_dict['user_profile'] = UserProfile.objects.filter(user=user)
    except User.DoesNotExist or Workout.DoesNotExist:
        context_dict['workouts'] = None
        context_dict['user_profile'] = None

    return render(request, 'rango/user_timeline.html', context_dict)


def user_teams(request, username):
    context_dict = {}

    try:
        user = User.objects.get(username=username)
        context_dict['user_teams'] = Team.objects.filter(users=user).order_by('-name')
    except User.DoesNotExist or Team.DoesNotExist:
        context_dict['user_teams'] = None

    context_dict['all_teams'] = Team.objects.all()

    return render(request, 'rango/user_teams.html', context_dict)


@login_required
def team_profile(request, team_id):
    context_dict = {}

    try:
        team = Team.objects.get(team_id=team_id)
        context_dict['team'] = Team.objects.get(team_id=team_id)
        users = Team.objects.get(team_id=team_id).users.all()
        context_dict['users'] = users
    except Team.DoesNotExist:
        context_dict['team'] = None
        context_dict['users'] = None

    user = request.user

    if request.method == "POST":
        if user in team.users.all():
            team.users.remove(user)
            return render(request, 'rango/team.html', context_dict)
        else:
            team.users.add(user)
            return render(request, 'rango/team.html', context_dict)

    return render(request, 'rango/team.html', context_dict)


def team_leaderboards_index(request, team_id):
    context_dict = {}

    try:
        team = Team.objects.get(team_id=team_id)

        context_dict['cardio'] = team.users.order_by('-distancepoints')
        context_dict['weights'] = team.users.order_by('-weightpoints')
        context_dict['workout_types'] = WorkoutType.objects.all()
    except Team.DoesNotExist:
        context_dict['cardio'] = None
        context_dict['weights'] = None
        context_dict['workout_types'] = None

    return render(request, 'rango/team_leaderboards_index.html', context_dict)


def team_leaderboards_workout(request, team_id, workout_id):
    context_dict = {}
    # TODO: context dictionary for workout specific team leaderboard
    return render(request, 'rango/team_leaderboards_workout.html', context_dict)


def team_member_list(request, team_id):
    context_dict = {}

    try:
        team = Team.objects.get(team_id=team_id)
        context_dict['users'] = team.user.all()
    except Team.DoesNotExist:
        context_dict['users'] = None

    return render(request, 'rango/team_member_list.html', context_dict)


@login_required
def add_team(request):
    form = TeamForm()
    user = request.user

    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            team = form.save(commit=True)
            team.users.clear()
            team.users.add(user)

            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)

    return render(request, 'rango/add_team.html', {'form': form})


@login_required
def add_workout(request, username):
    form = WorkoutForm()

    try:
        user = User.objects.get(username=username)
        if request.user != user:
            return user_redirect(request)
    except User.DoesNotExist:
        user = None

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            if user:
                workout = form.save(commit=False)
                workout.user = user
                workout.distancepoints = workout.distance * (1 + workout.cadence)
                workout.weightpoints = workout.sets * workout.reps * workout.weights
                workout.save()
                userProf = UserProfile.objects.get(user=user)
                userProf.distancepoints += workout.distancepoints
                userProf.weightpoints += workout.weightpoints
            return user_redirect(request)
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'rango/add_workout.html', context_dict)


def leaderboards_index(request):
    context_dict = {}

    try:
        context_dict['cardio_users'] = UserProfile.objects.all().order_by('-cardiopoints')
        context_dict['weights_users'] = UserProfile.objects.all().order_by('-weightpoints')
        context_dict['workout_types'] = WorkoutType.objects.all()
    except UserProfile.DoesNotExist:
        context_dict['cardio_users'] = None
        context_dict['weights_users'] = None
        context_dict['workout_types'] = None

    return render(request, 'rango/leaderboards_index.html', context_dict)


def leaderboards_single(request, workout_id):
    context_dict = {}

    try:
        workout_type = WorkoutType.objects.get(name=workout_id)

        if workout_type.cardio:
            context_dict['workouts'] = Workout.objects.filter(workoutType=workout_type).order_by('-distancepoints')
        elif workout_type.weights:
            context_dict['workouts'] = Workout.objects.filter(workoutType=workout_type).order_by('-weightpoints')
    except WorkoutType.DoesNotExist:
        context_dict['workouts'] = None

    return render(request, 'rango/leaderboard.html', context_dict)
