from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
    response = render(request, 'wwworkout/index.html')
    return response


def about(request):
    return render(request, 'wwworkout/about.html')


def user_redirect(request):
    # TODO: redirect to user's profile at /user/<username>
    if request.user.is_authenticated():
        username = request.user.username
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


def user_register(request):
    register = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)


# TODO: implement database access for context dictionaries
def user_profile(request, username):
    context_dict = None
    return render(request, 'wwworkout/user_profile.html', context_dict)


def user_timeline(request, username):
    context_dict = None
    return render(request, 'wwworkout/user_timeline.html', context_dict)


def user_groups(request, username):
    context_dict = None
    return render(request, 'wwworkout/user_groups.html', context_dict)


def group_profile(request, group_id):
    context_dict = None
    return render(request, 'wwworkout/group_profile.html', context_dict)


def group_leaderboards_index(request, group_id):
    context_dict = None
    return render(request, 'wwworkout/group_leaderboards_index.html', context_dict)


def group_leaderboards_workout(request, group_id):
    context_dict = None
    return render(request, 'wwworkout/group_leaderboards_workout.html', context_dict)


def group_member_list(request, group_id):
    context_dict = None
    return render(request, 'wwworkout/group_member_list.html', context_dict)


def add_group(request):
    # TODO: use forms (like with category creation in tango_with_django) and models to create new groups
    context_dict = None
    return render(request, 'wwworkout/add_group.html', context_dict)
