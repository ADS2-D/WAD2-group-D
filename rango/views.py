from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rango.forms import UserForm, UserProfileForm, TeamForm
from rango.models import User, UserProfile, Workout, Team


def home(request):
    response = render(request, 'rango/index.html')
    return response

def about(request):
    return render(request, 'rango/about.html')


@login_required
def user_redirect(request):
    # TODO: redirect to user's profile at /user/<username>
    if request.user.is_authenticated():
        username = request.user.username
        return HttpResponseRedirect(reverse('home'))
        # redirect here
    else:
        return HttpResponseRedirect(reverse('home'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(usename=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # TODO: redirect user to their own profile
                return HttpResponseRedirect(reverse('user_redirect'))
            else:
                return HttpResponse('Your WWWorkout account has been disabled.')
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            return render(request, 'rango/login.html', {'invalid_login': 'Your login details are invalid.'})
    else:
        return render(request, 'rango/login.html', {'invalid_login': ''})


def user_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=True)
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

    return render(request, 'rango/register.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


# TODO: implement database access for context dictionaries
def user_profile(request, username):
    context_dict = {}

    try:
        user = User.objects.filter(username=username)
        userProfile = UserProfile.objects.filter(user=user)
        context_dict['workouts'] = Workout.objects.filter(user=user).order_by('-date')[:-5]
        context_dict['user_profile'] = userProfile
        context_dict['team_number'] = Team.objects.filter(user=user).count()
    except User.DoesNotExist:
        context_dict['workouts'] = None
        context_dict['user_profile'] = None
        context_dict['team_number'] = None

    return render(request, 'rango/profile.html', context_dict)


def user_timeline(request, username):
    context_dict = {}
    return render(request, 'rango/user_timeline.html', context_dict)


def user_groups(request, username):
    context_dict = None
    return render(request, 'rango/user_groups.html', context_dict)


def group_profile(request, group_id):
    context_dict = None
    return render(request, 'rango/group_profile.html', context_dict)


def group_leaderboards_index(request, group_id):
    context_dict = None
    return render(request, 'rango/group_leaderboards_index.html', context_dict)


def group_leaderboards_workout(request, group_id):
    context_dict = None
    return render(request, 'rango/group_leaderboards_workout.html', context_dict)


def group_member_list(request, group_id):
    context_dict = None
    return render(request, 'rango/group_member_list.html', context_dict)


def add_group(request):
    # TODO: use forms (like with category creation in tango_with_django) and models to create new groups
    context_dict = None
    return render(request, 'rango/add_group.html', context_dict)


@login_required
def add_workout(request):
    context_dict = None
    return render(request, 'rango/add_workout.html', context_dict)


def leaderboards_index(request):
    context_dict = None
    return render(request, 'rango/leaderboards_index.html', context_dict)


def leaderboards_single(request, workout_id):
    context_dict = None
    return render(request, 'rango/leaderboard.html', context_dict)
